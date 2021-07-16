print("ข้อหนึ่ง")
scores_1 = [43,65,79,28,66,54,43,45,82,76]
scores_2 = [29,67,55,90,46,38,85,89,16,33]

print (sum(scores_1))
print (sum(scores_2))
print (min(scores_1))
print (len(scores_1+scores_2))
print (sum(scores_1+scores_2))
print (sum(scores_1+scores_2)/len(scores_1+scores_2))

#-----------------------
print('''


''')
print("ข้อสอง")
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
print(month[0:3])
print(month[3:6])
print(month[6:9])
print(month[9:12])

#-----------------------
print('''


''')
print("ข้อสาม")
month_th = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤ๋ษภาคม','มิถุนายน','กรกฏาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
for x in month_th:
    if x.endswith("คม"):
        print(x)

#-----------------------
print('''


''')
print("ข้อสี่")
two_dice = range(0,7)
dice = [[x,y] for x in two_dice for y in two_dice]
print (dice)

#-----------------------
print('''


''')
print("ข้อห้า")
three_dice = range(0,7)
result = [[x,y,z] for x in three_dice for y in three_dice for z in three_dice if x+y+z == 5]
print (result)
