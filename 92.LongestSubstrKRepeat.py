"""
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb",
as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
s = 'ababbc'
k = 2


def longestSubstring(s, k):
    res = 0
    for i in range(1, len(set(s)) + 1):
        times = [0] * 26
        l = r = ct = dif_ct = 0
        while r < len(s):
            ind = ord(s[r]) - ord('a')
            times[ind] += 1
            if times[ind] == 1:
                dif_ct += 1
            if times[ind] == k:
                ct += 1
            r += 1

            while l < r and dif_ct > i:
                ind = ord(s[l]) - ord('a')
                if times[ind] == k:
                    ct -= 1
                if times[ind] == 1:
                    dif_ct -= 1
                times[ind] -= 1
                l += 1
            if dif_ct == ct == i:
                res = max(res, r - l)
    return res


print(longestSubstring(s, k))
