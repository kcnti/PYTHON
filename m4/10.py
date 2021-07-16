phone_database = []

while True:
    first_name = input("name")
    last = input("last")
    tel = input("tel")
    phone_entry = {first_name , last , tel}
    if first_name != "" and last != "" and tel != "":
        phone_database.append(phone_entry)
    elif first_name == "" and last == "" and tel == "":
        break
print(phone_database)

