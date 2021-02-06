import unittest
from math import sqrt


def classify_triangle(a, b, c):
    """ based on 3 side lengths, return the triangle type: scalene, isosceles, or equilateral, and if  it is a right triangle"""

    a, b, c = sorted([a, b, c])

    if a + b <= c:
        return("NotATriangle", False)
    elif a != b != c:
        triangleType = "Scalene"
    elif a == c:
        triangleType = "Equilateral"
    else:
        triangleType = "Isosceles"

    rightTriangle = sqrt(a**2 + b**2) == c or sqrt(a**2 + c**2) == b or sqrt(b**2 + c**2) == a

    return(triangleType, rightTriangle)



class Testclassify_triangle(unittest.TestCase):
    def test_nonright_scalene(self):
        self.assertEqual(classify_triangle(1, 2.5, 3), ("Scalene", False))

    def test_right_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), ("Scalene", True))

    def test_nonright_isosceles(self):
        self.assertEqual(classify_triangle(1, 1, 1.5), ("Isosceles", False))

    def test_right_isosceles(self):
        self.assertEqual(classify_triangle(1, 1, sqrt(2)), ("Isosceles", True))

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), ("Equilateral", False))

    def test_notATriangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), ("NotATriangle", False))


if __name__ == '__main__':
    unittest.main()
