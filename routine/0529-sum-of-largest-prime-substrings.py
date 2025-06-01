from functools import cache
from math import sqrt


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        primes = set()

        @cache
        def is_prime(num):
            if num == 1:
                return False
            if num == 2:
                return True
            for i in range(2, int(sqrt(num) + 1)):
                if num % i == 0:
                    return False
            return True

        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i : j + 1]
                num = int(sub)
                if is_prime(num):
                    primes.add(num)
        return sum(sorted(primes, reverse=True)[:3])
