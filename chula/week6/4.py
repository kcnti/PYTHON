import math
def distance1(x1, y1, x2, y2):
    return math.sqrt(((x2-x1)**2)+((y2-y1)**2))

def distance2(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def distance3(c1, c2):
    state = False
    d = math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)
    if c1[2]+c2[2] >= d:
        state = True

    return d, state

def perimeter(points):
    d = 0
    for i in range(len(points)):
        if i+1 < len(points):
            d+=distance2(points[i], points[i+1])
    d+=distance2(points[0], points[-1])
    return d

exec(input().strip())
