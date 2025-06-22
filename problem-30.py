"""
30. Generation of Square Table
Create a method that prints the squares of all numbers from 1 up to a given
number (n). How will you design this method to generate and display the
squares of numbers in this range?
printSquareTable (n)
"""

n = int(input())
print("Square Table")
for i in range(1,n+1):
    print(f"Square({i}) = {i**2}")