# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int((n + 1) ** 0.5)):
        if n % i == 0:
            return False
    return True

def get_prime_factors(n):
    factors = []
    for i in range(1, int((n + 1)  ** 0.5)):
        if n % i == 0 and is_prime(i):
            factors.append(i)
    if is_prime(n):
        factors.append(n)
    return factors

print get_prime_factors(600851475143)
