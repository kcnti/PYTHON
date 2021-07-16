x = [str(x) for x in input().split()]
grade = ['A', 'B', 'C', 'D', 'F']
grade.reverse()
y = 0
for i in x:
    d = grade.index(i)
    y += d
print(round(y/len(x), 2))
