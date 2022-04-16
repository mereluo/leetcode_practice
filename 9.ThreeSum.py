"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Input: nums = [0]
Output: []

no duplicate triplets
"""
nums = [-1, 0, 1, 2, -1, -4]
# 1. sort the list
# 2. start with num[0] as a, find b+c = -a, skip duplicates
# 3. find b+c using l, r pointer
# 3.1 if b+c > -a, r -= 1, skip duplicates
# 3.2 if b+c < -a, l += 1, skip duplicates
res = []
nums.sort()
for i, a in enumerate(nums):
    if i > 0 and a == nums[i - 1]:
        continue

    l, r = i+1, len(nums)-1
    while r > l:
        threeSum = a + nums[l] + nums[r]
        if threeSum < 0:
            l += 1
        elif threeSum > 0:
            r -= 1
        else:
            res.append([nums[i], nums[l], nums[r]])
            l += 1
            # to skip duplicates, only need one pointer to move
            while nums[l] == nums[l - 1]:
                l += 1
        print(res)
