"""
Using this space for debugging
"""
sandwiches = [1, 0, 0, 0, 1, 1]
students = [1, 1, 1, 0, 0, 1]

while sandwiches and (sandwiches[0] in students):
    s = sandwiches.pop(0)
    students.remove(s)

print(students)
