"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] 
indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:

0-1-2 3-4

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:

0-1
  |
  2-3-4

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
"""
# Approach 1: Depth-First Search (DFS)
# time: O(E+V)
# space: O(E+V)
# Approach 1: Depth-First Search (DFS)

#Algorithm
#1. Create an adjacency list such that adj[v] contains all the adjacent vertices of vertex v.
#2. Initialize a hashmap or array, visited, to track the visited vertices.
#3. Define a counter variable and initialize it to zero.
#4. Iterate over each vertex in edges, and if the vertex is not already in visited, start a DFS from it. Add every vertex visited during the DFS to visited.
#5. Every time a new DFS starts, increment the counter variable by one.
#6. At the end, the counter variable will contain the number of connected components in the undirected graph.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {}
        
        for i in range(n):
            adjList[i] = set()
        
        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])
            
        components, visited = 0, set()

        def dfs(curr):
            visited.add(curr)
            for nextNode in adjList[curr]:
                if nextNode in visited:
                    continue
                dfs(nextNode)

        for node in adjList:
            if node in visited:
                continue
            dfs(node)
            components +=1

        return components

#Approach 2: Disjoint Set Union (DSU) 

#Algorithm

#1.Initialize a variable count with the number of vertices in the input.
#2.Traverse all of the edges one by one, performing the union-find method combine on each edge. 
#  If the endpoints are already in the same set, then keep traversing. If they are not, then decrement count by 1.
#3.After traversing all of the edges, the variable count will contain the number of components in the graph.
class Solution:
	def countComponents(self, n, edges):
		par = [i for i in range(n)]
		rank = [1] * n

		# find root parent of node
		def find(n1):
			res = n1
			# stop when node is its own parent, because it is a root parent
			while res != par[res]:
				par[res] = par[par[res]]
				res = par[res]

		def union(n1, n2):
			p1, p2 = find(n1), find(n2)

			if p1 == p2:
				return 0

			if rank[p2] > rank[p1]:
				par[p1] = p2
				rank[p2] += rank[p1]
			else:
				par[p2] = p1
				rank[p1] += rank[p2]
			return 1

		res = n
		for n1, n2 in edges:
			res -= union(n1,n2)
		
		return res
