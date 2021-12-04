"""
Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1
 
Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        
        minDiff = float("inf")
        prev = None
        
        stack = []
        curr = root
        while curr or len(stack) > 0:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            if prev != None:
                minDiff = min(minDiff, curr.val - prev)
            prev = curr.val
            
            curr = curr.right
        
        return minDiff
            