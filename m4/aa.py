scores_1 = [43,65,79,28,66,54,43,45,82,76]
scores_2 = [29,67,55,90,46,38,85,89,16,33]

all_scores = scores_1 + scores_2

print (sum(scores_1))
print (sum(scores_2))
print (min(scores_1))
print (len(all_scores))
print (sum(all_scores))
print (sum(all_scores)/len(all_scores))


month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
print (month[0:3])
print (month[3:6])
print (month[6:9])
print (month[9:12])


month_th = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤ๋ษภาคม','มิถุนายน','กรกฏาคม',
            'สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
for x in month_th:
    if x.endswith("คม"):
        print(x)


two_dice= range(0,7)
dice = [[x,y] for x in two_dice for y in two_dice]
print(dice)


three_dice = [[x,y,z] for x in two_dice for y in two_dice for z in two_dice if x+y+z == 5]
print(three_dice)

my_list = [10,20,30,40,50,60,70,80,90,100]
print(my_list[3:8])
print(my_list[2:6])
print(my_list[:9])
print(my_list[4:])

name = ['Arm','Bobby','Cathy','Dorothy','Emily']
height = [163.5,150.0,167.0,161.25,170.0]
soso = [[x,y] for x,y in zip(name,height) if x.startswith('A') == False and x.startswith('C') == False]
for z in soso:
    if z[1] <= 160:
        del z[1]
print (soso)


name = ['Arm','Bobby','Cathy','Dorothy','Emily']
score = [86,78,54,65,34]
for x,y in zip(name,score):
    if y >= 80:
        print(x,y,'4')
    elif y>=70 and y<80:
        print(x,y,'3 warning')
    else:
        print(x,y,'2 stop')


x = input('type : ')
y = input('type : ')
z = input('type : ')
string = [x,y,z]
print(string)
c = input('put alphabet : ')
d = []
result = [d.count(c) for d in string]
print (result)


def get_scores():
    score_list = []
    while True:
        value = input ('Enter Score : ')
        if value == 'q':
            break
        score_list.append(float(value))
    for x in score_list:
        if x < 50:
            n += 1
            print("student failed : ",n)
    return score_list

get_scores()



