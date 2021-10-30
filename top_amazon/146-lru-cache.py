"""
146. LRU Cache

Share
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 
Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""
# from collections import OrderedDict
# dic = OrderedDict()

# dic[1], dic[2], dic[3], dic[4] = 1, 2, 3 , 4
# print(dic) #OrderedDict([(1, 1), (2, 2), (3, 3), (4, 4)])
# print(dic.popitem())           #(4, 4)
# print(dic.popitem(last=False)) #(1,1)

# dic[1], dic[2], dic[3], dic[4] = 1, 2, 3 , 4
# print(dic) # OrderedDict([(2, 2), (3, 3), (1, 1), (4, 4)])

# dic.move_to_end(2)
# print(dic) #OrderedDict([(3, 3), (1, 1), (4, 4), (2, 2)])
# dic.move_to_end(4,last=False)
# print(dic) #OrderedDict([(4, 4), (3, 3), (1, 1), (2, 2)])
# next(reversed(dic)) # reversed return a iterator in O(1) 

import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache: 
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = value
        self.cache.move_to_end(key)

class Node:
    def __init__(self, key="#", data='#', left=None, right=None):
        self.key = key
        self.data = data
        self.right = right
        self.left = left      
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = Node(), Node()
        self.head.right = self.tail
        self.tail.left = self.head
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.enqueueNode(node)
            return node.data
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.data = value
            self.removeNode(node)
            self.enqueueNode(node)
        else:
            if len(self.cache) == self.capacity:
                lastNode = self.tail.left
                self.removeNode(lastNode)
                del self.cache[lastNode.key]

            newNode = Node(key, value, None, None)
            self.cache[key] = newNode
            self.enqueueNode(newNode)
        
    def removeNode(self, node):
        if node:
            node.right.left = node.left
            node.left.right = node.right
            node.left = None
            node.right = None
    
    def enqueueNode(self, node):
        if node:
            node.right = self.head.right
            node.right.left = node
            node.left = self.head
            self.head.right = node