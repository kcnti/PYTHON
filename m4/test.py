def get_scores():
    score_list = []
    while True:
        value = input('Enter score: ')
        if value == "q":
            break
        score_list.append(float(value))
    return score_list
score = get_scores()
print("Scores = ",score)
print("Number of scores = ",len(score))
print("Average score = ",sum(score)/len(score))
print("Max = ", max(score))
print("Min = ", min(score))
        
