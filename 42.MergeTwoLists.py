"""
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# start from the last
n3 = ListNode(4)
n2 = ListNode(3, n3)
n1 = ListNode(1, n2)
l1 = n1

n4 = ListNode(4)
n5 = ListNode(2, n4)
n6 = ListNode(1, n5)
l2 = n6

# solutions
dummy = ListNode()
tail = dummy

while l1 and l2:
    if l1.val < l2.val:
        tail.next = l1
        l1 = l1.next
    else:
        tail.next = l2
        l2 = l2.next
    tail = tail.next

if l1:
    tail.next = l1
elif l2:
    tail.next = l2


tail.next = l1
tail = tail.next
tail.next = l2

dumlist = []
while dummy:
    dumlist.append(dummy.val)
    dummy = dummy.next

taillist = []
while tail:
    taillist.append(tail.val)
    tail = tail.next

print(dumlist)
print(taillist)
