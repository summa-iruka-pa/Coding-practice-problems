"""
39) You have a number, and your task is to repeatedly sum its digits until
you obtain a single-digit result. Write a method that performs this process
and returns the final single-digit sum. How will you design your method to
handle the iterative summing and achieve this ultimate single-digit result?
"""

def functions(n):
    sum = 0 
    while n > 0 :
        rem = n % 10 
        sum += rem
        n //= 10

    if sum < 10 :
        return sum
    else:
        return functions(sum)
    
n = 9999
print(functions(n))