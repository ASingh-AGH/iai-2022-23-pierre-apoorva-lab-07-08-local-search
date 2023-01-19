from abc import ABC
from typing import List

from local_search.helpers.camel_to_snake import camel_to_snake
from local_search.problems.base.problem import Goal
from local_search.problems.graph_coloring_problem.models.edge import Edge
from local_search.problems.graph_coloring_problem.state import GraphColoringState


class GraphColoringGoal(Goal, ABC):
    """
    Base class for goals of the graph coloring problem
    """
    goals = {}

    def __init__(self, edges: List[Edge], n_vertices: int):
        self.edges = edges
        self.n_vertices = n_vertices

    def __init_subclass__(cls):
        GraphColoringGoal.goals[camel_to_snake(cls.__name__)] = cls

    def _num_colors(self, state: GraphColoringState) -> int:
        # return number of distinct colors used in `state.coloring` 

        all_col = []
        for i in state.coloring:
            all_col.append(i.color)

        return len(set(all_col))

        raise NotImplementedError()

    def _bad_edges(self, state: GraphColoringState) -> List[int]:
        # TODO:
        # return number of bad edges of every color class in the graph
        # tip 1. `self.edges` is the list of 'Edge' in the graph
        # tip 2. example usage: `state.coloring[edge.start].color` 
        #        is color of the edge start in the current state
#-----------my code start----------------------------------------------
        bad_edges = [0] * self.n_vertices
        for edge in self.edges:
            if state.coloring[edge.start].color == state.coloring[edge.end].color:
                bad_edges[state.coloring[edge.start].color] += 1
        return bad_edges
#----------end my code-------------------------------------------------

        raise NotImplementedError()

    def _color_classes(self, state: GraphColoringState) -> List[int]:
        # TODO:
        # return sizes of the color classes
        # - assume the worst case — there is as many colors as there are vertices
        #   so the result should be a list of size `self.n_vertices`
        # - the result is a list with values corresponding to sizes of the color classes, e.g.
        #   `result[0] = 5` means that there five nodes in `state` with `color = 0`
#------------my code start---------------------------------------------
        color_classes = [0] * self.n_vertices
        for node in state.coloring:
            color_classes[node.color] += 1
        return color_classes
#------------end my code-------------------------------------------------
        raise NotImplementedError()

    def human_readable_objective_for(self, state: GraphColoringState) -> str:
        return f"{self._num_colors(state)} colors"
