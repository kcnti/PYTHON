filename, year = [x for x in input().split()]
year = year[2:]
with open(filename, 'r') as f:
    d = f.read().split()
    stid = []
    score = []
    scoreid = []
    for i in range(len(d)):
        if i%2 == 0:
            stid.append(d[i])
        else:
            score.append(d[i])
    for i in stid:
        if i.startswith(year):
            scoreid.append(float(score[stid.index(i)]))
    if len(scoreid) == 0:
        print("No data")
    else:
        print(min(scoreid), max(scoreid), sum(scoreid)/len(scoreid))

