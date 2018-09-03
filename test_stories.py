from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import uuid

from tqdm import tqdm

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.events import ActionExecuted, UserUttered
from rasa_core.interpreter import RegexInterpreter
from rasa_core.training import extract_story_graph
from rasa_core.training.generator import TrainingDataGenerator
from rasa_core.channels.channel import CollectingOutputChannel
from rasa_core.channels import UserMessage

logger = logging.getLogger(__name__)


def create_argument_parser():
    """Create argument parser for the evaluate script."""

    parser = argparse.ArgumentParser(
            description='evaluates a dialogue model')
    parser.add_argument(
            '-s', '--stories',
            type=str,
            required=True,
            help="file that contains the stories to evaluate on")
    parser.add_argument(
            '-m', '--max_stories',
            type=int,
            default=None,
            help="maximum number of stories to test on")
    parser.add_argument(
            '-d', '--core',
            required=True,
            type=str,
            help="core model to run with the server")

    utils.add_logging_option_arguments(parser)
    return parser


def run_story_evaluation(story_file, policy_model_path,
                         max_stories=None, shuffle_stories=True):
    """Test the stories from a file, running them through the stored model."""

    interpreter = RegexInterpreter()

    agent = Agent.load(policy_model_path, interpreter=interpreter)

    story_graph = extract_story_graph(story_file, agent.domain,
                                      interpreter)

    g = TrainingDataGenerator(story_graph, agent.domain,
                              use_story_concatenation=False,
                              tracker_limit=100,
                              augmentation_factor=0)
    completed_trackers = g.generate()

    logger.info(
            "Evaluating {} stories\nProgress:".format(len(completed_trackers)))

    num_correct = 0

    for tracker in tqdm(completed_trackers):
        sender_id = "default-" + uuid.uuid4().hex

        events = list(tracker.events)

        action_to_log = None
        events_to_log = []

        preds = []
        actual = []

        for i, event in enumerate(events[1:]):
            if isinstance(event, UserUttered):

                msg = UserMessage(event.text,
                                  CollectingOutputChannel(),
                                  sender_id)
                agent.log_message(msg)
                result = agent.predict_next(sender_id=sender_id)
                next_action = 'action_listen'
                best_score = 0
                for actions_scores in result["scores"]:
                    if actions_scores['score'] > best_score:
                        next_action = actions_scores['action']
                        best_score = actions_scores['score']

                preds.append(next_action)

                action_to_log = None

            elif isinstance(event, ActionExecuted):
                if action_to_log is not None:
                    result = agent.predict_next(sender_id=sender_id)
                    next_action = 'action_listen'
                    best_score = 0
                    for actions_scores in result["scores"]:
                        if actions_scores['score'] > best_score:
                            next_action = actions_scores['action']
                            best_score = actions_scores['score']

                    preds.append(next_action)

                agent.execute_action(sender_id, event.action_name, CollectingOutputChannel())
                actual.append(event.action_name)
                action_to_log = event.action_name
                events_to_log = []

            else:
                events_to_log.append(event)

        # final unlogged action
        # if action_to_log is not None:
        #     actual.append(action_to_log)

        print("=====================")
        print("actions in story: {}".format(len(actual)))
        # print(actual)

        # print("predicted actions: ")
        # print(preds)

        if preds == actual:
            num_correct += 1
        print("equal ? {}".format(preds == actual))

        if preds != actual:
            for idx, a in enumerate(actual):
                if a == preds[idx]:
                    print(a)
                else:
                    print("{:30} {}".format(a, preds[idx]))

    logger.info("{} stories correct out of {}".format(num_correct,
                                                      len(completed_trackers)))

    return num_correct


if __name__ == '__main__':
    # configure_logging()
    # Running as standalone python application
    arg_parser = create_argument_parser()
    cmdline_args = arg_parser.parse_args()

    logging.basicConfig(level='INFO')
    run_story_evaluation(cmdline_args.stories,
                         cmdline_args.core,
                         cmdline_args.max_stories)
    logger.info("Finished evaluation")
