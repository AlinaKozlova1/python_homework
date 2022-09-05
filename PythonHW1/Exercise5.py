import math


def find_distance(x2, x1, y2, y1):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Distance between ({x1},{x2}) and ({y1},{y2}) is equal to {distance}")

find_distance(7, 3, 15, 12)