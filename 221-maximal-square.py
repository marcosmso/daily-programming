"""
Given an m x n binary matrix filled with 0's and 1's, find the 
largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxSize = 0 
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    maxSize = 1
        
        if maxSize == 0:
            return 0
        
        if len(matrix) == 1:
            return 1
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = min([matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]]) + 1
                    maxSize = max(maxSize, matrix[i][j])
        
        return maxSize * maxSize