# Find the sum of all the primes below two million.

prime_numbers = [2]
is_prime = True
# Check all primes until length of prime list is 10,001
for i in range(3, 2000000, 2):
    for d in prime_numbers:
        if d > i/d:
            break
        is_prime = True
        if i % d == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)

print(len(prime_numbers))
print(prime_numbers[0:20])
print(sum(prime_numbers))
