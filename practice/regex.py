import re

string = 'search inside of this text please!'

a = re.search('this', string)
print(a, "\n", a.span(), "\n", a.start(), "\n", a.end(), "\n", a.group())
