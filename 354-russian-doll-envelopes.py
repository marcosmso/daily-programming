"""
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height
of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the 
other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
 
Constraints:

1 <= envelopes.length <= 5000
envelopes[i].length == 2
1 <= wi, hi <= 104
"""
from bisect import bisect_left 
class Solution(object):
#     def maxEnvelopes(self, envelopes):
#         n = len(envelopes)
#         envelopes.sort(key = lambda e: (e[0],e[1]))
        
#         dp = n * [1]
         
#         for i in range(1, n):
#             for j in range(i):
#                 if not envelopes[j][0] < envelopes[i][0] or not envelopes[j][1] < envelopes[i][1]:
#                     continue
#                 dp[i] = max(dp[i], dp[j] + 1)
                
#         return max(dp)
    
    def maxEnvelopes(self, envelopes):
        n = len(envelopes)
        envelopes.sort(key = lambda e: (e[0],-e[1]))
        
        dp = []
         
        for w, h in envelopes:
            i = bisect_left(dp, h)
            
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        
        return len(dp)
    

        