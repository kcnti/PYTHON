student_name = ['Arm','Bobby','Cathy','Dorothy','Emily']
student_height = [163.5,150.0,167.0,161.25,170.0]
a = [[x,y]for x,y in zip(student_name,student_height) if x.startswith("A") == False if x.startswith("C") == False]
for x,y in a:
    if y >= 160:
        print (x,y)

