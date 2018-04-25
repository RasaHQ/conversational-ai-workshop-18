from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging

from rasa_core import utils

from test_stories import run_story_evaluation
from trainer import train_domain_policy

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


if __name__ == '__main__':
    # configure_logging()
    # Running as standalone python application
    arg_parser = create_argument_parser()
    cmdline_args = arg_parser.parse_args()
    num_correct = []

    logging.basicConfig(level='INFO')
    for i in [0, 10, 30, 50, 70, 100]:
        train_domain_policy('data/train/',
                            'models/dialogue_keras',
                            exclusion_file='data/train/restaurant_happy.md',
                            exclusion_percentage=i
                            )

        no = run_story_evaluation(cmdline_args.stories,
                                  cmdline_args.core)

        num_correct.append(no)
    print(num_correct)
    logger.info("Finished evaluation")
