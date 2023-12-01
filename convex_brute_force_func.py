from convex_jarvis_march_func import convex_hull_jarvismarch as js
def _validate_input(points):
    return sorted(set(tuple(point) for point in points))

def _det(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def convex_hull_bruteforce(points):
    points = _validate_input(points)
    n = len(points)
    convex_set = set()

    for i in range(1,n):
        for j in range(1,n):
            for k in range(1,n):
                _det(points[i],points[j],points[k])

    for i in range(n - 1):
        for j in range(i + 1, n):
            points_left_of_ij = points_right_of_ij = False
            ij_part_of_convex_hull = True

            for k in range(n):
                if k != i and k != j:
                    det_k = _det(points[i], points[j], points[k])

                    if det_k > 0:
                        points_left_of_ij = True
                    elif det_k < 0:
                        points_right_of_ij = True
                    else:
                        if points[k] < points[i] or points[k] > points[j]:
                            ij_part_of_convex_hull = False
                            break

            if points_left_of_ij and points_right_of_ij:
                ij_part_of_convex_hull = False

            if ij_part_of_convex_hull:
                convex_set.update([points[i], points[j]])

    hull = js(points)
    return hull