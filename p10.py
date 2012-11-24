import sys
import math

def check_prime(x):
    y = 2
    max_factor = int(math.sqrt(x))
    while y <= max_factor:
        if x % y == 0:
            return False
        y += 1
    return True

if __name__ == "__main__":
    end = 2000000
    x = 3
    answer = 0
    print "Starting!"
    while x < end:
        if check_prime(x):
            answer += x
        x += 2
    print "Sum of primes below two million is: " + str(answer)
