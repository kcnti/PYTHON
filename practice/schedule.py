while(True):
    enter_date = input("Enter your date : ")
    if enter_date == "q":
        break
    save_inform = input("Enter what to do in that day : ")
    f = open('C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python38-32\\_WORK_\\schedule.txt','a')
    f.write("%s %s\n"%(enter_date,save_inform))
print("your schedule has been save")
