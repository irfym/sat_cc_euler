# This is a combinatorics problem.
# Each 20x20 grid must have a path of exactly 40 moves, consisting
# of 20 rights and 20 downs. The rights and downs are not 'unique'
# in their nature.

# There are 40! ways of combining these 40 moves, divided by 20! as
# the 'rights' can be arranged in any order whilst maintaining uniqueness
# and divided by 20! again as the 'downs' can similarly be re-arranged between them

import math

def enum_lattice_paths(n):
    """Finds number of paths through a lattice described of side n"""
    paths = math.factorial((2*n))/(math.factorial(n)*math.factorial(n))
    return paths

print(enum_lattice_paths(20))
    