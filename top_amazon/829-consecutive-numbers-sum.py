"""
Given an integer n, return the number of ways you can write n as the sum of consecutive positive integers.

Example 1:
Input: n = 5
Output: 2
Explanation: 5 = 2 + 3

Example 2:
Input: n = 9
Output: 3
Explanation: 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: n = 15
Output: 4
Explanation: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
 
Constraints:

1 <= n <= 109
"""
# N = (x + 1) + ... + (x + k)
# N = x k + k(k + 1)/2
import math
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        # x > 0 --> N/k - (k + 1)/2 > 0
        upper_limit = math.ceil((2 * N + 0.25)**0.5 - 0.5) + 1
        for k in range(1, upper_limit):
            # x should be integer
            if (N - k * (k + 1) // 2) % k == 0:
                count += 1
        return count

        
        