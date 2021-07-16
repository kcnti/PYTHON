filename = input("Enter your filename : ")
extns = filename.split(".")
print("Your file extension is :",repr(extns[-1]))
#repr is when you output it has single quote