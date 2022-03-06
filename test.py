# from array import array
import unittest
import binary
import linear


class SearchTest(unittest.TestCase):
    a = [1,6,7,9,10,15]
    def test_binary(self):
        self.assertEqual(binary.binary_search(self.a, 0, len(self.a)-1, 10), 4)
        self.assertEqual(binary.binary_search(self.a, 0, len(self.a)-1, 1), 0)
        self.assertEqual(binary.binary_search(self.a, 0, len(self.a)-1, 100), -1)

    def test_linear(self):
        self.assertEqual(linear.linear_search(self.a, 10), 4)
        self.assertEqual(linear.linear_search(self.a, 1), 0)
        self.assertEqual(linear.linear_search(self.a, 100), -1)


if __name__ == '__main__':
    unittest.main()