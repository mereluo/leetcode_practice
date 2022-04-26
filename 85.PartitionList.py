"""
Given the head of a linked list and a value x,
partition it such that all nodes less than x come
before nodes greater than or equal to x.

You should preserve the original relative order of
the nodes in each of the two partitions.

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n6 = ListNode(2)
n5 = ListNode(5, n6)
n4 = ListNode(2, n5)
n3 = ListNode(3, n4)
n2 = ListNode(4, n3)
n1 = ListNode(1, n2)
l1 = n1

x = 3

left, right = ListNode(), ListNode()
tailL = left
tailR = right

while l1:
    if l1.val < x:
        tailL.next = l1
        tailL = tailL.next
    else:
        tailR.next = l1
        tailR = tailR.next
    l1 = l1.next

tailL.next = right.next
tailR.next = None

reslist = []
while left:
    reslist.append(left.val)
    left = left.next
print(reslist)
