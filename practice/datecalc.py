from datetime import date
day1 = int(input("DD1 : "))
month1 = int(input("MM1 : "))
year1 = int(input("YY1 : "))
day2 = int(input("DD2 : "))
month2 = int(input("MM2 : "))
year2 = int(input("YY2 : "))

fdate = date(year1,month1,day1)
ldate = date(year2,month2,day2)
print(ldate - fdate)