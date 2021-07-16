student_dict = {'John': 35.5, 'Mary': 73.0, 'Cindy': 83.5, 'Sean': 65.0,
'Barry': 81.0, 'Mark': 79.5, 'Eugene': 87.0, 'Bob': 49.5}
while True:
    name = input("Name : ")
    score = input("Score : ")

    if name in student_dict:
        print(student_dict[1])
#    if name != "" and score != "":
#        print(score)
#        student_dict.update({name:score})
#    elif name == "" and score == "":
#        break
print(student_dict)
