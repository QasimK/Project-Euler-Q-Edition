import unittest

import utility.primes2 as primes

class Test(unittest.TestCase):
    def setUp(self):
        self.prime_list = primes.PrimeList()
    
    def test_is_prime(self):
        self.assertTrue(self.prime_list.is_prime(2))
        self.assertTrue(self.prime_list.is_prime(3))
        self.assertTrue(self.prime_list.is_prime(19))
        self.assertTrue(self.prime_list.is_prime(73))
        
        self.assertFalse(self.prime_list.is_prime(4))
        self.assertFalse(self.prime_list.is_prime(16))
        self.assertFalse(self.prime_list.is_prime(55))
    
    def test_sieve(self):
        self.prime_list.sieve(100)

        self.assertTrue(self.prime_list.is_prime(2))
        self.assertTrue(self.prime_list.is_prime(3))
        self.assertTrue(self.prime_list.is_prime(19))
        self.assertTrue(self.prime_list.is_prime(73))
        
        self.assertFalse(self.prime_list.is_prime(4))
        self.assertFalse(self.prime_list.is_prime(16))
        self.assertFalse(self.prime_list.is_prime(55))
        
        self.prime_list.sieve(1500)
        
        self.assertTrue(self.prime_list.is_prime(653))
        self.assertFalse(self.prime_list.is_prime(1220))
    
    def test_sieve_and_continue(self):
        self.assertTrue(self.prime_list.is_prime(73))
        self.assertFalse(self.prime_list.is_prime(55))
        
        self.prime_list.sieve(150)
        
        self.assertTrue(self.prime_list.is_prime(73))
        self.assertFalse(self.prime_list.is_prime(55))
        
        self.assertFalse(self.prime_list.is_prime(148))
        self.assertTrue(self.prime_list.is_prime(149))
        self.assertFalse(self.prime_list.is_prime(150))
        self.assertTrue(self.prime_list.is_prime(151))
        
        self.assertTrue(self.prime_list.is_prime(241))
        self.assertFalse(self.prime_list.is_prime(242))
    
    def test_get_primes(self):
        prime_generator = self.prime_list.get_primes()
        self.assertEqual(next(prime_generator), 2)
        self.assertEqual(next(prime_generator), 3)
        self.assertEqual(next(prime_generator), 5)
        self.assertEqual(next(prime_generator), 7)
        self.assertEqual(next(prime_generator), 11)
        self.assertEqual(next(prime_generator), 13)
        self.assertEqual(next(prime_generator), 17)
        self.assertEqual(next(prime_generator), 19)
        self.assertEqual(next(prime_generator), 23)
    
    def test_get_primes_in(self):
        primes = self.prime_list.get_primes_in(range(5, 13))
        self.assertEqual(next(primes), 5)
        self.assertEqual(next(primes), 7)
        self.assertEqual(next(primes), 11)
    
    def test_get_prime_factors(self):
        pfs = self.prime_list.get_prime_factors(36)
        self.assertEqual(list(pfs), [2, 2, 3, 3])
        
        pfs = self.prime_list.get_prime_factors(7)
        self.assertEqual(next(pfs), 7)
        with self.assertRaises(StopIteration):
            next(pfs)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()