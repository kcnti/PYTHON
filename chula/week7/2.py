_input = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
if _input[0].lower() not in alphabet:
    ans = _input[1].lower()
    for i in range(2, len(_input)): 
        if _input[i].isdigit():
            ans+=_input[i]
        if _input[i].lower() not in alphabet:
            continue
        if _input[i-1].lower() not in alphabet:
            ans+=_input[i].upper()
            continue

        ans+=_input[i].lower()

else:
    ans = _input[0].lower()
    for i in range(1, len(_input)):
        if _input[i].isdigit():
            ans+=_input[i]
        if _input[i].lower() not in alphabet:
            continue
        if _input[i-1].lower() not in alphabet:
            ans+=_input[i].upper()
            continue
        ans+=_input[i].lower()
print(ans)
