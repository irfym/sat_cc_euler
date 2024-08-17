# What is the first triangular number to have over 500 divisors?

# import libraries and helpder functions
import helper_fns

# Generate triangular number sequence
tri_num = 1
factor_count = 0
i = 2

while factor_count <= 500:
    tri_num = tri_num + i
    factor_count = len(helper_fns.find_all_factors(tri_num))
    i = i + 1
print(tri_num, factor_count)

