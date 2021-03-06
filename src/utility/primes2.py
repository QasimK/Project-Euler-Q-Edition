import array
import math as maths

class PrimeList:
    """Generate and check for prime numbers"""
    
    def __init__(self):
        #: Starting from 0, 1, 2, 3, 4, 5, .... 1 means it *IS* a prime
        self.number_list = array.array('b', [0, 0, 1, 1, 0, 1])
    
    def max_known_number(self):
        """Return the maximum number which is known to be a prime or not"""
        return len(self.number_list)-1
    
    def is_prime(self, number):
        if self.max_known_number() < number:
            self.sieve(number)
        
        return self.number_list[number] == 1
    
    def sieve(self, upto_num):
        """Store primes up to and including the number specified."""
        max_cur_known = self.max_known_number()
        
        num_new = upto_num - max_cur_known
        #All new numbers are primes until they are crossed off
        self.number_list.extend(array.array('b', [1])*num_new)
        
        for marker_num in range(2, maths.floor(maths.sqrt(upto_num)) + 1):
            #For efficiency only use prime marked numbers
            if not self.is_prime(marker_num):
                continue
            
            min_x = max(max_cur_known // marker_num + 1, marker_num)
            max_x = upto_num // marker_num
            
            for x in range(min_x, max_x + 1):
                self.number_list[marker_num*x] = 0 # Non-prime
    
    def get_primes(self, startnum=2):
        """A generator which returns prime numbers
        
        It starts from 2 unless specified otherwise"""
        i = startnum
        while True:
            if self.is_prime(i):
                yield i
            i += 1
    
    def get_primes_in(self, grange):
        """Return generator yielding primes within a generator
        
        If you have a large grange, you are better off doing a sieve first."""
        for n in grange:
            if self.is_prime(n):
                yield n
    
    def get_prime_factors(self, number):
        """Yield the prime factors of a number"""
        for prime in self.get_primes():
            while number % prime == 0:
                yield prime
                number /= prime
            
            if number == 1:
                break
    
    def __str__(self):
        s=""
        for i, is_prime in enumerate(self.number_list):
            s += "%s: %s\n"%(i, ("Yes" if is_prime==1 else "No"))
        return s
    
    def _printraw(self):
        s=""
        for i, is_prime in enumerate(self.number_list):
            s += "%s: %s\n"%(i, is_prime)
        print(s)
