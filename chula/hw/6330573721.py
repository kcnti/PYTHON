# Prog-08: Bag-of-Words
# 6330573721 Name Apichaya Mongkolphinyopas

def char_count(w):
    res = 0
    for i in w:
        res+=1
    return res - line_count(w)

def alphanumeric_count(w):
    res = 0
    for i in w:
        if i.isalnum():
            res+=1
    return res

def line_count(w):
    res = 0
    for i in w:
        if i == '\n':
            res+=1
    return res

def word_count(w):
    res = 0
    for i in w:
        res+=1
    return res

def fhash_calc(w, m): # w = list of character
    G = 37
    w = [i for i in w if i.isalnum()]
    res = ord(w[0])
    times = 1
    for i in w[1:]:
        res+=ord(i)*(G**times)
        times+=1
    return res%m

def fhash(w, m): # w = list of string
    #w = w.split()
    _list = []
    listnum = []
    res = []
    for i in range(len(w)):
        _list.append([j for j in w[i]])
        listnum.append(fhash_calc(_list[i], m))
    no_dups = []
    for i in listnum:
        count = listnum.count(i)
        if i not in no_dups:
            no_dups.append(i)
            res.append([i, count])
    return res

file_name = input("File name = ")
while(True):
    feature = input("Use feature hashing ? (y,Y,n,N) ").lower()
    if feature in ['y', 'n']:
        break
    else:
        print("Try again.")
    

stop_words = open('stopwords.txt', 'r')
stop_words = stop_words.read().split()
if feature.lower() == 'y':
    M = int(input("M = "))
    print('-------------------')
    with open(file_name, 'r') as f:
        text = f.read()
        print("char count = " + str(char_count(text)))
        print("alphanumeric count = " + str(alphanumeric_count(text)))
        print("line count = " + str(line_count(text)))
        print("word count = " + str(word_count(text.split())))
        words = []
        for i in text.split():
            if i.lower() in stop_words:
                continue
            words.append(i)
        print(fhash(words, M))
        f.close()

elif feature.lower() == 'n': 
    print('-------------------')
    with open(file_name, 'r') as f:
        text = f.read()
        print("char count = " + str(char_count(text)))
        print("alphanumeric count = " + str(alphanumeric_count(text)))
        print("line count = " + str(line_count(text)))
        print("word count = " + str(word_count(text.split())))
        words = []
        for i in text.split():
            if i.lower() in stop_words:
                continue
            string = str()
            for j in i:
                if j.isalnum():
                    string+=j
                else:
                    continue
            words.append(string)
        res = []
        no_dups = []
        for i in words:
            count = words.count(i)
            if i not in no_dups:
                no_dups.append(i)
                res.append([i, count])
        print(res)

