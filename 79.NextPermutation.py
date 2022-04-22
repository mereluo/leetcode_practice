"""
For example, for arr = [1,2,3], the following are considered permutations of arr:
[1,2,3], [1,3,2], [3,1,2], [2,3,1].

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1,1,5]
Output: [1,5,1]
"""
# 1. find the pivot point (when i < i-1)
# 2. [i:] find the first number a that is larger than pivot
# 3. swap a and pivot
# 4. sort the [pivot:]
n1 = [1, 2, 3, 4, 5]
n2 = [1, 7, 3, 4, 6, 5]
n3 = [5, 4, 3, 2, 1]
n4 = [1, 3, 2, 5, 6]


def nextPermutation(nums):

    N = len(nums)
    pivot = 0

    for i in range(N-1, 0, -1):
        if nums[i-1] < nums[i]:
            pivot = i
            print(pivot)
            break
    if pivot == 0:
        nums.reverse()
        return

    swap = N-1
    while nums[pivot-1] >= nums[swap]:
        swap -= 1
    print(swap)

    nums[swap], nums[pivot-1] = nums[pivot-1], nums[swap]

    nums[pivot:] = reversed(nums[pivot:])


# print(nextPermutation(n1))
# print(n1)
print(nextPermutation(n2))
print(n2)
print(nextPermutation(n3))
print(n3)
print(nextPermutation(n4))
print(n4)
