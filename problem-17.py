"""
Question 17 ():
Write a program to implement a simple calculator that supports 5 basic arithmetic operations. The user should enter two numbers followed by a character indicating the desired operation. The operations and their corresponding characters are as follows:
'a' for Addition
's' for Subtraction
'm' for Multiplication
'd' for Division
'u' for Modulus (remainder of division)
The program should perform the operation based on the character input and display the result in the following format:
Example 1:
Input: 20 15 a
Output: 20a15 = 20 + 15 = 35
Example 2:
Input: 20 15 u
Output: 20u15 = 20 mod 15 = 5
Make sure to handle division by zero and invalid operation inputs gracefully.
"""

a = int(input("Operand-1 : "))
b = int(input("Operand-2 : "))
operator = input("Enter the operator : ")

match operator :
    case 'a' :
        print(a+b)
    case 's' :
        print(a-b)
    case 'm' :
        print(a*b)
    case 'd' :
        print(a/b)
    case 'u' :
        print(a%b)

