"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

class Solution:
    def merge(self, intervals):
        if not intervals and len(intervals) == 0:
            return None
        
        intervals.sort(key = lambda interval: interval[0])
        
        minVal, maxVal = intervals[0]
        ans = []
        for interval in intervals:
            if minVal <= interval[0] and interval[0] <= maxVal:
                maxVal = max(maxVal, interval[1])
            elif interval[0] > maxVal:
                ans.append([minVal, maxVal])
                minVal, maxVal = interval[0], interval[1] 
                
        ans.append([minVal, maxVal]) 
        
        return ans