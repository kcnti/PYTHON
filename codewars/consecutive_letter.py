def solve(st):
 #..
    res = []
    alpha2 = []
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    char2 = []
    char = [char for char in st]
    st = ''.join(sorted(st)) 
    for i in range(len(alpha)):
        if st.startswith(alpha[i]):
            char2.append(alpha[i])
            for _ in range(i,i+len(char)):
                char2.append(alpha[_])
    char.sort()
    print('print char1',char)
    char2 = sorted(set(char2))
    print('print char2',char2)
#     for i in range(len(char)):
#         alpha2.append(alpha[i])
#     print('print alpha2',alpha2)
    for i in char:
        if char != char2:
            print('1')
            return False
        if len(char) != len(set(char)):
            print('2')
            return False
        if i not in alpha:
            print('3')
            return False
        else:
            print('4')
            return True