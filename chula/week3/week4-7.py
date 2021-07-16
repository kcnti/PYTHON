number = str(input())
if len(number) == 10:
    if number.startswith("08") or number.startswith("09") or number.startswith("06"):
        print("Mobile number")
    else:
        print("Not a mobile number")
else:
    print("Not a mobile number")
