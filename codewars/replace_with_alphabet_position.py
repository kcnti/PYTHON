from string import ascii_lowercase


def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(n.lower()) + 1) for n in text if n.isalpha())


def alphabet_position(text):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    ualpha = []
    for i in alpha:
        ualpha.append(i.upper())
    text = [char for char in text]
    res = []
#     remove thing that's not 
    for i in text:
        if not i.isalpha():
            text.remove(i)
#         
    for i in range(len(text)):
        if text[i] in ualpha:
            _a = ualpha.index(text[i])
            res.append(str(_a+1))
        if text[i] in alpha:
            a = alpha.index(text[i])
            res.append(str(a+1))
    print(res)
    return ' '.join(res)