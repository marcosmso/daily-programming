"""
You are starving and you want to eat food as quickly as possible. 
You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

Example 1:
Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.

Example 2:
Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.

Example 3:
Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.
Example 4:

Input: grid = [["O","*"],["#","O"]]
Output: 2
Example 5:

Input: grid = [["X","*"],["#","X"]]
Output: -1
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[row][col] is '*', 'X', 'O', or '#'.
The grid contains exactly one '*'.
"""
import collections

class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        i_0, j_0 = 0, 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '*':
                    i_0, j_0 = i, j
                    break
        
        grid[i_0][j_0] = 0 
        shortest_path = float("inf")
        to_process = collections.deque()
        to_process.append((i_0,j_0))
        
        while len(to_process) > 0:
            i, j = to_process.popleft()
            
            for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
                if not (0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0])):
                    continue
                
                content = grid[i+di][j+dj]
                if content == "X": 
                    continue
                elif content == '#':
                    grid[i+di][j+dj] = grid[i][j] + 1
                    to_process.append((i+di,j+dj))
                    shortest_path = min(shortest_path, grid[i+di][j+dj])
                elif content == "O":
                    grid[i+di][j+dj] = grid[i][j] + 1
                    to_process.append((i+di,j+dj))
        
        return shortest_path if shortest_path < float("inf") else -1