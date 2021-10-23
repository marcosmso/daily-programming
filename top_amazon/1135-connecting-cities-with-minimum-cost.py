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
            
            if rootA == rootB: return;
            
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
        