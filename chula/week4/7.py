word = str(input())
string = str(input())
string = ''.join(x for x in string if x not in '"(),.\'')
print(string.count(word))
