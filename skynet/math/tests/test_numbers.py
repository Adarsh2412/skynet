import unittest
from skynet.math import numbers

class FactorialTest(unittest.TestCase) :
    known_values = {
        0 : 1,
        1 : 1,
        2 : 2,
        3 : 6,
        5 : 120,
        8 : 40320,
        13 : 6227020800,
    }

    wrong_values = [-1, -2, -3, -5, -8]

    def test_recursive_factorial_known_values(self) :
        for n, factorial in self.known_values.items() :
            self.assertEqual(factorial, numbers.recursive_factorial(n))

    def test_iterative_factorial_known_values(self) :
        for n, factorial in self.known_values.items() :
            self.assertEqual(factorial, numbers.iterative_factorial(n))

    def test_builtin_factorial_known_values(self) :
        for n, factorial in self.known_values.items() :
            self.assertEqual(factorial, numbers.builtin_factorial(n))

    def test_recursive_factorial_wrong_values(self) :
        for n in self.wrong_values :
            self.assertRaises(ValueError, numbers.recursive_factorial, n)

    def test_iterative_factorial_wrong_values(self) :
        for n in self.wrong_values :
            self.assertRaises(ValueError, numbers.iterative_factorial, n)

    def test_builtin_factorial_wrong_values(self) :
        for n in self.wrong_values :
            self.assertRaises(ValueError, numbers.builtin_factorial, n)

class GCDTest(unittest.TestCase) :
    known_values = {
        (2, 3) : 1,
        (8, 20) : 4,
        (5, 2) : 1,
        (42, 91) : 7,
        (5, 0) : 5,
        (2, 1) : 1,
        (64, 16) : 16,
        (97, 33) : 1,
        (91, 78) : 13,
        (10**10, 2**12) : 2**10,
    }

    def test_recursive_gcd(self) :
        for (m, n), g in self.known_values.items() :
            self.assertEqual(g, numbers.recursive_gcd(m, n))
            self.assertEqual(g, numbers.recursive_gcd(n, m))

    def test_iterative_gcd(self) :
        for (m, n), g in self.known_values.items() :
            self.assertEqual(g, numbers.iterative_gcd(m, n))
            self.assertEqual(g, numbers.iterative_gcd(n, m))

class XGCDTest(unittest.TestCase) :
    known_values = {
        (2, 3) : 1,
        (8, 20) : 4,
        (5, 2) : 1,
        (42, 91) : 7,
        (75, 275) : 25,
        (5, 0) : 5,
        (2, 1) : 1,
        (64, 16) : 16,
        (97, 33) : 1,
        (91, 78) : 13,
        (10**10, 2**12) : 2**10,
    }

    def test_iterative_xgcd(self) :
        for (m, n), g in self.known_values.items() :
            x, y, h = numbers.iterative_xgcd(m, n)
            self.assertEqual(g, h)
            self.assertEqual(x*m + y*n, h)

    def test_recursive_xgcd(self) :
        for (m, n), g in self.known_values.items() :
            x, y, h = numbers.recursive_xgcd(m, n)
            self.assertEqual(g, h)
            self.assertEqual(x*m + y*n, h)

if __name__ == '__main__':
    unittest.main()