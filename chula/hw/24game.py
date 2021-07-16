# Prog-05: The 24 Game
# 6330573721 Name Apichaya Mongkolphinyopas

from itertools import permutations, product
import math

def generate_all_combinations(num_list, operators):
    all_combi = []
    for n,o in product(sorted(set(permutations(num_list))),
                       product(operators, repeat=3)): 
        x = [None]*(len(n)+len(o))
        x[::2] = n
        x[1::2] = o
        all_combi.append(x)
    return all_combi
#--------------------------------------------------------- 

def find_24(nlist):
    for i in range(len(nlist)):
        n1 = nlist[i][0]
        o1 = nlist[i][1]
        n2 = nlist[i][2]
        o2 = nlist[i][3]
        n3 = nlist[i][4]
        o3 = nlist[i][5]
        n4 = nlist[i][6]
        f1 = '( ( {} {} {} ) {} {} ) {} {}'.format(n1,o1,n2,o2,n3,o3,n4)
        f2 = '( {} {} ( {} {} {} ) ) {} {}'.format(n1,o1,n2,o2,n3,o3,n4)
        f3 = '( {} {} {} ) {} ( {} {} {} )'.format(n1,o1,n2,o2,n3,o3,n4)
        f4 = '{} {} ( ( {} {} {} ) {} {} )'.format(n1,o1,n2,o2,n3,o3,n4)
        f5 = '{} {} ( {} {} ( {} {} {} ) )'.format(n1,o1,n2,o2,n3,o3,n4)
        try:
            if eval(f1) == 24:
                return f1 + ' = 24'
            elif eval(f2) == 24:
                return f2 + ' = 24'
            elif eval(f3) == 24:
                return f3 + ' = 24'
            elif eval(f4) == 24:
                return f4 + ' = 24'
            elif eval(f5) == 24:
                return f5 + ' = 24'
        except:
             return 'No Solutions'
    return 'No Solutions'
#---------------------------------------------------------
nums = input('Enter 4 integers: ').split()

cases = generate_all_combinations(nums,  '+-*/' )
#print(cases[1])
ans = find_24(cases)

print(ans)
