"""
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
"""
import collections

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        
        frequencies = collections.defaultdict(int)
        max_freq = float("-inf")
        
        for n, f in counter.items():
            frequencies[f] += 1
            max_freq = max(max_freq, f)
            
        for i in range(1, max_freq + 1):
            if k == 0: break
            
            if k >= frequencies[i]*i:
                k -= frequencies[i]*i
                frequencies[i] = 0
            else:
                q, r = divmod(k, i)
                frequencies[i] -= q
                
                if r > 0:
                    frequencies[i] -= 1
                    frequencies[i-r] += 1
                k = 0
              
        integers = 0
        for value in frequencies.values():
            integers += value
        return integers

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = collections.Counter(arr)
        
        l = list(freq.items())
        l.sort(key = lambda e: e[1])
        
        unique = len(l)
        for t in l:
            if k == 0:
                break
            if k >= t[1]:
                k = k - t[1]
                unique -= 1
        
        return unique
            
