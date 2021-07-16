_input = int(input())
_ = 0
print(_input)
for i in range(1, _input):
    if _input%i == 0:
        print(i, end=' ')
    _ += 1