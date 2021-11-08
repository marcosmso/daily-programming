"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections 
forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. 
Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
Return all critical connections in the network in any order.

Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:
Input: n = 2, connections = [[0,1]]
Output: [[0,1]]
 
Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""
import collections
class Solution:
    
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        adjList = collections.defaultdict(list)
        for node1, node2 in connections:
            adjList[node1].append(node2)
            adjList[node2].append(node1)
        
        time = 0
        parent, low, disc = [-1] * n, [-1] * n, [-1] * n
        bridges = []
        
        def DFS(node):
            nonlocal time
            disc[node] = low[node] = time
            time += 1
            
            for nextNode in adjList[node]:
                if disc[nextNode] == -1:
                    parent[nextNode] = node
                    DFS(nextNode)
                    low[node] = min(low[node], low[nextNode])

                    if low[nextNode] > disc[node]:
                        bridges.append([node, nextNode])
                elif nextNode != parent[node]:
                    low[node] = min(low[node], disc[nextNode])
                
        
        for i in range(n):
            if disc[i] == -1: #not visited
                DFS(i)
        
        return bridges
                
        
        