grade = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
ids = list()
grades = list()

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

for i in range(len(ids)):
    print(ids[i], grades[i])
