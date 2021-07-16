
def get_scores():
    score_list = []
    n = 0
    while True:
        value = input("Enter Score : ")
        if value =='q':
            break
        score_list.append(float(value))
    for x in score_list:
        if x <= 50:
            n = n + 1
            continue
    print('Number of fail student is ',n)
get_scores()
