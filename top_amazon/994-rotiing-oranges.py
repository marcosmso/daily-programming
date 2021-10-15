"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        good_oranges = 0 
        to_process = deque()
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good_oranges += 1
                elif grid[i][j] == 2:
                    to_process.append((i,j,0))
                    visited.add((i,j))
        
        min_minutes = 0
        
        while len(to_process) > 0 and good_oranges > 0:   
            cur_i, cur_j, path = to_process.popleft()         
            if grid[cur_i][cur_j] == 1:                          
                grid[cur_i][cur_j] = 2
                good_oranges -= 1
            
            for step_i, step_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_i = cur_i + step_i
                next_j = cur_j + step_j
                
                is_valid_position = (0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]))
        
                if not is_valid_position: continue
                    
                if grid[next_i][next_j] == 0: continue
                
                if (next_i, next_j) in visited: continue
                    
                min_minutes = max(min_minutes, path+1)
                to_process.append((next_i, next_j, path+1))
                visited.add((next_i, next_j))
            
        return min_minutes if good_oranges == 0 else -1

# Without a visited set
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        good_oranges = 0 
        to_process = deque()
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    good_oranges += 1
                elif grid[i][j] == 2:
                    to_process.append((i,j,0))
                    visited.add((i,j))
        
        min_minutes = 0
        
        while len(to_process) > 0 and good_oranges > 0:   
            cur_i, cur_j, path = to_process.popleft()         
            
            for step_i, step_j in [(1,0),(-1,0),(0,1),(0,-1)]:
                next_i = cur_i + step_i
                next_j = cur_j + step_j
                
                is_valid_position = (0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]))
        
                if not is_valid_position: continue
                    
                if grid[next_i][next_j] in [0,2]: continue
                
                good_oranges -= 1
                min_minutes = max(min_minutes, path + 1)
                to_process.append((next_i, next_j, path+1))
                grid[next_i][next_j] = 2
            
        return min_minutes if good_oranges == 0 else -1

# Leetcode
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1

# Usually in BFS algorithms, we keep a visited table which records the visited candidates. 
# The visited table helps us to avoid repetitive visits.

# But as one notices, rather than using the visited table, we reuse the input grid to keep 
# track of our visits, i.e. we were altering the status of the input grid in-place.

# This in-place technique reduces the memory consumption of our algorithm.
# Also, it has a constant time complexity to check the current status (i.e. array access, grid[row][col]), 
# rather than referring to the visited table which might be of constant time complexity as well (e.g. hash table)
# but in reality could be slower than array access.

# We use a delimiter (i.e. (row=-1, col=-1)) in the queue to separate cells on different levels. 
# In this way, we only need one queue for the iteration. As an alternative, one can create a queue 
# for each level and alternate between the queues, though technically the initialization and the 
# assignment of each queue could consume some extra time.