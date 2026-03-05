 
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:

	def _getNumber(self, l):
		node = l
		num = 0
		digit_place = 0

		while not(node is None):
			num += 10**digit_place * node.val 
			digit_place += 1
			node = node.next
		return num

	def _numToListNode(self, num):

		if num == 0:
			return ListNode(num)

		parent = None
		head = None
		
		while num != 0:
			digit = num % 10
			num = num // 10
			node = ListNode(digit)

			if not(parent is None):
				parent.next = node
				parent = parent.next
			else:
				head = node
				parent = head

		return head

	def addTwoNumbers(self, l1, l2):
		l1_num = self._getNumber(l1)
		l2_num = self._getNumber(l2)
		return self._numToListNode(l1_num+l2_num)


def test():

	list1 = ListNode(3,4,5)

	list2 = ListNode(1,1,1)

	node = Solution().addTwoNumbers(list1,list2)
	num = 0
	digit_place = 0

	while not(node is None):
		num += 10**digit_place * node.val 
		digit_place += 1
		node = node.next

	return num

print(test())
