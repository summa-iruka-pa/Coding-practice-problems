"""
34. Imagine you‘ve stumbled upon a magical sequence known as the
Fibonacci series. Your task is to uncover the (n)th number in this intriguing
sequence. Write a method to find and reveal the number that sits at position
(n) in the Fibonacci series. Can you unravel this sequence and discover the
(n)th term?

"""
def fibonacci(n):
    # print(n)
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
    
n = int(input())
print(f"The fibonacci value at {n} position is {fibonacci(n)}")