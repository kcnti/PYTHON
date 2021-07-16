import re

pattern = re.compile('this')
string = 'search this inside of this text please!'

a = pattern.search(string)
b = pattern.findall(string)
#print(a.group())
print(b)