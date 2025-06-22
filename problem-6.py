"""
6. You have two secret numbers, and you need to figure out how they relate
to each other using a set of special tools. Your challenge is to write a program
that uses these tools—>, >=, <, <=, ==, and !=—to uncover all the secrets
about how these numbers compare. How will you use each tool to solve the
puzzle?
For example, consider two numbers 15 and 20.
15 < 20 is true.
15 <= 20 is true.
15 > 20 is false.
15 >= 20 is false.
15 == 20 is false.
15 != 20 is true. 
"""

a = 15
b = 20

print(True if a < b else False)
print(True if a <= b else False)
print(True if a > b else False)
print(True if a >= b else False)
print(True if a == b else False)
print(True if a != b else False)