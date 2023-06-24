import unittest
from b import signs_list
from random import randint


class Syllables2Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(signs_list(">>"), [4, 3])

    def test_2(self):
        self.assertEqual(signs_list("<<"), [6, 7])

    def test_3(self):
        self.assertEqual(signs_list("><<<>>><>>>><><>>>"), [4, 5, 6, 7, 6, 5, 4, 5, 4, 3, 2, 1, 2, 1, 2, 1, 0, -1])


if __name__ == '__main__':
    unittest.main()
