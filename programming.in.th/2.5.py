a = int(input())
b = int(input())
c = int(input())
s = a + b + c
dic = {80:'A', 75:'B+', 70:'B',
       65:'C+', 60:'C', 55:'D+',
       50:'D', 0:'F'}
for score, grade in dic.items():
    if s >= score:
        print(grade)
        break
