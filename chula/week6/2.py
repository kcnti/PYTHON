def is_prime(n): #ทดสอบวา่nเป็นจานวนเฉพาะหรอืไม่ 
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True

def next_prime(N):
    N+=1
    ans = 0
    for i in range(N, N*5):
        if is_prime(i):
            ans = i
            break
            
    return ans

def next_twin_prime(N):
    N+=1
    ans1 = 0
    ans2 = 0
    for i in range(N, N*10):
        if is_prime(i) and is_prime(i+2):
            ans1 = i
            ans2 = i+2
            break
    return ans1, ans2

#print(next_prime(10000000))
#print(next_twin_prime(10000000))



exec(input().strip())
