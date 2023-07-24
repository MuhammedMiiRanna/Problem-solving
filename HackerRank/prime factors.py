

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2+1):
        if (n % i) == 0:
            return False
    return True


def next_prime(p, n):
    fen = (range(p+1, n))
    for i in fen:
        if is_prime(i):
            return i


def factors(nbr):
    if nbr == 1:
        return 0
    if is_prime(nbr):
        return 1

    p = 2
    div, _ = divmod(nbr, p)
    factors = [p]

    while not is_prime(div):
        while divmod(div, p)[1]:
            p = next_prime(p, nbr)
        div, _ = divmod(div, p)
        factors.append(p)
    print(factors, div, end='\n\n')
    return len(factors)


samples = (
    (1, 0),
    (2, 1),
    (3, 1),
    (500, 4),
    (5000, 5),
    (10000000000, 10)
)

for index, (nbr, result) in enumerate(samples):
    factor_result = factors(nbr)
    print('>>> id_N-{:<2}: {:>9}{:<5}{:>22}{:<3}{:>8}{:<3}{:>17}{}'.format(index+1, ' number: ', nbr, ' - expected result: ', result,
          '- Result: ', factor_result, '  | This result is: ',  bool(result == factor_result)), end='\n\n')


# ################################
# Refrences:
# 1. https://www.calculatorsoup.com/calculators/math/prime-factors.php


# ################################
# Solution
# In order to maximize the unique number of primes, we multiply each prime in ascending order until the given limit is reached.
# Since we take each prime number into account only once, i.e. with exponent 11, and step up to the next larger prime,
# the overall number of distinct prime factors gets maximized. A simple implementation in Python is then:

# def primeCount(n):
#   primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

#   p = 1
#   i = 0
#   while True:
#     p*= primes[i]
#     if p > n:
#       return i
#     i+= 1
#   return 0


# ################################""
# for i in nex_prime(5):
#     print(i)
# print()

# for i in nex_prime(5):
#     print(i)
# print()

# for i in nex_prime(10):
#     print(i)
# print()

# for i in nex_prime(500):
#     print(i)

# ################################""
