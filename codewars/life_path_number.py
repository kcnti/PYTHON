def recursive(n):
    a = [int(i) for i in str(n)]
    if len(a) != 1:
        return recursive(sum(a))
    else:
        return sum(a)
    
def life_path_number(birthdate):
    a = birthdate.split('-')
    b = recursive(a[0])
    c = recursive(a[1])
    d = recursive(a[2])
    final = recursive(b+c+d)
    return final

print(life_path_number("1971-06-28"))