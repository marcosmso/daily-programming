"""
Implement the RandomizedSet class:
> RandomizedSet() Initializes the RandomizedSet object.
> bool insert(int val) Inserts an item val into the set if not present. 
Returns true if the item was not present, false otherwise.
> bool remove(int val) Removes an item val from the set if present. 
Returns true if the item was present, false otherwise.
> int getRandom() Returns a random element from the current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""
# Whats should getRandom return when len(RandomizedSet)=0
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        
    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            lastElement, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[lastElement] = lastElement, idx
            self.list.pop()
            del self.dict[val]
            return True
        return False
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)
