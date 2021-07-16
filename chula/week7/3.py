alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = alphabet_lower.upper()

while True:
    _input = input()
    ans = str()
    if _input == 'end':
        break
    for i in _input:
        if i in alphabet_lower:
            if alphabet_lower.index(i)+13 > len(alphabet_lower)-1:
                i = alphabet_lower[alphabet_lower.index(i)-13]
            elif alphabet_lower.index(i)+13 < len(alphabet_lower):
                i = alphabet_lower[alphabet_lower.index(i)+13]
        elif i in alphabet_upper:
            if alphabet_upper.index(i)+13 > len(alphabet_lower)-1:
                i = alphabet_upper[alphabet_upper.index(i)-13]
            elif alphabet_upper.index(i)+13 < len(alphabet_lower):
                i = alphabet_upper[alphabet_upper.index(i)+13]
        ans += i

    print(ans)
