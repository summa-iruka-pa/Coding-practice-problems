"""
32. Generation of Fibonacci series. You need to write a method that prints
the first (n) numbers in the Fibonacci series, where (n) is provided as input.
How will you design this method to generate and display the sequence of
Fibonacci numbers up to (n)?
"""
first = 0
next = 1
n = int(input())
print(f"Fibonacci series of {n} values : " ,end=' ')

for i in range(n):
    print(first ,end=' ')
    first , next = next , first+next



