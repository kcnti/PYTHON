arr = []
while True:
    n = input()
    if n == 'q':
        break
    arr.append(float(n))

print("No Data") if len(arr) == 0 else print(round(sum(arr)/len(arr), 2))
    
    

