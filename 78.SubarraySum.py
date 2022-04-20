"""
Given an array of integers nums and an integer k,
return the total number of subarrays whose sum equals to k.
Input: nums = [1,1,1], k = 2
Output: 2
"""
nums = [1, -1, 1, 1, 1, 1]
k = 3

# Gist: save prefix sum and count of the sum
# if prefix sum = 1 appears twice, then we can throw them twice
res = 0
prefixSum = {0: 1}
curSum = 0

for n in nums:
    curSum += n
    diff = curSum - k

    res += prefixSum.get(diff, 0)  # if no, then 0
    prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

print(res)
