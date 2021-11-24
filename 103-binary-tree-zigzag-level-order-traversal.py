"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return root
        
        zigzag = []
        toProcess = deque()
        reverse = False
        toProcess.append(root)
        
        while len(toProcess) > 0:
            nextToProcess = deque()
            aux = []
            while len(toProcess) > 0:
                if reverse: # pop from bottom, append in begin right an then left
                    curr = toProcess.pop()
                    aux.append(curr.val)
                    if curr.right:
                        nextToProcess.appendleft(curr.right)
                    if curr.left:
                        nextToProcess.appendleft(curr.left)
                else: # pop from front, left -> right 
                    curr = toProcess.popleft()
                    aux.append(curr.val)
                    if curr.left:
                        nextToProcess.append(curr.left)
                    if curr.right:
                        nextToProcess.append(curr.right)
            zigzag.append(aux)
            reverse = not reverse
            toProcess = nextToProcess
        
        return zigzag

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return [] 
        
        zigzag, level = [], [root] 
        f = 1
        
        while level:
            t = [node.val for node in level]
            
            if f == 0:
                t.reverse()
                
            zigzag.append(t)
            f = not f
            
            next_level = [] 
            for node in level: 
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right) 
            level = next_level
            
        return zigzag