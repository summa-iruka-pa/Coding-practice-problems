"""
14. You have two numbers, and your challenge is to write a program that
performs both addition and subtraction with them. However, if any
subtraction results in a negative number, display it as a positive value. How
will you tackle this and show the final results?
"""

a = int(input())
b = int(input())

print(f"Addition : {abs(a+b)}")
print(f"Addition : {abs(a-b)}")