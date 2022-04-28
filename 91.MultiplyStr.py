"""
Input: num1 = "123", num2 = "456"
Output: "56088"
"""
num1 = "123"
num2 = "456"

if "0" in [num1, num2]:
    print("0")

res = [0] * (len(num1) + len(num2))
num1, num2 = num1[::-1], num2[::-1]

for i1 in range(len(num1)):
    for i2 in range(len(num2)):
        digit = int(num1[i1]) * int(num2[i2])
        res[i1 + i2] += digit
        res[i1 + i2 + 1] += (res[i1 + i2] // 10)
        res[i1 + i2] = res[i1 + i2] % 10

# remove leading zeros
res, beg = res[::-1], 0
while beg < len(res) and res[beg] == 0:
    beg += 1

res = map(str, res[beg:])
print("".join(res))
