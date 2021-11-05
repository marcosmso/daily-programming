"""
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        
        def dfsParent(node, par=None):
            if node:
                parent[node] = par
                dfsParent(node.left, node)
                dfsParent(node.right, node)

        dfsParent(root)
        
        ans = []
        seen = set([target]) 
        queue = collections.deque([(target, 0)])
        
        while len(queue) > 0:
            curr, path = queue.popleft()
            
            if path == k: 
                ans.append(curr.val)
                continue
            
            for nextNode in [curr.left, curr.right, parent[curr]]:
                if nextNode and nextNode not in seen: 
                    queue.append((nextNode, path + 1))
                    seen.add(nextNode)
             
        return ans
            
            