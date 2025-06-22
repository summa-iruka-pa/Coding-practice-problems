"""
35. CAPGEMINI 2023
Write a method to solve the following equation a3 + a2b + 2a2b + 2ab2 + ab2 + b3. 
Write a program to accept three values in order of a, b and c and
get the result of the above equation
"""
a = int(input())
b = int(input())

print(a**3 + a**2*b + 2*a**2*b + 2*a*b**2 + a*b**2 + b**3)