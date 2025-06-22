"""
11. You have a number in hand, and your challenge is to write a program
that determines whether this number can be evenly divided by 100. Can you
uncover if it‘s a multiple of 100 or not?
"""

n = int(input())
print(f"{n} is divisible by 100" if n % 100 == 0 else f"{n} is not divisible by 100")