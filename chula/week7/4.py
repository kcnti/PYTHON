first = sorted([x for x in input().lower()])
second = sorted([x for x in input().lower()])
for i in range(len(first)):
    try:
        first.remove(' ')
    except:
        break
for i in range(len(second)):
    try:
        second.remove(' ')
    except:
        break
if first == second:
    print("YES")
else:
    print("NO")
