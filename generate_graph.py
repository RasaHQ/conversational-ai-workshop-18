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
    while count < 3:
        correct_keras = []
        correct_embed = []
        for i in percentages:
            train_domain_policy(cmdline_args.data,
                                starspace=True,
                                exclusion_file=cmdline_args.exclude,
                                exclusion_percentage=i,
                                epoch_no=cmdline_args.epochs,
                                embed_dim=20
                                )

            no = run_story_evaluation(cmdline_args.stories,
                                      'models/dialogue_embed')

            correct_embed.append(no)

            train_domain_policy(cmdline_args.data,
                                starspace=False,
                                exclusion_file=cmdline_args.exclude,
                                exclusion_percentage=i
                                )

            no = run_story_evaluation(cmdline_args.stories,
                                      'models/dialogue_keras')
            correct_keras.append(no)
        num_correct['keras'].append(correct_keras)
        num_correct['embed'].append(correct_embed)
        count += 1
    percentages = [100-x for x in percentages]

    memo = [x/100.0 for x in percentages]
    no_stories = len(StoryFileReader.read_from_file(cmdline_args.exclude,
                                                    TemplateDomain.load(
                                                        'domain.yml')))
    num_correct['no_of_stories'] = [round((x/100.0) * no_stories) for x in percentages]
    file_name = cmdline_args.exclude[:-3] + '.p'
    pickle.dump(num_correct, open(file_name, 'wb'))
    # num_correct['keras'] = [x/float(no_stories) for x in num_correct['keras']]
    # num_correct['embed'] = [x/float(no_stories) for x in num_correct['embed']]
    # plt.plot(percentages, num_correct['keras'], label='keras', marker='.')
    # plt.plot(percentages, num_correct['embed'], label='embed', marker='.')
    # plt.plot(percentages, memo, '--', label='memoization')
    # plt.xlabel('percentage of data present')
    # plt.ylabel('accuracy')
    # plt.xlim([0, 100])
    # plt.ylim([0, 1.05])
    #
    # plt.legend(loc=4)
    # plt.show()
    # defaultdict(<type 'list'>, {u'embed': [29, 27, 24, 20, 14, 7, 4, 0], u'keras': [29, 28, 21, 16, 14, 4, 1, 0]})
    # print(num_correct)
    logger.info("Finished evaluation")
