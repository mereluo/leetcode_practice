"""
Given an integer array nums,
return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

nums = [1, 2, 3, 4]
right = [1] * len(nums)
left = [1] * len(nums)

prefix = 1
for i in range(len(nums)):
    right[i] = prefix
    prefix *= nums[i]

print(right)

postfix = 1
for i in range(len(nums)-1, -1, -1):
    left[i] = postfix
    postfix *= nums[i]

print(left)

print([left[i] * right[i] for i in range(len(left))])
# 1, 2, 3, 4

# right: 24, 12, 4, 1
# left: 1, 1, 2, 6

# result: 24, 12, 8, 6
