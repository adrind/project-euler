##inspired by Dickson's method (cite: Wikipedia)
##if r is an even integer py-triplets can be found
##by finding the factor pairs of (r^2/2) and adding
##r+s, r+t, r+s+t to get a, b, c

import sys
import itertools

#computes all the factor pairs for n
def find_factors(n):
    factors = filter(lambda x: n%x == 0, range(1, int(n)))
    factor_pairs = []
    for factor in factors:
        for check in factors:
            if factor * check == n:
                factor_pairs.append((factor, check))
    return factor_pairs

#finds next py-triple for that even number value r
def next_pytri(r, f_list):
    (s, t) = f_list.pop()
    return r+s, r+t, r+s+t


if __name__ == "__main__":
    n = 4
    factor_list = [(2, 2), (4, 1)]
    a, b, c = next_pytri(n, factor_list)
    while a+b+c != 1000:
        if not factor_list:
            n+=2
            factor_list = find_factors(n*n*0.5)
        a, b, c = next_pytri(n, factor_list)
    print "a, b, and c are " + str(b) + ", " + str(a) + ", " +  str(c)
    print "Multiply to " + str(a*b*c)

    sys.exit()


