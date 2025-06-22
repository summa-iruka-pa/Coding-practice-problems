"""
33. You have a number and need to check if it belongs to the Fibonacci
sequence, where each number is the sum of the two preceding ones. Write a
method to determine if this number is part of the Fibonacci series. Return
`true` if it is, and `false` if it isn‘t. How will you uncover whether this number
fits into the famous Fibonacci pattern?
"""
def isFibonacci(n):
    start = 0 
    next = 1

    while next < n :
        start , next = next , start + next

    return next == n or n == 0
    

n = int(input()) 
if isFibonacci(n):
    print("true")
else:
    print("false")