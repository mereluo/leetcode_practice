"""
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Runtime: O(log n) -> indication of binary search
"""
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
l, r = 0, len(nums) - 1

while l <= r:
    m = (l + r) // 2  # set midpoint
    if target == nums[m]:
        print(m)

    # left sorted portion
    if nums[l] <= nums[m]:
        if target > nums[m] or target < nums[l]:
            l = m + 1  # search the right
        else:
            r = m - 1  # search the left

    # right sorted portion
    else:
        if target < nums[m] or target > nums[r]:
            r = m - 1  # search the left
        else:
            l = m + 1  # search the right

print(-1)
