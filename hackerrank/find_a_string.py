string = input().split()
sub_string = input().split()
for i in range(0, string):
    if sub_string in string:
        print(i)