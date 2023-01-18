from typing import Union
from local_search.algorithms.hill_climbing.hill_climbing import HillClimbing
from local_search.problems.base.state import State
from local_search.problems.base.problem import Problem


class RandomChoiceHillClimbing(HillClimbing):
    """
    Stochastic variant of hill climbing local search.

    Algorithm works, by randomly sampling the neighborhood
    and selecting a move if it improves the current state.
    """

    def _climb_the_hill(self, model: Problem, state: State) -> Union[State, None]:
        # TODO:
        # - look first at the `first_choice_hill_climbing.py` and understand it
        # - get single random neighbor:
        #   [1] use `self._get_random_neighbours(model, state)`` instead of `self._get_neighbours(model, state)`;
        #       it's an iterator over neighbors in random order
        #   [2] in python `next(iterator)` takes a single element from iterator ;)
        # - if the random state is better than the current one, return it
        #   [1] `model.improvement` is your friend
        # - otherwise return the current state

        for neighbour in self._get_random_neighbours(model, state):
            n2 = next(neighbour)
            if model.improvement(n2, neighbour) > 0:
                return n2
            else:
                return state
        raise NotImplementedError()