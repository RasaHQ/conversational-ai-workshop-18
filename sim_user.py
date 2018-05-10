from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import uuid
from enum import Enum
import numpy as np

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.events import ActionExecuted, UserUttered
from rasa_core.interpreter import RegexInterpreter

class UserState(Enum):
    INFORM = "inform"
    EXPLAIN = "explain"
    DIDTHATWORK = "did_that_work"
    CORRECT = "correct"
    CHITCHAT = "chitchat"
    

class SimulatedUser(object):
    def __init__(self):
        self.sender_id = uuid.uuid4().hex
        self.state = UserState.INFORM
        self.informativeness = 1.1
        self.preferences = {
            "location": ["paris","london","rome"],
            "people": ["1", "2", "4","6"],
            "startdate": ["today", "next week", "May 25th"],
            "enddate": ["tomorrow", "next week", "May 26th"],
            "price": ["cheap", "mid-range", "expensive"]
        }
        self.provided = set()
        self.last_utter = None
        self.last_system_utter = None

    def new_state(self):
        self.state = np.random.choice(UserState, p=[0.8,0.05,0.05,0.05,0.05])

    def pick_entities(self):
        # override state if none or all slots have already been provided
        if len(self.preferences) == len(self.provided):
            self.state = UserState.CORRECT
        elif len(self.provided) == 0:
            self.state = UserState.INFORM

        if self.state == UserState.INFORM:
            n_ent = np.random.poisson(self.informativeness - 1) + 1
            candidates = set(self.preferences.keys()) - self.provided
        elif self.state == UserState.CORRECT:
            n_ent = 1
            candidates = self.provided
        else:
            return ""
        ents = np.random.choice(list(candidates),
                                size=n_ent,
                                replace=False)
        #print(ents)
        self.provided = self.provided.union(set(ents))

        ents_str = ",".join([
            '"{}": "{}"'.format(k, 
                np.random.choice(self.preferences[k]))
            for k in ents])
        #print(ents_str)
        return "{"+ents_str+"}"
        

    def next_utter(self):
        self.new_state()
        entities = self.pick_entities()        
        #print("entities in next utter: {}".format(entities))
        utter = "/{}{}".format(self.state.value, entities)
        self.last_utter = {"intent": self.state.value, "entities": entities}
        return utter

    def response_correct(self, action):
        intent = self.last_utter["intent"]
        if intent == UserState.CHITCHAT.value:
            return action == "utter_chitchat"
        elif intent in [UserState.INFORM.value, UserState.CORRECT.value]:
            if len(self.provided) < len(self.preferences):
                try:
                    entity = action.split("utter_ask_")[1]
                    return "utter_ask" in action and entity not in self.provided
                except:
                    return False
            else:
                return action == "utter_filled_slots"
        elif intent == UserState.DIDTHATWORK.value:
            if len(self.provided) < len(self.preferences):
                return action == "utter_more_info_hotel"
            else:
                return action == "utter_worked_hotel"
        elif intent == UserState.EXPLAIN.value:
            try:
                entity = user.last_system_utter.split("utter_ask_")[1]
                return action == "utter_explain_{}_hotel".format(entity)
            except:
                return "utter_explain" in action
        else:
            raise ValueError("unhandled case: {} {}".format(self.last_utter, action))

def print_story(agent, user_id):
    tracker = agent.tracker_store.get_or_create_tracker(user_id)
    print(tracker.export_stories())


def run_sim_user(agent, max_steps=8):
    success = True
    user = SimulatedUser()
    first_utter = "request_hotel"
    result = agent.start_message_handling(first_utter, user.sender_id)
    user.last_system_utter = result["next_action"]
    agent.continue_message_handling(user.sender_id,
                                    result["next_action"], [])
    for _ in range(max_steps):
        utter = user.next_utter()
        result = agent.start_message_handling(utter, user.sender_id)
        action = result["next_action"]
        if 'utter' in action:
            user.last_system_utter = action
        if not user.response_correct(action):
            print_story(agent, user.sender_id)
            print(action)
            return 0
        while action is not None:
            if 'utter' in action:
                user.last_system_utter = action
            result = agent.continue_message_handling(user.sender_id,
                                                     action,
                                                     [])
            action = result["next_action"]


    print_story(agent, user.sender_id)
    return 1


def evaluate_policy(policy_model_path, num_dialogues=10):
    interpreter = RegexInterpreter()

    agent = Agent.load(policy_model_path, interpreter=interpreter)
    n_correct = 0
    for _ in range(num_dialogues):
        n_correct += run_sim_user(agent)
    return n_correct


n = evaluate_policy("models/dialgue_all")
print("n correct {} ".format(n))
