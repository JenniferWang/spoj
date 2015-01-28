#implement Dijsktra
import collections

class Node:
  def __init__(self, val):
    self.val = val

class Graph:
  def __init__(self, num_node):
    self.n = num_node
    self.edgList = collections.defaultdict(dict)

  def add_edge(self, node1, node2, weight):
    self.edgList[node1][node2] = weight
    self.edgList[node2][node1] = weight

  def _getMinCostNode(self, costs):
    return min(costs, key = costs.get)

  def dijsktra(self, start):
    visited = set()
    shortest_path = {start:[]}
    shortest_costs = {start: 0}
    costs = {node: float("inf") for node in self.edgList}
    costs[start] = 0

    while len(visited) < self.n:
      curr = self._getMinCostNode(costs)
      curr_cost = costs[curr]
      shortest_costs[curr] = curr_cost
      del costs[curr]
      visited.add(curr)   
      
      for neighbor in self.edgList[curr]:
        if neighbor not in visited:
          cost_thru_node = self.edgList[curr][neighbor] + curr_cost
          if cost_thru_node < costs[neighbor]:
            costs[neighbor] = cost_thru_node
            shortest_path[neighbor] = shortest_path[curr] + [curr.val]
    
    for key in sorted(shortest_costs):
      print key.val, ': ', shortest_costs[key]
    return shortest_path

g = Graph(9)
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
g.add_edge(node0, node1, 4)
g.add_edge(node0, node7, 8)
g.add_edge(node1, node7, 11)
g.add_edge(node1, node2, 8)
g.add_edge(node7, node8, 7)
g.add_edge(node7, node6, 1)
g.add_edge(node8, node6, 6)
g.add_edge(node2, node8, 2)
g.add_edge(node2, node3, 7)
g.add_edge(node2, node5, 4)
g.add_edge(node6, node5, 2)
g.add_edge(node3, node5, 14)
g.add_edge(node3, node4, 9)
g.add_edge(node5, node4, 10)

g.dijsktra(node0)