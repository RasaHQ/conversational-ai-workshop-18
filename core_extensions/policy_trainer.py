from rasa_core.training.dsl import StoryFileReader
from rasa_nlu import utils as nlu_utils
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies import PolicyTrainer

from rasa_core.training.structures import StoryGraph
from rasa_core.training.generator import TrainingsDataGenerator
from rasa_core.agent import Agent
from rasa_core.domain import check_domain_sanity


def extract_story_graph(resource_name, domain,
                        interpreter=RegexInterpreter(),
                        exclusion_file=None,
                        exclusion_percentage=None):

    story_steps = StoryReader.read_from_folder(resource_name,
                                               domain, interpreter,
                                               exclusion_file=exclusion_file,
                                               exclusion_percentage=exclusion_percentage)

    return StoryGraph(story_steps)


class CustomPolicyTrainer(PolicyTrainer):

    def train(self,
              resource_name=None,  # type: Optional[Text]
              augmentation_factor=20,  # type: int
              max_training_samples=None,  # type: Optional[int]
              max_number_of_trackers=2000,  # type: int
              remove_duplicates=True,  # type: bool
              exclusion_file=None,
              exclusion_percentage=None,
              **kwargs  # type: **Any
              ):
        # type: (...) -> None
        """Trains a policy on a domain using training data from a file.

        :param resource_name: story file containing the training conversations
        :param augmentation_factor: how many stories should be created by
                                    randomly concatenating stories
        :param max_training_samples: specifies how many training samples to
                                     train on - `None` to use all examples
        :param max_number_of_trackers: limits the tracker generation during
                                       story file parsing - `None` for
                                       unlimited
        :param remove_duplicates: remove duplicates from the training set
                                  before training
        :param kwargs: additional arguments passed to the underlying ML trainer
                       (e.g. keras parameters)
        :return: trained policy
        """

        # logger.debug("Policy trainer got kwargs: {}".format(kwargs))
        check_domain_sanity(self.domain)

        training_trackers, events_metadata = self.extract_trackers(
                resource_name,
                self.domain,
                augmentation_factor=augmentation_factor,
                remove_duplicates=remove_duplicates,
                max_number_of_trackers=max_number_of_trackers,
                exclusion_file=exclusion_file,
                exclusion_percentage=exclusion_percentage
        )

        self.ensemble.train(training_trackers, events_metadata, self.domain,
                            max_training_samples=max_training_samples,
                            **kwargs)

    @staticmethod
    def extract_trackers(
            resource_name,  # type: Text
            domain,  # type: Domain
            remove_duplicates=True,  # type: bool
            augmentation_factor=20,  # type: int
            max_number_of_trackers=2000,  # type: int
            tracker_limit=None,  # type: Optional[int]
            use_story_concatenation=True,  # type: bool
            exclusion_file=None,
            exclusion_percentage=None


    ):
        # type: (...) -> GeneratorOut

        if resource_name:

            # TODO pass extract_story_graph as a function or
            # TODO pass graph to agent
            # TODO to support code creating stories
            graph = extract_story_graph(resource_name, domain,
                                        exclusion_file=exclusion_file,
                                        exclusion_percentage=exclusion_percentage)

            g = TrainingsDataGenerator(graph, domain,
                                       remove_duplicates,
                                       augmentation_factor,
                                       max_number_of_trackers,
                                       tracker_limit,
                                       use_story_concatenation)
            return g.generate()
        else:
            return [], None


class StoryReader(StoryFileReader):

    @staticmethod
    def read_from_folder(resource_name, domain, interpreter=RegexInterpreter(),
                         template_variables=None, exclusion_file=None,
                         exclusion_percentage=None):
        """Given a path reads all contained story files."""

        story_steps = []
        for f in nlu_utils.list_files(resource_name):
            steps = StoryFileReader.read_from_file(f, domain, interpreter,
                                                   template_variables)
            if exclusion_file and exclusion_percentage != 0:
                if f == exclusion_file:
                    # need to make this round up
                    idx = int(exclusion_percentage/100.0 * len(steps))
                    steps = steps[:-idx]

            story_steps.extend(steps)
        return story_steps


class CustomAgent(Agent):

    def train(self, resource_name=None, model_path=None,
              remove_duplicates=True,
              exclusion_file=None,
              exclusion_percentage=None,
              **kwargs):
        # type: (Optional[Text], Optional[Text], bool, **Any) -> None
        """Train the policies / policy ensemble using dialogue data from
        file"""
        trainer = CustomPolicyTrainer(self.policy_ensemble, self.domain)
        trainer.train(resource_name, remove_duplicates=remove_duplicates,
                      exclusion_file=exclusion_file,
                      exclusion_percentage=exclusion_percentage,
                      **kwargs)

        if model_path:
            self.persist(model_path)
