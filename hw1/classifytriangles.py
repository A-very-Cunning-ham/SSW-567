from math import sqrt


def classify_triangle(a, b, c):
    """ 
    Based on 3 side lengths, return the triangle properties: scalene, isosceles, or equilateral, and if it is a right triangle.
    Triangles are invalid if the summed length of their two shortest sides is shorter than the longest side
    """

    if not (isinstance(a, (int, float)) or isinstance(b, (int, float)) or isinstance(c, (int, float))) or a < 0 or b < 0 or c < 0:
        return("InvalidInput", "Nonright")

    a, b, c = sorted([a, b, c])

    if a + b <= c:
        return("NotATriangle", "Nonright")
    elif a != b != c:
        triangleType = "Scalene"
    elif a == c:
        triangleType = "Equilateral"
    else:
        triangleType = "Isosceles"

    if sqrt(a**2 + b**2) == c:
        rightTriangle = "Right"
    else:
        rightTriangle = "Nonright"

    return(triangleType, rightTriangle)



