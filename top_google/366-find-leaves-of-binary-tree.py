"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.

Example 2:
Input: root = [1]
Output: [[1]]
 

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        
        def recursiveFindLeaves(node):
            if not node: return 0
            
            left_layer  = recursiveFindLeaves(node.left)
            right_layer = recursiveFindLeaves(node.right)
            
            my_layer = 1 + max(left_layer, right_layer)
            
            if len(self.ans) < my_layer:
                self.ans.append([])
            self.ans[my_layer - 1].append(node.val)
            
            return my_layer
        
        if root:
            recursiveFindLeaves(root)
    
        return self.ans