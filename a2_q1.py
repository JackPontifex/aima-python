# Question 1 code
import random

def decision(probability):
  return random.random() < probability

def rand_graph(n, p):
  randomGraph = {}
  for i in range(0, n):
    randomGraph[i] = []

  for i in range(0, n):
    for j in range(i + 1, n):
      if decision(p):
        randomGraph[i].append(j)
        randomGraph[j].append(i)

  return randomGraph