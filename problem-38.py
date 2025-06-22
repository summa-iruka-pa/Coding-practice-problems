"""
38) You have a number, and your challenge is to find the sum of its digits.
Write a method that adds up each digit in the number and gives you the
total. How will you craft your method to calculate this sum effectively?
"""

def sum_of_digit(n):
    sum_of_digit = 0
    while n > 0 :
        rem = n % 10 
        sum_of_digit += rem
        n //= 10
    return sum_of_digit

n = 123456789
print(sum_of_digit(n))