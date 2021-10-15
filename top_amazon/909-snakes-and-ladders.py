"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting 
from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:
	> Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n**2)].
		This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, 
		regardless of the size of the board.
	> If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
	> The game ends when you reach the square n**2.

A board square on row r and column c has a snake or ladder if board[r][c] != -1. 
The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. 
If the destination to a snake or ladder is the start of another snake or ladder, 
you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. 
You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.

Example 1:
Input: board = 
[[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:
Input: board = 
[[-1,-1],
 [-1,3]]
Output: 1
 
Constraints:

n == board.length == board[i].length
2 <= n <= 20
grid[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 do not have any ladders or snakes.
"""
from collections import List
import collections

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        side = len(board)
        
        def square2Idx(square):
            nonlocal side
            row = side -1 - (square-1) // side
            
            if ((square-1)//side) % 2 == 0:
                col = (square-1) % side
            else:
                col = side -1 - (square-1) % side
            return (row, col)
    
        visited = set()
        to_process = collections.deque()
        to_process.append((1, 0))
        
        while len(to_process) > 0:
            square, path = to_process.popleft()
            visited.add(square)
            
            row, col = square2Idx(square)
            
            if board[row][col] != -1:
                square = board[row][col]
                
            if square == side**2:
                return path
            
            max_move = min(square + 6, side ** 2)
            for next_square in range(square + 1, max_move + 1):
                if next_square not in visited:
                    to_process.append((next_square, path + 1))
        
        return -1
