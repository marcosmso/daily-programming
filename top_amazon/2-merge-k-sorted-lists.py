""" 
Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it. 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

"""
import unittest
import heapq
from LinkedList import createLinkedList, isEqual, ListNode

class Solution:
    def mergeKLists(self, lists):
        heap = []
        
        for alist in lists:
            if alist:
                heapq.heappush(heap, alist)

        merged = last = ListNode()
        
        while len(heap) > 0:
            curr = heapq.heappop(heap)
            currNext = curr.next
            if currNext:
                heapq.heappush(heap, currNext)
            curr.next = None
            last.next = curr
            last = curr
        
        return merged.next

class Tests(unittest.TestCase):
	def test_1(self):
		lists = [createLinkedList([1,4,5]), createLinkedList([1,3,4]), createLinkedList([2,6]), createLinkedList([])]
		self.assertTrue(isEqual(Solution().mergeKLists(lists), createLinkedList([1,1,2,3,4,4,5,6])))
	
	def test_2(self):
		lists = []
		self.assertEqual(Solution().mergeKLists(lists), None)
	
	def test_3(self):
		lists = [[]]
		self.assertEqual(Solution().mergeKLists(lists), None)

if __name__ == '__main__':
	unittest.main()