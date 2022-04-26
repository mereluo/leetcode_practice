"""
Given the head of a singly linked list and two integers left and right
where left <= right, reverse the nodes of the list from position left to
position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Input: head = [5], left = 1, right = 1
Output: [5]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
head = n1
left = 2
right = 4

dummy = ListNode(0, head)

# 1) reach node at position "left"
leftPrev, cur = dummy, head
for i in range(left - 1):
    leftPrev, cur = cur, cur.next  # 1: LP, 2: C

# Now cur = "left", leftPrev = "node before left"
# 2) reverse from left to right
prev = None
for i in range(right - left + 1):
    tmpNext = cur.next  # cur.next = 3
    cur.next = prev  # cur.next = none
    prev, cur = cur, tmpNext  # prev = 2, cur = 3

# 3) update pointers
leftPrev.next.next = cur  # 2 -> none then 2 -> 5
leftPrev.next = prev  # 1 -> 4

while dummy:
    print(dummy.val)
    dummy = dummy.next
