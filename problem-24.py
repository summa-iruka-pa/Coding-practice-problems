"""
24. You have a number (n), and your task is to write a program that prints
the squares and cubes of all numbers from 1 up to n. Use a `while` loop to
generate and display these values. How will you set up your program to
calculate and show both the squares and cubes for each number in the
range?
Sample input:
Assume that N =5.
Sample output:
The square of first 5 natural numbers are 1, 4, 9, 16, 25.
The cube of first 5 natural numbers are 1, 8, 27, 64, 125
"""

def square(n):
    for i in range(1,n+1):
        yield i**2
def cube(n):
    for i in range(1,n+1):
        yield i**3

n = int(input())
print(f"The square of first {n} natural numbers are {' '.join(map(str,square(n)))}")
print(f"The cube of first {n} natural numbers are {' '.join(map(str,cube(n)))}")