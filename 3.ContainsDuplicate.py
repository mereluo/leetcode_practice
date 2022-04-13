"""
Input: nums = [1,2,3,1]
Output: true
"""

nums = [1, 2, 3, 1]
checkSet = set()

for n in nums:
    if n in checkSet:
        print(True)
    checkSet.add(n)

print(False)
