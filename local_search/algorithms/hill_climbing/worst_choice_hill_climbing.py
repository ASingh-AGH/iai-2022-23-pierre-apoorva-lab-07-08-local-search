from typing import Union
from local_search.algorithms.hill_climbing.hill_climbing import HillClimbing
from local_search.problems.base.state import State
from local_search.problems.base.problem import Problem


class WorstChoiceHillClimbing(HillClimbing):
    """
    Implementation of hill climbing local search.

    Pretty exotic version of hill climbing. Algorithm works, by checking all the available moves
    and selecting the worst one that improves the current state.
    """

    def _climb_the_hill(self, model: Problem, state: State) -> Union[State, None]:
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

        n = len(improvement)

        for i in range(n):
            for j in range(0, n - 1):
                if model.improvement(improvement[j], improvement[j+1]) > 0:
                    improvement[j], improvement[j + 1] = improvement[j + 1], improvement[j]

        
        if len(improvement) > 1:
            return improvement[1]
        else:
            return state
        raise NotImplementedError()
