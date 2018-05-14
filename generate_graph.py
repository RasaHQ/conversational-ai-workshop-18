from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging

from rasa_core import utils
from ast import literal_eval

from test_stories import run_story_evaluation
from trainer import train_domain_policy

import matplotlib.pyplot as plt

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
            '--exclude',
            type=str,
            default=None,
            help="file to exclude from training")
    parser.add_argument(
            '--data',
            type=str,
            default='data/train',
            help="training data")
    parser.add_argument(
            '--epochs',
            type=int,
            default=2000,
            help="number of epochs")

    utils.add_logging_option_arguments(parser)
    return parser


if __name__ == '__main__':
    # configure_logging()
    # Running as standalone python application
    logging.basicConfig(level="INFO")
    from collections import defaultdict
    from rasa_core.training.dsl import StoryFileReader
    from rasa_core.domain import TemplateDomain
    import pickle
    # from math import log
    arg_parser = create_argument_parser()
    cmdline_args = arg_parser.parse_args()
    num_correct = defaultdict(list)

    logging.basicConfig(level='INFO')
    percentages = [0, 5, 25, 50, 70, 90, 95, 100]
    count = 0
    while count < 1:
        correct_keras = defaultdict(list)
        correct_embed = defaultdict(list)

        for i in percentages:
            logging.info("Starting exclusion round {}/{}".format(percentages.index(i)+1, len(percentages)))
            train_domain_policy(cmdline_args.data,
                                starspace=True,
                                exclusion_file=cmdline_args.exclude,
                                exclusion_percentage=i,
                                epoch_no=cmdline_args.epochs,
                                embed_dim=20,
                                output_path='models/dialogue_embed'
                                )
            for s in literal_eval(cmdline_args.stories):
                no = run_story_evaluation(s, 'models/dialogue_embed')
                correct_embed[s.split('/')[-1]].append(no)

            train_domain_policy(cmdline_args.data,
                                starspace=False,
                                exclusion_file=cmdline_args.exclude,
                                exclusion_percentage=i,
                                output_path='models/dialogue_keras'
                                )

            for s in literal_eval(cmdline_args.stories):
                no = run_story_evaluation(s, 'models/dialogue_keras')
                correct_keras[s.split('/')[-1]].append(no)

        count += 1
    percentages = [100-x for x in percentages]

    no_stories = len(StoryFileReader.read_from_file(cmdline_args.exclude,
                                                    TemplateDomain.load(
                                                        'domain.yml')))
    correct_embed['no_of_stories'] = [round((x/100.0) * no_stories) for x in percentages]
    correct_keras['no_of_stories'] = [round((x/100.0) * no_stories) for x in percentages]
    pickle.dump(correct_embed, open('embed_results.p', 'wb'))
    pickle.dump(correct_keras, open('keras_results.p', 'wb'))

    logger.info("Finished evaluation")
