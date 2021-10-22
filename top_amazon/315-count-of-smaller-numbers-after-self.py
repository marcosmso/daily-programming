"""
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements 
to the right of nums[i].

Example 1:
Input: nums = [5,2,6,1]
Output: [2,1,1,0]

Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2:
Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        def mergeSort(l, r, arr, nums):
            if l < r:
                m = (l+r) //2
                mergeSort(l, m, arr, nums)
                mergeSort(m+1, r, arr, nums)
                
                n1, n2 = m - l + 1, r - m
                L = [arr[l+i] for i in range(n1)] 
                R = [arr[m+1+i] for i in range(n2)]
                
                i, j, k = 0, 0, l
                passes = 0
                while i < n1 and j < n2:
                    lNum, rNum = nums[L[i][0]], nums[R[j][0]]
                    if lNum <= rNum:
                        arr[k] = (L[i][0], L[i][1] + passes) 
                        i += 1
                    else:
                        passes += 1
                        arr[k] = R[j]
                        j += 1
                    k += 1
                    
                while i < n1:
                    arr[k] = (L[i][0], L[i][1] + passes)
                    i+=1
                    k+=1
                
                while j < n2:
                    arr[k] = R[j]
                    j+=1
                    k+=1
        
        n = len(nums)
        indexes = [(i, 0) for i in range(n)]
        mergeSort(0, n - 1, indexes, nums)
        
        res = n * [0]
        for idx, qtt in indexes:
            res[idx] = qtt
        
        return res
            