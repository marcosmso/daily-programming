"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the
island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix 
heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly 
north, south, east, and west if the neighboring cell's height is less than or equal to the 
current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water 
can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 
Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""
from collections import deque()
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])
        aVisited, pVisited = set(), set()
        aQueue, pQueue = deque(), deque()
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pVisited.add((i,j))
                    pQueue.append((i,j))
                    
                if i == m-1 or j == n-1:
                    aVisited.add((i,j))
                    aQueue.append((i,j))

        
        directions = [(-1,0), (0,-1), (0,1), (1,0)]
        
        def searchReachable(Queue, Visited):
            while Queue:
                x, y = Queue.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy 

                    if not (0 <= nx < m) or not (0 <= ny < n) or (nx,ny) in Visited:
                        continue

                    if heights[nx][ny] >= heights[x][y]:
                        Visited.add((nx,ny))
                        Queue.append((nx,ny))
        
        searchReachable(aQueue, aVisited)
        searchReachable(pQueue, pVisited)
        
        return list(aVisited & pVisited)

