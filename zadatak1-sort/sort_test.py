import unittest
import sort


class TestRefSort(unittest.TestCase):
    def test_empty(self):
        r = sort.ref_sort([])
        self.assertEqual([], r)

    def test_one(self):
        r = sort.ref_sort([1])
        self.assertEqual([1], r)

    def test_few(self):
        r = sort.ref_sort([1, 5, 8, 3, 2, 0])
        self.assertEqual([0, 1, 2, 3, 5, 8], r)

    def test_repeat(self):
        r = sort.ref_sort([9, 4, 7, 2, 4, 0, 1, 0])
        self.assertEqual([0, 0, 1, 2, 4, 4, 7, 9], r)

class TestMySort(unittest.TestCase):
    def test_empty(self):
        r = sort.my_sort([])
        self.assertEqual([], r)

    def test_one(self):
        r = sort.my_sort([1])
        self.assertEqual([1], r)

    def test_few(self):
        r = sort.my_sort([1, 5, 8, 3, 2, 0])
        self.assertEqual([0, 1, 2, 3, 5, 8], r)

    def test_repeat(self):
        r = sort.my_sort([9, 4, 7, 2, 4, 0, 1, 0])
        self.assertEqual([0, 0, 1, 2, 4, 4, 7, 9], r)


if __name__ == '__main__':
    unittest.main()
