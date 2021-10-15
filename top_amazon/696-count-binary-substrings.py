"""
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, 
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
"""

# class Solution:
# 	def countBinarySubstrings(self, s):
# 		groups = []
# 		curr, i = 1, 0
# 		while i < len(s)-1: 
# 			if s[i] == s[i+1]:
# 				curr += 1
# 			else:
# 				groups.append(curr)
# 				curr=1
# 			i += 1
# 		groups.append(curr)
		
# 		num_substrings = 0
# 		for i in range(len(groups)-1):
# 			num_substrings += min(groups[i], groups[i+1])
		
# 		return num_substrings

# class Solution(object):
#     def countBinarySubstrings(self, s):
#         groups = [1]
#         for i in xrange(1, len(s)):
#             if s[i-1] != s[i]:
#                 groups.append(1)
#             else:
#                 groups[-1] += 1

#         ans = 0
#         for i in xrange(1, len(groups)):
#             ans += min(groups[i-1], groups[i])
#         return ans

class Solution(object):
    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)