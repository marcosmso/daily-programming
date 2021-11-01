"""
There are n cities labeled from 1 to n. You are given the integer n and an array connections 
where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city 
yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path 
between each pair of cities. If it is impossible to connect all the n cities, return -1,

The cost is the sum of the connections' costs used.

Example 1:
Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: Choosing any 2 edges will connect all cities so we choose the minimum 2.

Example 2:
Input: n = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: There is no way to connect all cities even if all edges are used.

Constraints:

1 <= n <= 104
1 <= connections.length <= 104
connections[i].length == 3
1 <= xi, yi <= n
xi != yi
0 <= costi <= 105
"""
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        parents = [i for i in range(0, n+1)]
        weights = (n+1) * [1]
        
        def find(a):
            while (a != parents[a]):
                parents[a] = parents[parents[a]]
                a = parents[a]
            return a
        
        def makeUnion(a, b):
            rootA = find(a)
            rootB = find(b)
            
            if rootA == rootB: return
            
            if weights[rootA] > weights[rootB]:
                parents[rootB] = rootA
                weights[rootA] += 1
            else:
                parents[rootA] = rootB
                weights[rootB] += 1     
        
        connections.sort(key = lambda t: t[2])
        total_cost, edges = 0, 0
        
        for v1, v2, cost in connections:
            # verify if nodes in same group
            if find(v1) == find(v2): continue 
            
            makeUnion(v1,v2)
            total_cost += cost
            edges += 1
            
        if edges == n - 1:
            return total_cost
        return -1
        


# # A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# # The program is for adjacency matrix representation of the graph
 
# import sys # Library for INT_MAX
 
class Solution:
  def primsAlgorithm(self, n, connections):
    



# class Graph():
 
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)]
#                     for row in range(vertices)]
 
#     # A utility function to find the vertex with
#     # minimum distance value, from the set of vertices
#     # not yet included in shortest path tree
#     def minKey(self, key, mstSet):
#         min = sys.maxint
#         for v in range(self.V):
#             if key[v] < min and mstSet[v] == False:
#                 min = key[v]
#                 min_index = v
 
#         return min_index
 
#     def primMST(self):

#         key = [sys.maxint] * self.V
#         parent = [None] * self.V 
#         key[0] = 0
#         mstSet = [False] * self.V
#         parent[0] = -1 
 
#         for cout in range(self.V):
 
#             # Pick the minimum distance vertex from
#             # the set of vertices not yet processed.
#             # u is always equal to src in first iteration
#             u = self.minKey(key, mstSet)
 
#             # Put the minimum distance vertex in
#             # the shortest path tree
#             mstSet[u] = True
 
#             # Update dist value of the adjacent vertices
#             # of the picked vertex only if the current
#             # distance is greater than new distance and
#             # the vertex in not in the shortest path tree
#             for v in range(self.V):
 
#                 # graph[u][v] is non zero only for adjacent vertices of m
#                 # mstSet[v] is false for vertices not yet included in MST
#                 # Update the key only if graph[u][v] is smaller than key[v]
#                 if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
#                         key[v] = self.graph[u][v]
#                         parent[v] = u
 
#         self.printMST(parent)
 
# g = Graph(5)
# g.graph = [ [0, 2, 0, 6, 0],
#             [2, 0, 3, 8, 5],
#             [0, 3, 0, 0, 7],
#             [6, 8, 0, 0, 9],
#             [0, 5, 7, 9, 0]]
 
# g.primMST();
 
# # Contributed by Divyanshu Mehta