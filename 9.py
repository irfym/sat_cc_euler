# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

b = 0
c = 0
limit = 1000

for a in range(1, int(limit), 1):
    for b in range(a+1, limit - 2*a):
        c = math.sqrt(a**2 + b**2)
        # print(a,b,c)
        if float(c).is_integer() and a + b + c == 1000:
            c = int(c)
            print(a, b, c)
            print(a**2, "+" , b**2, "=", c**2)
            print("Product is ", a*b*c)
            break
