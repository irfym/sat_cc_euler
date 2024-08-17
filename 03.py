# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

n = 600851475143

prime_numbers = [2]
prime_factors = []
highest_pf = 2
new_n = n

# Find prime numbers, testing each one (i) against the n
# If n is divisible by the prime number, the upper bound to test against is reduced
# to new_n = n/i, to reduce to total search space and run time
for i in range(3, n, 2):
    if i >= new_n:
        prime_factors.append(new_n)
        break
    for d in prime_numbers:
        is_prime = True
        if i % d == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)
        if new_n % i == 0:
            new_n = int(new_n/i)
            prime_factors.append(i)
            highest_pf = max(i, new_n)

print("Highest prime factor: ", highest_pf)
print("Prime factors are: ", prime_factors)
print("Prime numbers are: ", prime_numbers)


