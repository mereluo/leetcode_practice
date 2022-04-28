"""
Given two non-negative integers, num1 and num2 represented as string,
return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library
for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Input: num1 = "11", num2 = "123"
Output: "134"
"""
num1 = '456'
num2 = '77'

# Method one
# def str2int(num):
#     result = 0
#     for n in num:
#         result = result * 10 + ord(n) - ord("0")
#     return result


# print(str(str2int(num1) + str2int(num2)))

# Method two (a quicker way)
num1 = list(num1)
num2 = list(num2)
car = 0
res = ''

while num1 or num2 or car:
    if num1:
        car += int(num1.pop())
    if num2:
        car += int(num2.pop())
    res += str(car % 10)
    car //= 10

print(res[::-1])
