def gradingStudent(grade):
    res = []
    for j in grade:
        if j >=38:
            mod = j%5
            value = (5-mod)
            if value<3:
                j += value
            res.append(j)
        else:
            res.append(j)
    return res

n = int(input().strip())
grade = []
for i in range(n):
    grade.append(int(input().strip()))

result = gradingStudent(grade)
print(result)