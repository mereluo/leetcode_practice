"""
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""
s = "3[a2[c]]"

# stack used to maintain the substrings
# find the first ]
stack = []

for i in range(len(s)):
    if s[i] != ']':
        stack.append(s[i])
    else:  # if we find the ']'
        substr = ''
        while stack[-1] != '[':
            substr = stack.pop() + substr
        stack.pop()  # remove the nearest '['

        k = ''
        while stack and stack[-1].isdigit():
            k = stack.pop() + k

        stack.append(int(k) * substr)

print(''.join(stack))
