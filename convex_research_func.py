def orientation(p, q, r):
    """
    Function to determine the orientation of three points (p, q, r).
    Returns:
        0 if the points are collinear
        1 if the orientation is clockwise
        -1 if the orientation is counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def convex_hull_andrews(points):
    """
    Andrew's Monotone Chain algorithm for finding the convex hull.
    Input:
        points: A list of tuples representing 2D points [(x1, y1), (x2, y2), ...].
    Returns:
        A list of tuples representing the convex hull in counterclockwise order.
    """
    # Sort the points lexicographically (by x-coordinate, then by y-coordinate)
    points = sorted(points)
    
    # Initialize upper and lower hulls
    upper_hull = []
    lower_hull = []
    
    # Build the upper hull
    for point in points:
        while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], point) != -1:
            upper_hull.pop()
        upper_hull.append(point)
    
    # Build the lower hull
    for point in reversed(points):
        while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], point) != -1:
            lower_hull.pop()
        lower_hull.append(point)
    
    # Concatenate the upper and lower hulls to get the convex hull
    convex_hull = upper_hull[:-1] + lower_hull[:-1]
    
    return convex_hull