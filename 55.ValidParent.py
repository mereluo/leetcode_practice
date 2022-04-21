"""
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true
Input: s = "()[]{}"
Output: true
Input: s = "(]"
Output: false
"""

s = "()[]{(}"
# s = "([()()])"  # 2, 3, 2, -2, 2, -2, -3, -2
#s = "]"

stack = []
valMap = {")": "(",
          "]": "[",
          "}": "{"}

for c in s:
    if c in valMap:
        if stack and stack[-1] == valMap[c]:  # first condition not an empty stack
            stack.pop()
        else:
            print(False)
    else:
        stack.append(c)

if not stack:
    print(True)
else:
    print(False)
