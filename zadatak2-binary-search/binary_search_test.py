import unittest
import binary_search
import random


class TestRefSearch(unittest.TestCase):

    def test_empty(self):
        r = binary_search.ref_search([], 0)

        self.assertEqual(-1, r)

    def test_one(self):
        r = binary_search.ref_search([1], 1)

        self.assertEqual(0, r)

        r = binary_search.ref_search([1], 5)

        self.assertEqual(-1, r)

    def test_few(self):
        r = binary_search.ref_search([1, 5, 8, 11, 20, 21], 5)

        self.assertEqual(1, r)

        r = binary_search.ref_search([1, 5, 8, 11, 20, 21], 3)

        self.assertEqual(-1, r)

        r = binary_search.ref_search([1, 5, 8, 11, 20, 21], 1)

        self.assertEqual(0, r)

        r = binary_search.ref_search([1, 5, 8, 11, 20, 21], 20)

        self.assertEqual(4, r)


class TestMySearch(unittest.TestCase):

    def test_empty(self):
        r = binary_search.my_search([], 0)

        self.assertEqual(-1, r)

    def test_one(self):
        r = binary_search.my_search([1], 1)

        self.assertEqual(0, r)

        r = binary_search.my_search([1], 5)

        self.assertEqual(-1, r)

    def test_few(self):
        r = binary_search.my_search([1, 5, 8, 11, 20, 21], 5)

        self.assertEqual(1, r)

        r = binary_search.my_search([1, 5, 8, 11, 20, 21], 3)

        self.assertEqual(-1, r)

        r = binary_search.my_search([1, 5, 8, 11, 20, 21], 1)

        self.assertEqual(0, r)

        r = binary_search.my_search([1, 5, 8, 11, 20, 21], 20)

        self.assertEqual(4, r)


if __name__ == '__main__':
    unittest.main()