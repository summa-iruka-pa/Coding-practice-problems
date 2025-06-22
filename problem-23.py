"""
23. You need to write a program that reads a number N and prints all
numbers from 1 up to N. The challenge is to keep the initialization statement
outside of the for loop and place the increment or decrement as the last
statement inside the for loop body. How will you design your program to
meet these conditions and produce the desired sequence?
Sample input:
Assume that N =5.
Sample output:
The first 5 natural numbers are 1, 2, 3, 4, 5.
"""
 
n = int(input())

for i in range(1,n+1):
    print(i)    