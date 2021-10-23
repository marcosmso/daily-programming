"""
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, 
return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 
Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""
#time: o(n^2)
#space: o(n^2)
import collections
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        sums = collections.defaultdict(int)
        
        for a in nums1:
            for b in nums2:
                sums[a+b] += 1
                
        res = 0
        for c in nums3:
            for d in nums4:
                complement = -(c+d)
                res += sums[complement]
            
        return res

# Approach 2: kSum II
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = {}

        def nSumCount(lists: List[List[int]]) -> int:
            addToHash(lists, 0, 0)
            return countComplements(lists, len(lists) // 2, 0)

        def addToHash(lists: List[List[int]], i: int, sum: int) -> None:
            if i == len(lists) // 2:
                m[sum] = m.get(sum, 0) + 1
            else:
                for a in lists[i]:
                    addToHash(lists, i + 1, sum + a)

        def countComplements(lists: List[List[int]], i: int, complement: int) -> int:
            if i == len(lists):
                return m.get(complement, 0)
            cnt = 0
            for a in lists[i]:
                cnt += countComplements(lists, i + 1, complement - a)
            return cnt

        return nSumCount([A, B, C, D])