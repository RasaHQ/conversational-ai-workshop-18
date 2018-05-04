from rasa_core.training.dsl import StoryFileReader
from rasa_nlu import utils as nlu_utils
from rasa_core.interpreter import RegexInterpreter

from rasa_core.training.structures import StoryGraph
from rasa_core.training.generator import TrainingDataGenerator
from rasa_core.agent import Agent


def extract_story_graph(
        resource_name,  # type: Text
        domain,  # type: Domain
        interpreter=None,  # type: Optional[NaturalLanguageInterpreter]
        exclusion_file=None,
        exclusion_percentage=None
):
    # type: (...) -> StoryGraph

    if not interpreter:
        interpreter = RegexInterpreter()
    story_steps = StoryReader.read_from_folder(resource_name,
                                               domain, interpreter,
                                               exclusion_file=exclusion_file,
                                               exclusion_percentage=exclusion_percentage)
    return StoryGraph(story_steps)


def load_data(
        resource_name,  # type: Text
        domain,  # type: Domain
        remove_duplicates=True,  # type: bool
        augmentation_factor=20,  # type: int
        max_number_of_trackers=2000,  # type: int
        tracker_limit=None,  # type: Optional[int]
        use_story_concatenation=True,  # type: bool
        exclusion_file=None,
        exclusion_percentage=None,
):
    # type: (...) -> List[DialogueStateTracker]

    if resource_name:
        graph = extract_story_graph(resource_name, domain,
                                    exclusion_file=exclusion_file,
                                    exclusion_percentage=exclusion_percentage)

        g = TrainingDataGenerator(graph, domain,
                                  remove_duplicates,
                                  augmentation_factor,
                                  max_number_of_trackers,
                                  tracker_limit,
                                  use_story_concatenation)
        return g.generate()
    else:
        return []


class StoryReader(StoryFileReader):

    @staticmethod
    def read_from_folder(resource_name, domain, interpreter=RegexInterpreter(),
                         template_variables=None, exclusion_file=None,
                         exclusion_percentage=None):
        """Given a path reads all contained story files."""
        import random
        # random.seed(666)
        story_steps = []
        for f in nlu_utils.list_files(resource_name):

            if (f.split('_')[1] == 'happy.md' or f.split('_')[1] ==
                    exclusion_file.split('_')[1]):
                steps = StoryFileReader.read_from_file(f, domain, interpreter,
                                                       template_variables)
                if exclusion_file and exclusion_percentage != 0:
                    if f == exclusion_file:
                        idx = int(round(exclusion_percentage/100.0 * len(steps)))
                        random.shuffle(steps)
                        steps = steps[:-idx]

                story_steps.extend(steps)
        return story_steps


class CustomAgent(Agent):

    def load_data(self,
                  resource_name,  # type: Text
                  remove_duplicates=True,  # type: bool
                  augmentation_factor=20,  # type: int
                  max_number_of_trackers=2000,  # type: int
                  tracker_limit=None,  # type: Optional[int]
                  use_story_concatenation=True,  # type: bool
                  exclusion_file=None,
                  exclusion_percentage=None
                  ):
        # type: (...) -> List[DialogueStateTracker]

        return load_data(resource_name, self.domain, remove_duplicates,
                         augmentation_factor, max_number_of_trackers,
                         tracker_limit, use_story_concatenation,
                         exclusion_file=exclusion_file,
                         exclusion_percentage=exclusion_percentage)
