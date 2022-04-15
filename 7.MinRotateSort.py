"""
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Return the minimu number of the array
 -> have to run it in O(log(n)) time
"""

nums = [3, 4, 5, 1, 2]
res = nums[0]
l, r = 0, len(nums) - 1

while l <= r:
    # check if the first number is res
    if nums[l] < nums[r]:
        res = min(res, nums[l])
        break

    # if the array is rotated
    m = (l + r) // 2    # find the midpoint
    res = min(res, nums[m])
    if nums[m] >= nums[l]:
        l = m + 1
    else:
        r = m - 1

print(res)
