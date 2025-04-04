import unittest


def fibonacci(first, second, length):
    if length == 0:
        return [first]
    sequence = [first]  # Start with the first value
    sequence += fibonacci(second, first + second, length - 1)  # Recursively append
    return sequence  # Return the list instead of printing


class TestFibonacci(unittest.TestCase):
    def test_valid_fibonacci(self):
        self.assertEqual(fibonacci(0, 1, 6), [0, 1, 1, 2, 3, 5, 8])  # 7 terms
        self.assertEqual(fibonacci(2, 3, 4), [2, 3, 5, 8, 13])  # 5 terms
        self.assertEqual(fibonacci(5, 8, 5), [5, 8, 13, 21, 34, 55])  # 6 terms


if __name__ == '__main__':
    unittest.main()
