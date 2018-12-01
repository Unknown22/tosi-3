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
    # def generate_n(self, bits):
    #     p = self.get_prime(bits)
    #     q = self.get_prime(bits)
    #
    #     while p == q:
    #         q = self.get_prime(self, bits)
    #
    #     # print "GenerateN - p = " + repr(p) + ", q = " + repr(q)
    #     return p * q
    #
    # def __init__(self, bits):
    #     self.n = self.generate_n(bits)
    #     length = self.bit_len(self.n)
    #     seed = random.getrandbits(length)
    #     self.set_seed(seed)
    #
    # def set_seed(self, seed):
    #     self.state = seed % self.n
    #
    # def bit_len(self, x):
    #     assert (x > 0)
    #     q = 0
    #     while x:
    #         q = q + 1
    #         x = x >> 1
    #     return q
    #
    # def next(self, numBits):
    #     "Returns up to numBit random bits"
    #
    #     result = 0
    #     for i in range(numBits, 0, -1):
    #         self.state = (self.state ** 2) % self.n
    #         result = (result << 1) | (self.state & 1)
    #
    #     return result