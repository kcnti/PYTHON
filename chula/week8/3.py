string = [c.lower() for c in input()]
r = []
n = []
for i in string:
    if n.count(i) == 0 and i.isalnum():
        n.append(i)
        r.append([string.count(i)*-1, i])

r.sort(key=lambda t: t[1], reverse=True)
r = [[f*-1, s] for f, s in r]
r.sort(key=lambda t:t[0])
r.reverse()

for i in r:
    print('{} -> {}'.format(i[1], i[0]))
