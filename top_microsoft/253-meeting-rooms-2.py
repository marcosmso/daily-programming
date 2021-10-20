"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
 
Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        START, END = 2, 1
        timePoints = [] 
        for interval in intervals: 
            timePoints.append((interval[0], START))
            timePoints.append((interval[1], END))
            
        timePoints.sort(key = lambda t: (t[0], t[1]))
        
        currRooms, neededRooms = 0, 0
        for timePoint in timePoints:
            if timePoint[1] == START:
                currRooms +=1
                neededRooms = max(neededRooms, currRooms)
            else:
                currRooms -=1
        
        return neededRooms