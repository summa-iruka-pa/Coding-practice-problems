"""
41) Imagine you have two numbers, (n) and (r), and you need to uncover the
secret value of (nCr), which represents the number of ways to choose (r)
items from (n) items without regard to order. Write a method to calculate
this value. How will you solve this combinatorial puzzle?
Hint: nCr (n, r) = n! / ((n-r)! *r!)
"""
def factorial(n):
    if n == 1 : return 1
    else : return n*factorial(n-1)

def nCr(n,r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))

n = 5
r = 2
print(nCr(n,r))
    