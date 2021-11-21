"""
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]

Example 2:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]

Example 3:
Input: l1 = [0], l2 = [0]
Output: [0]
 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?
"""
# time: O(n1+n2) space: O(n1+n2)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1, runner = [], l1
        while runner:
            num1.append(runner)
            runner = runner.next
            
        num2, runner = [], l2
        while runner:
            num2.append(runner)
            runner = runner.next
            
        if len(num2) > len(num1):
            num1, num2 = num2, num1
            l1, l2 = l2, l1
            
        carry = 0
        while len(num2) > 0:
            node1, node2 = num1.pop(), num2.pop()
            value = node1.val + node2.val + carry
            carry, digit = value//10, value % 10
            node1.val = digit
        
        while len(num1) > 0:
            node1 = num1.pop()
            value = node1.val + carry
            carry, digit = value//10, value % 10
            node1.val = digit
        
        if carry > 0:
            return ListNode(1, l1)   
        return l1
    