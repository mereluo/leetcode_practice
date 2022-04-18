"""
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented
by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section)
are being trapped.
"""
# The gist:
# the min height of left/right side - height[i]
# determines the amount of water trapped

# 1. set l, r pointer, leftHeight, rightHeight
# 2. if height[l] > height[r]: l += 1, leftHeight - height[l]
# 3. same thing to the right

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
l, r = 0, len(height) - 1
leftMax, rightMax = height[l], height[r]
res = 0

while l < r:
    if leftMax < rightMax:
        l += 1
        leftMax = max(leftMax, height[l])
        res += leftMax - height[l]
    else:
        r -= 1
        rightMax = max(rightMax, height[r])
        res += rightMax - height[r]

print(res)
