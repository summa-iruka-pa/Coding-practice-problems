"""
12. You have a number to examine, and your mission is to write a program
that checks whether this number can be divided evenly by 27. Can you find
out if it‘s a multiple of 27?
"""

n = int(input())
print(f"{n} is divisible by 27" if n % 27 == 0 else f"{n} is not divisible by 27")