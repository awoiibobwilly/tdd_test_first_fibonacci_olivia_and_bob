import unittest


class TestFibonacci(unittest.TestCase):

    # Test for valid Fibonacci sequence generation
    def test_valid_fibonacci(self):
        self.assertEqual(PrintFibonacci(0, 1, 7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(PrintFibonacci(2, 3, 5), [2, 3, 5, 8, 13])
        self.assertEqual(PrintFibonacci(5, 8, 6), [5, 8, 13, 21, 34, 55])


if __name__ == '__main__':
    unittest.main()
