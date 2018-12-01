from sympy.ntheory.primetest import isprime
import random
from math import gcd


class BlumBlumShub():

    def run_bbs(self, bits, len_of_message):
        p = self.get_prime(bits)
        q = self.get_prime(bits)

        while p == q:
            q = self.get_prime(self, bits)

        n = p * q
        while True:
            s = random.randint(1, n - 1)
            if gcd(s, n) == 1:
                break
        key = ""
        state = s
        while len_of_message:
            state = (state ** 2) % n
            key += str(state % 2)
            len_of_message -= 1
        return key

    def get_prime(self, bits):
        while True:
            p = random.getrandbits(bits)

            if p & 1 == 0:
                p += 1
            while True:
                prob = isprime(p)
                if prob is True:
                    break
                else:
                    p += 2
            if p % 4 == 3:
                break
        return p
    #