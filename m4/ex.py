import csv
with open("Data-score.csv") as files:
    reader = csv.reader(files)
    for x in reader:
        print((x[1]))
