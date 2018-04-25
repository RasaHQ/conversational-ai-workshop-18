from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging

from rasa_core import utils

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

    utils.add_logging_option_arguments(parser)
    return parser


if __name__ == '__main__':
    # configure_logging()
    # Running as standalone python application
    from collections import defaultdict
    arg_parser = create_argument_parser()
    cmdline_args = arg_parser.parse_args()
    num_correct = defaultdict(list)

    logging.basicConfig(level='INFO')
    percentages = [0, 10, 30, 50, 70, 100]
    for i in percentages:
        train_domain_policy('data/train/',
                            starspace=True,
                            exclusion_file=cmdline_args.exclude,
                            exclusion_percentage=i
                            )

        no = run_story_evaluation(cmdline_args.stories,
                                  'models/dialogue_embed')

        num_correct['embed'].append(no)

        train_domain_policy('data/train/',
                            starspace=False,
                            exclusion_file=cmdline_args.exclude,
                            exclusion_percentage=i
                            )

        no = run_story_evaluation(cmdline_args.stories,
                                  'models/dialogue_keras')
        num_correct['keras'].append(no)

    percentages = [0, 30, 50, 70, 90, 100]
    memo = [0, 0.3, 0.5, 0.7, 0.9, 1]
    num_correct['keras'] = [x/17.0 for x in num_correct['keras'][::-1]]
    num_correct['embed'] = [x/17.0 for x in num_correct['embed'][::-1]]
    plt.plot(percentages, num_correct['keras'], label='keras', marker='.')
    plt.plot(percentages, num_correct['embed'], label='embed', marker='.')
    plt.plot(percentages, memo, '--', label='memoization')
    plt.xlabel('percentage of data present')
    plt.ylabel('accuracy')
    plt.xlim([0, 100])
    plt.ylim([0, 1.05])

    plt.legend(loc=4)
    plt.show()

    print(num_correct)
    logger.info("Finished evaluation")
