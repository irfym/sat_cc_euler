# Find the difference between the sum of the squares
# of the first one hundred natural numbers and the square of the sum.

# Sum of squares of first 100 natural numbers
sum_squares = 0
for i in range(1, 101, 1):
    sum_squares = sum_squares + (i ** 2)
print(sum_squares)

# Square of sum of first 100 natural numbers
square_of_sum = 0
sum_i = 0
for i in range(1, 101, 1):
    sum_i = sum_i + i
square_of_sum = sum_i ** 2
print(square_of_sum)

print("Difference of sum of squares and square of sum is: ",(square_of_sum - sum_squares))
