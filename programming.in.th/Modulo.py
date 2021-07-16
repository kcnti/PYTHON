i = list(map(int, input().split()))
lst = []
for _ in i:
    lst.append(_%42)
print(sum(lst))
