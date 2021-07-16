def num_to_base():
    while(True):
        convrt = input("0b(binary),0o(octal),0x(hexadecimal) : ")
        if convrt == "q":
            break
        text = int(input("Type the number that you want to convert : "))
        if convrt == "0b":
            binry = bin(text)
            print(binry)
        elif convrt == "0o":
            octl = oct(text)
            print(octl)
        elif convrt == "0x":
            hexe = hex(text)
            print(hexe)
#def base_to_num():
#    while(True):
#        convet = input("type a base number : ")
#        print(convet)

num_to_base()
#base_to_num()