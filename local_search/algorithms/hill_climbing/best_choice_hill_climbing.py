from typing import Union
from local_search.algorithms.hill_climbing.hill_climbing import HillClimbing

from local_search.problems.base.state import State
from local_search.problems.base.problem import Problem

class BestChoiceHillClimbing(HillClimbing):
    """
    Implementation of hill climbing local search.

    The most known version of hill climbing.
    Algorithm works, by checking all the available moves
    and selecting the best one that improves the current state.
    """

    def _climb_the_hill(self, model: Problem, state: State) -> Union[State, None]:
        # TODO:
        # - look first at the `first_choice_hill_climbing.py` and understand it
        # - go trough all the neighbors :
        #   [1] `self._get_neighbours` is your friend
        # - find the worst, but still improving improving state 
        #   [1] one with minimal model.improvement(....) > 0 
        # return it (or the current state if there is no improving state)!

        improvement=[state]

        for neighbour in self._get_neighbours(model, state):
            if model.improvement(neighbour, state) > 0:
                improvement.append(neighbour)

        return max(improvement)
        
     

        raise NotImplementedError()
