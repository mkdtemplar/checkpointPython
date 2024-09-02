import math

coordinate_x: int
coordinate_y: int

type point = (int, int)


def distance(a: point, b: point) -> float:
    return abs(math.sqrt((math.pow((b[0] - a[0]), 2) + math.pow((b[1] - a[1]), 2))))

def area_rectangle(a, b, c: point) -> float:
    ab = distance(a, b)
    bc = distance(b, c)

    return ab * bc

def area_triangles(a, b, c : point) -> float:
    # Heron formula
    ab = distance(a, b)
    bc = distance(b, c)
    ca = distance(c, a)

    s = (ab + bc + ca) / 2.0
    return abs(math.sqrt(s * ( s - ab) * (s - bc) * ( s - ca)))

def check_point (a, b, c, d, p : point) -> bool:
    pab = area_triangles(p, a, b)
    pbc = area_triangles(p, b, c)
    pcd = area_triangles(p, c, d)
    pad = area_triangles(p, a, d)

    rectangle_area = area_rectangle(a, b, c)
    triangles_area = pab + pbc + pcd + pad

    return triangles_area <= rectangle_area

A: point = (1, 2)
B: point = (5, 2)
C: point = (5, 6)
D: point = (1, 6)
P: point = (3, 4)

if check_point(A, B, C, D, P) :
    print("inside")
else:
    print("outside")

