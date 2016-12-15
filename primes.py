# -*- coding: utf-8 -*-

import math
import sys
import unittest

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):  # 3, 5, 7,..., √n
            if n % i == 0:
                return False
        return True

def primes(n):
    """n以下の素数のリスト(小さい順)を返す関数"""
    ### WRITE YOUR CODE HERE ###
    result = []
    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)
    return result
    ### END OF YOUR CODE ###

 
class Homework7(unittest.TestCase):
    def test_is_prime(self):
        for non_prime in (1, 4, 6, 8, 9, 10, 12):
            self.assertFalse(is_prime(non_prime))
        for prime in (2, 3, 5, 7, 11, 13, 17):
            self.assertTrue(is_prime(prime))
            
    def test_small_primes(self):
        self.assertEqual(primes(2), [2])
        self.assertEqual(primes(5), [2, 3, 5])
        self.assertEqual(primes(10), [2, 3, 5, 7])
 
    def test_corner_cases(self):
        self.assertEqual(primes(0), [])
        self.assertEqual(primes(1), [])
 
    def test_large_primes(self):
        self.assertEqual(primes(101), [2, 3, 5, 7, 11, 13, 17, 19, 23,
                                       29, 31, 37, 41, 43, 47, 53,
                                       59, 61, 67, 71, 73, 79, 83,
                                       89, 97, 101])
 
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Homework7)
    unittest.TextTestRunner(verbosity=2, stream=sys.stderr).run(suite)