"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct."""

# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         NON_VISITED, PROCESSING, SORTED = 0,1,2 
#         status = numCourses * [NON_VISITED]
#         stack = []
#         is_possible = True
#         adjacencies = {}
        
#         for course, req in prerequisites:
#             if req not in adjacencies:
#                 adjacencies[req] = [course]
#             else:
#                 adjacencies[req].append(course)
        
#         def helper(course):
#             nonlocal is_possible
#             if not is_possible:
#                 return
            
#             status[course] = PROCESSING
            
#             if course in adjacencies:
#                 for nextCourse in adjacencies[course]:
#                     if status[nextCourse] == PROCESSING:
#                         is_possible = False
#                     elif status[nextCourse] == NON_VISITED:
#                         helper(nextCourse)
            
#             status[course] = SORTED
#             stack.append(course)
            
#         for course in range(0, numCourses):
#             if status[course] == NON_VISITED:
#                 helper(course)
            
#         stack.reverse()
#         return stack if is_possible else []

import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree, adjacencies = numCourses * [0], collections.defaultdict(list)
        
        for course, preCourse in prerequisites:
            adjacencies[preCourse].append(course)
            indegree[course] +=1
        
        # indegree: number of prerequisites
        queue = collections.deque([course for course in range(numCourses) if indegree[course] == 0])
        topological_sort = []
        
        while len(queue) > 0:
            preCourse = queue.popleft()
            topological_sort.append(preCourse)
            
            if preCourse in adjacencies:
                for nextCourse in adjacencies[preCourse]:
                    indegree[nextCourse]-=1
                    if indegree[nextCourse] == 0:
                        queue.append(nextCourse)
                    
        return topological_sort if len(topological_sort) == numCourses else []        
     
        
        