import random
from typing import Generator, Set, Dict, List

from local_search.problems.base.moves import Move
from local_search.problems.graph_coloring_problem.models.vertex import Vertex
from local_search.problems.graph_coloring_problem.moves.move_generator import GraphColoringMoveGenerator
from local_search.problems.graph_coloring_problem.state import GraphColoringState
import copy


class KempeChainMove(Move[GraphColoringState]):
    def __init__(self, graph: Dict[int, Set[int]], from_state: GraphColoringState, idx: int, color: int):
        super().__init__(from_state)
        self.idx = idx
        self.color = color
        self.graph = graph
        self.old_color = self.state.coloring[idx].color

    def _kempe_chain(self, coloring: List[Vertex]):
        # TODO: do the kempe chain thing
        # - self.idx is index of the node beginning the chain
        # - self.color is the new color of the node (already set in the `make` method)
        # - self.old_color is the old color of the node 
        # - self.graph[c] are the neighbors of the node c
        # - coloring is the list of vertices (every vertex has index and color)
        #   your task is to modify this coloring in place
        #
        # The color of the node with index self.idx has changed!
        # Now you have to fix all the possible conflicts in a BFS fashion
        # by changing colors of nodes (via `coloring`): 
        # - with self.color to self.old_color 
        # - with self.old_color to self.color
        pass

    def make(self) -> GraphColoringState:
        new_coloring = copy.deepcopy(self.state.coloring)
        new_coloring[self.idx].color = self.color
        self._kempe_chain(new_coloring)
        return GraphColoringState(coloring=new_coloring)


class KempeChain(GraphColoringMoveGenerator):

    def random_moves(self, state: GraphColoringState) -> Generator[KempeChainMove, None, None]:
        while True:
            idx = random.randrange(self.n_vertices)
            available_colors = self.get_available_colors(idx, state)
            yield KempeChainMove(self.graph,
                                 state,
                                 idx=random.randrange(self.n_vertices),
                                 color=random.choice(available_colors))

    def available_moves(self, state: GraphColoringState) -> Generator[KempeChainMove, None, None]:
        for idx in range(self.n_vertices):
            for color in self.get_available_colors(idx, state):
                if state.coloring[idx].color == color:
                    continue
                yield KempeChainMove(self.graph, state, idx, color)
