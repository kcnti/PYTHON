my_list = [10,20,30,40,50,60,70,80,90,100]
print(my_list[3:8])
print(my_list[2:6])
print(my_list[:9])
print(my_list[4:])

#--------------

names=['Arm','Bobby','Cathy','Dorothy','Emily']
heights = [163.5,150.0,167.0,161.25,170.0]
answer = [[x,y] for x,y in zip(names,heights) if x.startswith("A") == False and x.startswith("C") == False]
 

for z in answer:
    if z[1] <= 160:
        del z[1]
print (answer)

#--------------


names=['Arm','Bobby','Cathy','Dorothy','Emily']
scores=[86,78,54,65,34]
for x,y in zip(names,scores):
    if y >= 80:
        print(x,y,'4')
    elif y >= 70 and y <=80:
        print(x,y,'warning')
    else:
        print(x,y,'2','stop')

#--------------

x = input('type ; ')
y = input('type ; ')
z = input('type ; ')
string = [x,y,z]
print(string)
c = input('type 1 alphabet : ')
d = []
answer = [d.count(c) for d in string]

print(answer)

#--------------

def get_scores():
    score_list = []
    n = 0
    while True:
        value=input('Enter score')
        if value == 'q':
            break
        score_list.append(float(value))
    for x in score_list:
        if x < 50:
            n = n+1
            print("Fail student is",n)
    return score_list

get_scores()

#--------------

for x in range (101):
    if x%5==0 and x%8==0:
        print(x)
