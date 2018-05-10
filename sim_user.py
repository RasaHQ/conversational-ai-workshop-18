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
            #"cuisine": "french",
            "location": "paris",
            "people": "4",
            "start_date": "today",
            "end_date": "tomorrow",
            "price": "expensive"
        }
        self.provided = set()
        self.last_utter = None

    def new_state(self):
        self.state = np.random.choice(UserState, p=[0.8,0.05,0.05,0.05,0.05])

    def pick_entities(self):
        if self.state == UserState.INFORM:
            n_ent = np.random.poisson(self.informativeness - 1) + 1
        elif self.state == UserState.CORRECT:
            n_ent = 1
        else:
            return ""
        ents = np.random.choice(list(self.preferences.keys()),
                                size=n_ent,
                                replace=False)
        #print(ents)
        self.provided = self.provided.union(set(ents))

        ents_str = ",".join(['"{}": "{}"'.format(k, self.preferences[k])
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
                return "utter_ask" in action
        elif intent == UserState.DIDTHATWORK.value:
            if len(self.provided) < len(self.preferences):
                return action == "utter_more_info_hotel"
            else:
                return action == "utter_worked_hotel"
        elif intent == UserState.EXPLAIN.value:
            # TODO log previous requested action
            return "utter_explain" in action
        else:
            raise ValueError("unhandled case: {} {}".format(self.last_utter, action))

def print_story(agent, user_id):
    tracker = agent.tracker_store.get_or_create_tracker(user_id)
    print(tracker.export_stories())


def run_sim_user(agent, max_steps=5):
    success = True
    user = SimulatedUser()
    first_utter = "request_hotel"
    result = agent.start_message_handling(first_utter, user.sender_id)
    agent.continue_message_handling(user.sender_id,
                                    result["next_action"], [])
    for _ in range(max_steps):
        utter = user.next_utter()
        print("next utter {} ".format(utter))
        result = agent.start_message_handling(utter, user.sender_id)
        action = result["next_action"]
        if not user.response_correct(action):
            print_story(agent, user.sender_id)
            print(action)
            return 0
        while action is not None:
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


#n = evaluate_policy("models/dialgue_all")
#print("n correct {} ".format(n))
