"""
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""
# Keeping two values, curMin, curMax, because
# you never know if the next number if negative, then
# n * curMin would be larger

nums = [0, 1]
res = max(nums)
curMax, curMin = 1, 1

for n in nums:
    # curMax will be changed
    temp = curMax * n
    curMax = max(curMax * n, curMin * n, n)  # [1, -8] -> [1]
    curMin = min(temp, curMin * n, n)  # [-1, -8] -> [-8]
    res = max(res, curMax)

print(res)
