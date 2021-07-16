num = int(input("First num : "))
num2 = int(input("Second num : "))
mod = num % num2
divine = num / num2
if mod > 0:
    print("even %d odd %d"%(divine,mod))
else:
    print("even %d"%divine)