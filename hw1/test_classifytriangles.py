import unittest
from math import sqrt
from classifytriangles import classify_triangle


class TestClassifyTriangle(unittest.TestCase):

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

    def test_notatriangle(self):
        self.assertEqual(classify_triangle(1, 1, 3), ("NotATriangle", "Nonright"))

    def test_invalid_input(self):
        self.assertEqual(classify_triangle("a", "b", "c"), ("InvalidInput", "Nonright"))

    def test_negative_input(self):
        self.assertEqual(classify_triangle(-1, 2, 3), ("InvalidInput", "Nonright"))

    def test_negative_input2(self):
        self.assertEqual(classify_triangle(-2, -2, -3), ("InvalidInput", "Nonright"))


if __name__ == "__main__":
    # show the classify_triangle function running as intended
    print(classify_triangle(1, 1, 1.5))
    print(classify_triangle(1, 1, sqrt(2)))
    print(classify_triangle(1, 1, 1))
    print(classify_triangle(3, 3, 3))
    print(classify_triangle(3, 4, 5))
    print(classify_triangle(6, 7, 3))
    print(classify_triangle(1, 1, 4))
    print(classify_triangle(1, 0, 0))

    # run the tests
    unittest.main(exit=True)
