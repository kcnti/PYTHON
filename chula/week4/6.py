string = str(input())
ans = ''
paren = 0
for i in string:
    if i == '(':
        i = '['
        paren+=1
    elif i == '[':
        i = '('
        paren+=1
    elif i == ')':
        i = ']'
        paren+=1
    elif i == ']':
        i = ')'
        paren+=1
    ans+=i

print('no parentheses') if paren == 0 else print(ans)
