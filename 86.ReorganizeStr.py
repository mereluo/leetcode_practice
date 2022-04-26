"""
Given a string s, rearrange the characters of s so that
any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

Input: s = "aab"
Output: "aba"

Input: s = "aaab"
Output: ""
"""

import heapq
from collections import Counter, deque

s = "aab"

count = Counter(s)
maxHeap = [[-cnt, char] for char, cnt in count.items()]  # [-2, -1]
heapq.heapify(maxHeap)

prev = None
res = ""

while maxHeap or prev:
    # when there is remaining
    if prev and not maxHeap:
        print("")
        break

    # got the most frequent char
    cnt, char = heapq.heappop(maxHeap)
    res += char
    cnt += 1

    # add prev to heap
    if prev:
        heapq.heappush(maxHeap, prev)
        prev = None
    # update prev
    if cnt != 0:
        prev = [cnt, char]

print(res)
