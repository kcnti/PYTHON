n = int(input())
s = 1
student_id = {}

for i in range(n*3):
    _id = input()
    if _id == '-': break
    student_id[_id] = s
    if s == n:
        s = 1
        continue
    s+=1

while(True):
    _input = input()
    if _input == 'quit':
        break
    if _input in student_id:
        print(student_id[_input])
    else:
        print('not found')

