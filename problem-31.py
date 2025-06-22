"""
31. Generation of Cube Table:
Create a method that prints the cubes of all numbers from 1 up to a
given number (n). How will you design this method to generate and display
the cubes of numbers within this range?
"""

n = int(input())
print("Cube Table")
for i in range(1,n+1):
    print(f"Cube({i}) = {i**3}")