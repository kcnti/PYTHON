grade = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
ids = list()
grades = list()
new = dict()
while(True):
    try:
        _id, _grade = [str(x) for x in input().split()]
        ids.append(_id)
        grades.append(_grade)
    except:
        break

uids = [str(x) for x in input().split()]
for i in uids:
    x = ids.index(i)
    t = grade.index(grades[x])
    if t-1 < 0:
        continue
    grades[x] = grade[t-1]

for keys in ids:
    for values in grades:
        new[keys] = values
        grades.remove(values)
        break

new = sorted(new.items(), key=lambda x: x[0])

for i in new:
    print(i[0], i[1])
