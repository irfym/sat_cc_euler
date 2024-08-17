import math

def find_prime_factors(n):
    """ Find all the prime factors of given n"""
    prime_numbers = set([2])
    prime_factors = set()
    new_n = n
    
    if n % 2 == 0:
        prime_factors.add(2)
        
    for i in range(3, n, 2):
        if i > new_n:
            #prime_factors.add(new_n)
            break
        for d in prime_numbers:
            is_prime = True
            if i % d == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.add(i)
            if new_n % i == 0:
                new_n = int(new_n/i)
                prime_factors.add(i)
    #print(prime_numbers)
    return(prime_factors)

def find_all_factors(n):
    """Find all factors of a given n"""
    factors = set([1,n])
    complimentary_factors = set()
    for i in range(2, math.floor(int(math.sqrt(n)))+1):
        if n % i == 0:
            factors.add(i)
    for f in factors:
        complimentary_factors.add(int(n/f))
    return(factors|complimentary_factors)