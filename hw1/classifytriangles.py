"""Module that helps to classify triangles"""
from math import sqrt


def classify_triangle(a, b, c):
    """
    Based on 3 side lengths, return the triangle properties: scalene, isosceles,
     or equilateral, and if it is a right triangle.
    Triangles are invalid if the summed length of their two shortest sides is
     shorter than the longest side
    """

    if (
        not (
            isinstance(a, (int, float))
            or isinstance(b, (int, float))
            or isinstance(c, (int, float))
        )
        or a < 0
        or b < 0
        or c < 0
    ):
        return ("InvalidInput", "Nonright")

    a, b, c = sorted([a, b, c])

    if a + b <= c:
        return ("NotATriangle", "Nonright")
    elif a != b != c:
        triangle_type = "Scalene"
    elif a == c:
        triangle_type = "Equilateral"
    else:
        triangle_type = "Isosceles"

    if sqrt(a ** 2 + b ** 2) == c:
        right_triangle = "Right"
    else:
        right_triangle = "Nonright"

    return (triangle_type, right_triangle)
