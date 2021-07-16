ans = str(input())
guess = str(input())
res = 0
for i in range(len(ans)):
    if len(ans) != len(guess):
        res = "Incomplete answer"
        break
    if ans[i] == guess[i]:
        res+=1
print(res)
