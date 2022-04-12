"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
nums = [2, 7, 11, 15]
target = 9


def twoSum(nums, target):
    MapComp = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement not in MapComp:
            MapComp[n] = i
        else:
            return [MapComp[complement], i]


print(twoSum(nums, target))
