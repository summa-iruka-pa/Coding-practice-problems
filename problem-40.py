"""
40) You have a number (n) and need to unravel its factorial. Write a method
that calculates the factorial of this number, which is the product of all
positive integers up to (n). Can you figure out how to find this magical
product?
"""

n = int(input())
factorial = 1
for i in range(1,n+1):
    factorial *= i

print(factorial)