"""
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
"""


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# node = [TreeNode{val: 1, left:
#                  TreeNode{val: 2, left: None, right:
#                           TreeNode{val: 5, left: None, right: None}}, right:
#                  TreeNode{val: 3, left: None, right:
#                           TreeNode{val: 4, left: None, right: None}}}]

print(deque(root))
res = []
q = deque([root])

while q:
    rightSide = None
    qLen = len(q)

    for i in range(qLen):
        node = q.popleft()
        if node:
            rightSide = node
            q.append(node.left)
            q.append(node.right)

        if rightSide:
            res.append(rightSide.val)

        print(res)
