"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_so_far = a[0]
curr_max = a[0]

for i in range(1, len(a)):
    print(a[i], curr_max+a[i])
    curr_max = max(a[i], curr_max + a[i])
    max_so_far = max(max_so_far, curr_max)

print(max_so_far)
