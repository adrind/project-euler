###Problem 3 Euler
###solution based on direct search factorization algorithm
###found on Wolfram

import sys
import getopt
import math

def check_prime(x):
    y = 2
    max_factor = int(math.floor(math.sqrt(x)))
    while y < max_factor:
        if x % y == 0:
            return False
        y += 1
    return True

if __name__ == "__main__":
    start = 600851475143
    factor = int(math.floor(math.sqrt(start))) - 1 #makes it odd
    answer = 0
    print "Starting!"
    while 1:
        if not (start % factor) and check_prime(factor):
            answer = factor
        factor -= 2
        if answer:
            break
    print "Largest prime factor of 600851475143 is: " + str(answer)
    sys.exit()
