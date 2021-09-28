class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __lt__(self, other):
        return self.val < other.val

def printModule():
	print("Linked List Module imported")

def createLinkedList(arr):
	if len(arr) == 0: return None
	
	curr = None
	for i in range(len(arr)-1, -1, -1):
		newNode = ListNode(arr[i], curr)
		curr = newNode

	return curr

def isEqual(linkedList1, linkedList2):
	runner1, runner2 = linkedList1, linkedList2

	while runner1 and runner2:
		if runner1.val != runner2.val:
			return False
		runner1, runner2 = runner1.next, runner2.next
	
	return not runner1 and not runner2 

def stringify(linkedList):
	if not linkedList:
		return "Empty LinkedList" 
	
	nodes = []
	runner = linkedList

	while runner:
		nodes.append(str(runner.val))
		runner = runner.next

	return "->".join(nodes)
	

# LinkedList.printModule()

# arr1 = [1,2,3,4,5,6,7,8,9,10]

# arr2 = [1,2,3,4,5,6,7,8,9,10]
# lList1 = LinkedList.createLinkedList(arr1)
# lList2 = LinkedList.createLinkedList(arr2)

# print("OK")
# print(LinkedList.isEqual(lList1, lList2))
# print(LinkedList.stringify(lList1))

