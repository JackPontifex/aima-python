# Question 2 code

def check_teams(graph, csp_sol):
  for i in range(len(graph)):
    group = csp_sol[i]
    for j in graph[i]:
      if csp_sol[j] == group:
        return False
  return True