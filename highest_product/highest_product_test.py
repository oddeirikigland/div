import unittest
from highest_product import highest_product


class TestHighestProduct(unittest.TestCase):
    def test_not_valid_lists(self):
        self.assertRaises(ValueError, highest_product, [])
        self.assertRaises(ValueError, highest_product, [1, 2])

    def test_positive_integers(self):
        self.assertEqual(highest_product([1, 1, 1]), 1)
        self.assertEqual(highest_product([7, 55, 22, 44, 7, 5, 20, 76]), 55 * 44 * 76)

    def test_positive_and_negative_integers(self):
        self.assertEqual(highest_product([-1, 1, 1]), -1)
        self.assertEqual(highest_product([-1, 1, 1, 1]), 1)

        self.assertEqual(highest_product([44, -55, 33, 22]), 44 * 33 * 22)
        self.assertEqual(highest_product([44, -55, 33, 22, -11]), 44 * 33 * 22)
        self.assertEqual(highest_product([44, -55, 33, -22, -11]), -55 * 44 * -22)
        self.assertEqual(highest_product([-44, -55, -33, -22, -11, 14]), -55 * -44 * 14)

        self.assertEqual(highest_product([-30, 20, 20, 20, -14]), -30 * 20 * -14)
        self.assertEqual(highest_product([-30, 20, 20, 20, -13]), 20 * 20 * 20)
        self.assertEqual(highest_product([-4, -1, -6, -7, -2, -8, 1]), 56)

    def test_all_negative_values(self):
        self.assertEqual(highest_product([-4, -1, -6, -7, -2, -8, -1]), -2)


if __name__ == "__main__":
    unittest.main()
