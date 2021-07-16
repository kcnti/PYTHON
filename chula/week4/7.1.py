word = str(input())
string = str(input())
count = 0
for i in range(len(string)):
  if string[i] in ['"', '(', ')', ',', '.', "'"]:
    string = string[:i] + ' ' + string[i+1:]
lst = string.split()
for i in range(len(lst)):
  if lst[i] == word:
    count+=1
print(count)
