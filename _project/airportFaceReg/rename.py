import sys
import os

#number = sys.argv[1]

def rename(_dir):
    path = [os.path.join(_dir, f) for f in os.listdir(_dir)]
    number = [i for i in path]
    print(number)

rename("data")