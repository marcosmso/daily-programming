"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, 
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
"""
#time: O(k * log(k))
#space: O(k)
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        rows, cols = len(matrix), len(matrix[0])
        min_heap = [(matrix[0][0], 0, 0)]
        
        for _ in range(k-1):
            curr, i, j = heapq.heappop(min_heap)
            
            if i < rows and j+1 < cols and matrix[1][j+1]!= None:
                heapq.heappush(min_heap, (matrix[i][j+1], i, j+1))
                matrix[i][j+1] = None
            if i+1 < rows and j < cols and matrix[i+1][j]!= None:
                heapq.heappush(min_heap, (matrix[i+1][j], i+1, j))
                matrix[i+1][j] = None
        
        return min_heap[0][0]
            
            
        
        