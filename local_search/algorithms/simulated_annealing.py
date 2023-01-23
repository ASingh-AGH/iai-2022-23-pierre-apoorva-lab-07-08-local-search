import random
from typing import Union
from local_search.algorithms import SubscribableAlgorithm, AlgorithmConfig
from local_search.problems.base.state import State
from local_search.problems.base.problem import Problem
import random
from dataclasses import dataclass
import mpmath
from enum import IntEnum, auto


class SAEscapeStrategy(IntEnum):
    RandomRestart = 0
    Perturbation = auto()
    Reheat = auto()


@dataclass
class SimulatedAnnealingConfig(AlgorithmConfig):
    initial_temperature: int = 5
    cooling_step: float = 0.999
    min_temperature: float = 1e-10
    escape_random_restart_probability: float = 0.33
    escape_perturbation_probability: float = 0.33
    escape_perturbation_size: int = 50
    escape_reheat_probability: float = 0.33
    escape_reheat_ratio: float = 0.1


DEFAULT_CONFIG = SimulatedAnnealingConfig()


class SimulatedAnnealing(SubscribableAlgorithm):
    """
    Implementation of the simulated annealing algorithm.

    A version of stochastic hill climbing, that allows going downhills. 
    """

    def __init__(self, config: SimulatedAnnealingConfig = None):
        self.config = config or DEFAULT_CONFIG
        self.temperature = self.config.initial_temperature
        self._local_optimum_escapes = 0
        self._escape_strategies = list(SAEscapeStrategy)
        self._escape_probabilities = [0 for _ in self._escape_strategies]
        self._escape_probabilities[SAEscapeStrategy.RandomRestart.value] = self.config.escape_random_restart_probability
        self._escape_probabilities[SAEscapeStrategy.Perturbation.value] = self.config.escape_perturbation_probability
        self._escape_probabilities[SAEscapeStrategy.Reheat.value] = self.config.escape_reheat_probability
        self.cooling_time = 0
        super().__init__(config=config)

    def _find_next_state(self, model: Problem, state: State) -> Union[State, None]:
        # TODO:
        # — find random neighbour:
        #   [1] `self._get_random_neighbours` creates a generator of the random neighbors
        #   [2] use `next` to read a single element from a generator, e.g. `next(generator)`
        # — if the neighbour is better then mark is as the next state:
        #   [1] use `model.improvement` to check for improvement
        # — otherwise calculate the probability of transition using `self._calculate_transition_probability`
        #   [1] use random.random() to generate a random number from range [0,1];
        #   [2] compare it to the probability to check if algorithm should go to the new state
        # — update temperature using `self._update_temperature`
        # — return the new state
        #----------------my code start---------------------------------------
        random_neighbours = self._get_random_neighbours(model, state)
        next_state = next(random_neighbours)
        if model.improvement(state, next_state) > 0:
            self._update_temperature()
            return next_state
        else:
            transition_probability = self._calculate_transition_probability(model, state, next_state)
            if random.random() < transition_probability:
                self._update_temperature()
                return next_state
            else:
                self._update_temperature()
                return state
        #----------------end my code---------------------------------------
        #raise NotImplementedError()

    def _calculate_transition_probability(self, model: Problem, old_state: State, new_state: State) -> float:
        # TODO:
        # - calculate probability of transition according to the metropolis function
        #   p = exp(delta / temperature) [1]
        # where: 
        #   - delta is the improvement of the objective function[2]
        #
        # [1] `mpmath.exp` calculates `exp` function
        # [2] `model.improvement` method
        #----------------my code start---------------------------------------
        delta = model.improvement(old_state, new_state)
        p = mpmath.exp(delta / self.temperature)
        return p
        #----------------end my code---------------------------------------
        #raise NotImplementedError()

    def _update_temperature(self):
        # TODO:
        # — update self.temperature according to the exponential decrease function:
        #   `T_k = T * a^k`
        #   where: 
        #       [1] `a` is `self.config.cooling_step`
        #       [2] `k` is stored as `self.cooling_time`` 
        # - update self.cooling_time
        # - make sure, the temperature can't go below `self.config.min_temperature`!
        #----------------my code start---------------------------------------
        self.temperature = self.config.initial_temperature * self.config.cooling_step**self.cooling_time
        self.cooling_time += 1
        if self.temperature < self.config.min_temperature:
            self.temperature = self.config.min_temperature
        #----------------end my code---------------------------------------
        #raise NotImplementedError()

    def escape_local_optimum(self, model: Problem, state: State, best_state: State) -> Union[State, None]:
        ''' This method chooses one of the three possible methods to escale the local minimum'''
        self._local_optimum_escapes += 1
        if self._local_optimum_escapes > self.config.local_optimum_escapes_max >= 0:
            return None

        strategy = random.choices(
            self._escape_strategies, weights=self._escape_probabilities)[0]

        if strategy == SAEscapeStrategy.RandomRestart:
            return self._random_restart(model)
        if strategy == SAEscapeStrategy.Perturbation:
            return self._perturb(model, self.config.escape_perturbation_size)
        if strategy == SAEscapeStrategy.Reheat:
            return self._reheat(state)

    def _reheat(self, from_state: State):
        # TODO:
        # — restore the initial temperature based on config (escape_reheat_ratio * initial_temperature)
        #   [1] initial temperature is stored in `self.config.initial_temperature`
        #   [2] you should decrease it a bit (multiply by `self.config.escape_reheat_ratio`)
        # — reset cooling schedule (`self.cooling_time`)
        # — reset counter looking for local minima (`self.steps_from_last_state_update`)
        # - return the `from_state`
        #----------------my code start---------------------------------------
        self.temperature = self.config.initial_temperature * self.config.escape_reheat_ratio
        self.cooling_time = 0
        self.steps_from_last_state_update = 0
        return from_state
        #----------------end my code---------------------------------------
        #raise NotImplementedError()
