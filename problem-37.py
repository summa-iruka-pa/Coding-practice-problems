"""
37) You have a number and need to find out how many digits it contains.
How will you design your method to determine the total count of digits
accurately?
"""

def count(n):
    count = 0
    while n > 0 :
        n //= 10
        count += 1
    return count

n = 1234567890
print(count(n))
