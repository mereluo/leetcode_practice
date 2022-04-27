"""
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

["cir","car"]
["c"]
"""

strs = ["cir", "car"]


def longest(strs):
    prefix = ''

    for i, char in enumerate(strs[0]):
        for s in strs:
            if i == len(s) or s[i] != char:
                return prefix
        prefix += char

    return prefix


print(longest(strs))
