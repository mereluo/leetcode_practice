"""
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
"""
from collections import Counter, deque
import heapq
# tasks = ["A", "A", "A", "B", "B", "C", "C"]
# n = 4
tasks = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
n = 2

count = Counter(tasks)
maxHeap = [-cnt for cnt in count.values()]  # [-3, -2, -2]
heapq.heapify(maxHeap)

time = 0
q = deque()

while maxHeap or q:
    time += 1
    if maxHeap:
        cnt = 1 + heapq.heappop(maxHeap)
        if cnt:
            q.append([cnt, time + n])
    if q and q[0][1] == time:
        heapq.heappush(maxHeap, q.popleft()[0])

print(time)
