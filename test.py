import unittest
from feature1 import count_words
from feature2 import sum_of_squares
from feature3 import square_roots

class TestFeature1(unittest.TestCase):
    def test_count_words(self):
        self.assertEqual(count_words("Hello, world! This is Feature 1."), 5)
        self.assertEqual(count_words("  Hello, world! This is Feature 1.   "), 5)
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("One two three."), 3)

class TestFeature2(unittest.TestCase):
    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares([1, 2, 3, 4]), 30)
        self.assertEqual(sum_of_squares([0, 0, 0]), 0)
        self.assertEqual(sum_of_squares([-1, -2, -3]), 14)
        self.assertEqual(sum_of_squares([5]), 25)

class TestFeature3(unittest.TestCase):
    def test_square_roots(self):
        self.assertEqual(square_roots([4, 9, 25]), [2.0, 3.0, 5.0])
        self.assertEqual(square_roots([1, 0]), [1.0, 0.0])
        # Assuming negative numbers should return "NaN"
        self.assertEqual(square_roots([4, -16, 25]), [2.0, "NaN", 5.0])

if __name__ == "__main__":
    unittest.main()
