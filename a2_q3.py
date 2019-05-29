# Question 3 code

from a2_q1 import rand_graph
from a2_q2 import check_teams
from csp import *



graphs = [rand_graph(30, 0.1), rand_graph(30, 0.2), rand_graph(30, 0.3),
          rand_graph(30, 0.4), rand_graph(30, 0.5)]

mapColoring = MapColoringCSP(range(30), graphs[0])

solution = backtracking_search(mapColoring)

print(graphs[0])
print(solution)
print(check_teams(graphs[0], solution))