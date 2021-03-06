
# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    if not root.left and not root.right:
        return 0
    
    h_left, h_right = 0, 0 
    if root.left:
        h_left = height(root.left)
    if root.right:
        h_right = height(root.right)
        
    return 1 + max(h_left, h_right)