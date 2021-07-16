import time
start = int(input("แม่คูณ = "))
end = int(input("แม่คูณตัวสุดท้าย = "))

for x in (start,end+1):
    print(x)
    for y in range(1,12+1):
        print(x,"x",y,"=",x*y)
        time.sleep(0.5)