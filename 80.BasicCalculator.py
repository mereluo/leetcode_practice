"""
Input: s = "3+2*2"
Output: 7

Input: s = " 3/2 "
Output: 1

Input: s = " 3+5 / 2 "
Output: 5
"""
# calculate * and / first, stop when + or - appears

s = '-1+23-3/4'


def calculate(s):
    if not s:
        return 0

    stack, curr_num, operator = [], 0, "+"
    all_operators = '+-*/'
    nums = '0123456789'

    for i in range(len(s)):
        char = s[i]

        if char in nums:
            curr_num = curr_num * 10 + int(char)

        if char in all_operators or i == len(s) - 1:
            if operator == "+":
                stack.append(curr_num)
            elif operator == "-":
                stack.append(-curr_num)
            elif operator == '*':
                stack[-1] *= curr_num
            else:
                temp = stack.pop()
                if temp // curr_num < 0 and temp % curr_num != 0:
                    stack.append(temp//curr_num + 1)
                else:
                    stack.append(temp//curr_num)

            curr_num = 0
            operator = char

    return sum(stack)


print(calculate(s))
