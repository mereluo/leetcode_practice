"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are
represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section)
the container can contain is 49.
"""

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# max(min-height * (x2 - x1))
# 1. start from start and end
# 2. if l < r: l + 1
# 3. update max

l, r = 0, len(height) - 1
maxW = 0

while r > l:
    h = min(height[l], height[r]) * (r - l)
    maxW = max(h, maxW)
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1

print(maxW)
