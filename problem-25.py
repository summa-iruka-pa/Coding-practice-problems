"""
25. You need to write a program that reads a number (n) and calculates the
sum of the first (n) natural numbers. Use any type of loop to accomplish this.
How will you design your program to sum these numbers and display the
result?
Sample input:
Assume that n =5.
Sample output:
Sum of first 5 natural numbers = 1 + 2 + 3 + 4 +5 = 15.
"""

n = int(input())
print(f"Sum of first {n} natural numbers is {sum(range(n+1))}")