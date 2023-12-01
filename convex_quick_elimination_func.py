import matplotlib.path as mpltPath
from convex_graham_scan_func import convex_hull_grahamscan 

def convex_hull_quickelimination(points):
    if len(points) < 3:
        return points  # Cannot form a convex hull with less than 3 points

    p0x = min(points, key=lambda x: x[0])
    p1x = max(points, key=lambda x: x[0])
    p0y = min(points, key=lambda x: x[1])
    p1y = max(points, key=lambda x: x[1])
    square = [p0x, p1x, p0y, p1y]  
    s_points = []

    for i in square:
        if i not in s_points:
            s_points.append(i)
    i = 0
    while len(s_points) < 3:
        while points[i] in s_points:
            i += 1
            if i >= len(points):
                break  # Avoid index out of range error

        if i < len(points):  # Make sure i is within bounds
            s_points.append(points[i])
            
    s_points.append(s_points[0])
    path = mpltPath.Path(s_points)
    unique = []
    for i in points:
        if not path.contains_point(i):
            unique.append(i)
    unique.extend(s_points)
    arr = []
    for i in unique:
        if i not in arr:
            arr.append(i)
    convex_hull = convex_hull_grahamscan(arr)
    
    return convex_hull
