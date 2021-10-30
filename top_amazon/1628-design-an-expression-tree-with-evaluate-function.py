"""
Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression.

Postfix notation is a notation for writing arithmetic expressions in which the operands (numbers) appear before their operators. 
For example, the postfix tokens of the expression 4*(5-(7+2)) are represented in the array postfix = ["4","5","7","2","+","-","*"].

The class Node is an interface you should use to implement the binary expression tree. The returned tree will be tested using the 
evaluate function, which is supposed to evaluate the tree's value. You should not remove the Node class; however, you can modify 
it as you wish, and you can define other classes to implement it if needed.

A binary expression tree is a kind of binary tree used to represent arithmetic expressions. Each node of a binary expression tree 
has either zero or two children. Leaf nodes (nodes with 0 children) correspond to operands (numbers), and internal nodes 
(nodes with two children) correspond to the operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/' (division).

It's guaranteed that no subtree will yield a value that exceeds 109 in absolute value, and all the operations are valid (i.e., no division by zero).

Follow up: Could you design the expression tree such that it is more modular? For example, is your design able to support additional 
operators without making changes to your existing evaluate implementation?

Example 1:
Input: s = ["3","4","+","2","*","7","/"]
Output: 2
Explanation: this expression evaluates to the above binary tree with expression ((3+4)*2)/7) = 14/7 = 2.

Example 2:
Input: s = ["4","5","2","7","+","-","*"]
Output: -16
Explanation: this expression evaluates to the above binary tree with expression 4*(5-(2+7)) = 4*(-4) = -16.

Example 3:
Input: s = ["4","2","+","3","5","1","-","*","+"]
Output: 18

Example 4:
Input: s = ["100","200","+","2","/","5","*","7","+"]
Output: 757
 
Constraints:
1 <= s.length < 100
s.length is odd.
s consists of numbers and the characters '+', '-', '*', and '/'.
If s[i] is a number, its integer representation is no more than 105.
It is guaranteed that s is a valid expression.
The absolute value of the result and intermediate values will not exceed 109.
It is guaranteed that no expression will include division by zero.
"""
import abc 
from abc import ABC, abstractmethod 

class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass
    
class NumberNode(Node):
    def __init__(self, data):
        self.data = int(data)
        self.left = None
        self.right = None
        
    def evaluate(self):
        return self.data
    
class OperationNode(Node):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
    def evaluate(self):
        if self.data == '+':
            return self.left.evaluate() + self.right.evaluate() 
        elif self.data == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.data == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.data == '/':
            return int(self.left.evaluate() / self.right.evaluate())
    
    
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        self.curr = len(postfix) - 1
        
        def recursiveBuild():
            if self.curr < 0:
                return
            
            data = postfix[self.curr]
            self.curr -= 1
            if data not in ["+","/","-","*"]:
                return NumberNode(data)
            
            right = recursiveBuild()
            left = recursiveBuild()
            
            return OperationNode(data, left, right)
        
        return recursiveBuild()
            
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass
    
class NumericNode(Node):
    # Must be a leaf node
    def __init__(self, num):
        self.num = num
        
    def evaluate(self):
        return int(self.num)

    
class OperatorNode(Node):
    # Must have 2 children
    def __init__(self):
        self.left = None
        self.right = None
    
    @abstractmethod
    def evaluate(self):
        pass
        
        
class MultiplactionNode(OperatorNode):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

    
class AdditionNode(OperatorNode):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

    
class SubtractionNode(OperatorNode):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

    
class DivisionNode(OperatorNode):
    def __init__(self):
        super().__init__()
    
    def evaluate(self):
        return self.left.evaluate() // self.right.evaluate()
    
    
class NodeFactory:
    @staticmethod
    def new_node(element) -> Node:
        if isinstance(element, Node):
            return element
        
        elif element.isdigit():
            return NumericNode(element)
        
        else:
            if element  == "+":
                return AdditionNode()
            
            elif element == "-":
                return SubtractionNode()
                
            elif element == "*":
                return MultiplactionNode()
                
            else:
                return DivisionNode()

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        
        for value in postfix:
            if not value.isdigit():
                node = NodeFactory.new_node(value)
                node.right = NodeFactory.new_node(stack.pop())
                node.left = NodeFactory.new_node(stack.pop())
                
                stack.append(node)
            else:
                stack.append(value)
                
        return stack.pop()
            
            
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
