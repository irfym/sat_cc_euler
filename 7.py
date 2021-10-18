# What is the 10 001st prime number?

prime_numbers = [2]
i = 3
# Check all primes until length of prime list is 10,001
while len(prime_numbers) < 10001:
    for d in prime_numbers:
        is_prime = True
        if i % d == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)
    i = i + 1

print(len(prime_numbers))
print(prime_numbers)
