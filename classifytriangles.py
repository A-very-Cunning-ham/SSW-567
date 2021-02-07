import unittest
from math import sqrt


def classify_triangle(a, b, c):
    """ 
    Based on 3 side lengths, return the triangle properties: scalene, isosceles, or equilateral, and if it is a right triangle.
    Triangles are invalid if the summed length of their two shortest sides is shorter than the longest side
    """

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



class Testclassify_triangle(unittest.TestCase):
    def test_nonright_scalene(self):
        self.assertEqual(classify_triangle(1, 2.5, 3), ("Scalene", "Nonright"))

    def test_right_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), ("Scalene", "Right"))

    def test_nonright_isosceles(self):
        self.assertEqual(classify_triangle(1, 1, 1.5), ("Isosceles", "Nonright"))

    def test_right_isosceles(self):
        self.assertEqual(classify_triangle(1, sqrt(2), 1), ("Isosceles", "Right"))

    def test_equilateral(self):
        self.assertEqual(classify_triangle(3, 3, 3), ("Equilateral", "Nonright"))

    def test_notATriangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), ("NotATriangle", "Nonright"))


if __name__ == '__main__':
    # show the classify_triangle function running as intended
    print(classify_triangle(1,2,2.5))
    print(classify_triangle(1,1,1))
    print(classify_triangle(3, 3, 3))
    print(classify_triangle(3, 4, 5))

    print(classify_triangle(6, 7, 3))
    # run the tests
    unittest.main(exit=True)
