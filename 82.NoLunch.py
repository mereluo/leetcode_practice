"""
Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
"""
students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]


def countStudents(students, sandwiches):
    # once you cannot find any matching return it

    while sandwiches and (sandwiches[0] in students):
        s = sandwiches.pop(0)
        students.remove(s)

    return len(sandwiches)
