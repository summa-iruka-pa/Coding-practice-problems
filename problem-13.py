"""
13. INFYTQ
You have a year in mind, and your task is to write a program that determines
if this year is a leap year. Can you figure out if it has an extra day in
February?
"""

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")