# Prog-10: Steganography
# 6330573721 Name Apichaya Mongkolphinyopas

import math
import copy
import numpy
from PIL import Image

# -----------------------------------------
def load_image(filename):   
    im = Image.open(filename).convert('RGB')        
    return numpy.asarray(im).tolist()   
        
def save_image(img, filename):       
    im = Image.fromarray(numpy.uint8(img))   
    im.save(filename)
     
def show_image(filename):       
    im = Image.open(filename)   
    im.show()       

def clone_image(img):
    return copy.deepcopy(img)

def char_to_bits(ch):
    return ('0000000' + bin(ord(ch))[2:])[-8:]

def bits_to_char( bits ):
    return chr( bits_to_int(bits) )

def int_to_bits(n):
    return ('0'*16 + bin(n)[2:])[-16:]

def bits_to_int( bits ):
    return int(bits,2)

def main():
    op = input('E(mbed text) or G(et text): ')
    if op == 'E' or op == 'G':
        file_in = input('Input image file (.png): ')
        if file_in[-4:] != '.png':
            file_in = file_in + '.png'
        if op == 'E':
            text = input('Text to be embedded: ')
            file_out = file_in[:-4] + '_x' + '.png'
            success = embed_text_to_image(text, file_in, file_out)
            if success:
                print('The output image file is', file_out)
            else:
                print('Need a bigger image.')
        else:
            txt = get_embedded_text_from_image(file_in)
            if txt == '':
                print('No hidden text.')
            else:
                print('The hidden text is', txt)
    else:
        print('Try again, re-enter E or G')
# --------------------------------------------------

def change_cb(c, b):
    if c%2 == 0 and b == 0:
        return c
    if c%2 == 0 and b == 1:
        return c+1
    if c%2 == 1 and b == 0:
        return c-1
    if c%2 == 1 and b == 1:
        return c

# --------------------------------------------------
def embed_text_to_image(text, file_in, file_out):
    if 16*3+8*len(text) < 16+(8*len(text))/3:
        return False
    result_bits = SPECIAL_BITS + int_to_bits(len(text)) + \
            ''.join([char_to_bits(x) for x in text]) + SPECIAL_BITS
    if len(result_bits)/3 > len(load_image(file_in))*len(load_image(file_in)[0]):
        return False
    lst = load_image(file_in)
    res_list = lst.copy()
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            for k in range(len(lst[i][j])):
                if len(result_bits) == 0:
                    break
                else:
                    ca = change_cb(lst[i][j][k], int(result_bits[0]))
                    res_list[i][j][k] = ca
                    result_bits = result_bits[1:]

    save_image(res_list, './{}'.format(file_out))
    return True


# --------------------------------------------------
def get_embedded_text_from_image(file_in):
    lst_in = load_image(file_in)
    string = ''
    length = 1
    _string = ''
    for i in range(len(lst_in)):
        for j in range(len(lst_in[i])):
            for k in range(len(lst_in[i][j])):
                if string[len(string)-16:] == SPECIAL_BITS and len(string) > 17:
                    break
                if (len(string) == 16 and string!= SPECIAL_BITS):
                    return ''
                num = lst_in[i][j][k]
                if num%2 == 0:
                    string+='0'
                else:
                    string+='1'
                #if len(string) == 32:
                #    string_ = string[16:]
                #    length = bits_to_int(int(string))
    
    if string[:16] != SPECIAL_BITS or string[len(string)-16:] != SPECIAL_BITS:
        return ''
    length = bits_to_int(string[16:32])
    char = string[32:len(string)-16]
    r = []
    while char:
        r.append(char[:8])
        char = char[8:]
    return ''.join([bits_to_char(x) for x in r])

# --------------------------------------------------
SPECIAL_BITS = '0100111101001011'
main()
