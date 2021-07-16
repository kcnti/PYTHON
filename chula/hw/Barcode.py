# Prog-07: EAN-13 Barcode
# ??3?????21 Name ?

import math
import matplotlib.pyplot as plt
#-------------------------------------------------
def show_barcode(digits, ean13_code):   
    x = [[int(e) for e in ean13_code]]        
    plt.axis('off')   
    plt.imshow(x, aspect='auto', cmap='binary')        
    plt.title(digits)       
    plt.show()   
#-------------------------------------------------
def test1():
    digits = input('Enter a 13-digit number: ')     
    codes = encode_EAN13(digits)       
    if codes == '':   
        print(digits, 'is not an EAN-13 number.')       
    else:
        decoded_digits = decode_EAN13(codes)
        if decoded_digits == digits:
            show_barcode(digits, codes)
        else:
            print('Error in decoding.')
#-------------------------------------------------
L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', \
           '0110001', '0101111', '0111011', '0110111', '0001011']
G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', \
           '0111001', '0000101', '0010001', '0001001', '0010111']
R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', \
           '1001110', '1010000', '1000100', '1001000', '1110100']

#=================================================


group1 = ['LLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', 'LGGLLG',
        'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL']

def codes_of(digits, patterns):
    string = ""
    digits = [x for x in digits]
    for i in range(len(patterns)):
        if patterns[i] == "L":
            string+=L_codes[int(digits[i])]
        elif patterns[i] == "G":
            string+=G_codes[int(digits[i])]
        elif patterns[i] == "R":
            string+=R_codes[int(digits[i])]
        else:
            return 0
    return string


def digits_of(codes):
    string = ""
    n = 7
    for i in range(0, len(codes), n):
        num = codes[i:i+n]
        if num in L_codes:
            string+=str(L_codes.index(num))
        elif num in G_codes:
            string+=str(G_codes.index(num))
        elif num in R_codes:
            string+=str(R_codes.index(num))
        else:
            return 0
    return string


def patterns_of(codes): 
    string = ""
    n = 7
    for i in range(0, len(codes), n):
        num = codes[i:i+n]
        if num in L_codes:
            string+="L"
        elif num in G_codes:
            string+="G"
        elif num in R_codes:
            string+="R"
        else:
            return 0
    return string

def check_digit(digits):
    result = 0
    ten = 0
    for i in range(len(digits)):
        if i%2 == 0:
            result = result + int(digits[i])*1
        else:
            result = result + int(digits[i])*3
    _min = result-int(digits[0])*10
    for i in digits: 
        if result-int(i)*10 < _min:
            _min = result-int(i)*10
    return abs(_min)


def encode_EAN13(digits):
    if len(digits) != 13:
        return ""
    pattern_right = group1[int(digits[0])]
    string="101"
    string+=codes_of(digits[1:7], pattern_right)
    string+="01010"
    string+=codes_of(digits[7:], "RRRRRR")
    string+="101"
    return string

def decode_EAN13(codes):
    string = ""
    if len(codes) != 95:
        return ''
    lcodes = codes[3:45]
    rcodes = codes[50:len(codes)-3]
    pattern_check = patterns_of(lcodes)
    if pattern_check.startswith("R"):
        lcodes, rcodes = rcodes, lcodes
        pattern_check = patterns_of(lcodes)
    if pattern_check == 0:
        return ""
    string+=str(group1.index(pattern_check))
    string+=digits_of(lcodes)
    string+=digits_of(rcodes)
    check_dgt = check_digit(string[:-1])
    if int(string[-1]) != check_dgt:
        return ""
    return string

#-------------------------------------------------
test1()
