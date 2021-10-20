#!/bin/python3

import math
import os
import random
import re
import sys

def isBalanced(s):
    matches = {'}':'{', ')':'(', ']':'['}
    stack = []
    
    for char in s:
        if char in ['[', '{', '(']:
            stack.append(char)
        else:
            if len(stack) == 0 or stack[-1] != matches[char]:
                return 'NO'
            else:
                stack.pop()  
    
    return 'YES' if len(stack) == 0 else 'NO'
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
