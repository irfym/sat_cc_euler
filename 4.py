# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

n = 1001
palindrome_check = False

for n in range(998001,10000,-1):
    n_string = str(n)
    if n_string == n_string[::-1]:
        for d in range(100,999,1):
            if n%d == 0 and n/d > 100 and n/d < 999:
                palindrome_check = True
    if palindrome_check == True:
        print("Palindrome = " + n_string)
        break



