"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps,
merge them into [1,6].
"""

# 1. sort the intervals by first num
# 2. use first element as reference
# 3. compare the last end in res to the start value
# 4. if last end >= start --> max(lastend, end)
# 5. else: append([start, end])
intervals = [[1, 3], [2, 7], [2, 5], [10, 14], [11, 13], [15, 18]]
intervals.sort(key=lambda i: i[0])
output = [intervals[0]]

for start, end in intervals[1:]:
    lastEnd = output[-1][1]  # most recent end
    if lastEnd >= start:
        output[-1][1] = max(lastEnd, end)  # [1,5],[2, 4] -> [1,5]
    else:
        output.append([start, end])

print(output)
