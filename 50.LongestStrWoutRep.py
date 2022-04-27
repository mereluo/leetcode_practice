"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""
s = "pwwkew"
# left, right pointer
charSet = set()
l = 0
res = 0

for r in range(len(s)):
    while s[r] in charSet:
        charSet.remove(s[l])
        l += 1
    charSet.add(s[r])
    res = max(res, r-l+1)

print(res)
