#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

# 1) Create an empty stack S.
# 2) Initialize current node as root
# 3) Push the current node to S and set current = current->left until current is NULL
# 4) If current is NULL and stack is not empty then 
#      a) Pop the top item from stack.
#      b) Print the popped item, set current = popped_item->right 
#      c) Go to step 3.
# 5) If current is NULL and stack is empty then we are done.

def inorder(indexes):
    stack = []
    curr = 1
    res = []
    
    while len(stack) > 0 or curr != -1:
        if curr != -1:
            stack.append(curr)
            curr = indexes[curr-1][0] #left child
        else:
            curr = stack.pop()
            res.append(curr)
            curr = indexes[curr-1][1] #right child
    
    return res 
            
def swapNodes(indexes, queries):
    import collections
    
    depths = {1:1}
    max_depth = float("-inf")
    
    for i in range(len(indexes)):
        node1, node2 = indexes[i]
        if node1 != -1:
            depths[node1] = depths[i+1] + 1
        if node2 != -1:
            depths[node2] = depths[i+1] + 1
        max_depth = max(max_depth, depths[i+1] + 1)
        
    nodes_by_depth = collections.defaultdict(list)
    for node, depth in depths.items():
        nodes_by_depth[depth].append(node)

    res = []
    
    for k in queries:
        factor = 1
        while factor * k <= max_depth:
            for node in nodes_by_depth[factor * k]:
                indexes[node-1][0], indexes[node-1][1] = indexes[node-1][1], indexes[node-1][0] 
            factor += 1
        res.append(inorder(indexes))

    return res
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()