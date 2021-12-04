"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 
Constraints:

1 <= n <= 1690
"""
#time O(N log N)
#space O(N)
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        if n == 1: return 1
        
        minHeap = [1]
        seen = set([1])
        
        i = 1
        while i < n:
            smallest = heapq.heappop(minHeap)
            for k in [2,3,5]:
                prod = smallest * k
                if prod not in seen:
                    seen.add(prod)
                    heapq.heappush(minHeap, prod)
            i += 1
                    
        return minHeap[0]