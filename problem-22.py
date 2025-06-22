"""
22. You need to write a program that reads a number (n) and prints all
numbers from 1 up to (n). However, there‘s a twist: keep the initialization
part outside of the `for` loop. How will you structure your program to
accomplish this?
Sample input:
Assume that N =5.
Sample output:
The first 5 natural numbers are 1, 2, 3, 4, 5.
"""

n = int(input())

for i in range(1,n+1):
    print(i)    