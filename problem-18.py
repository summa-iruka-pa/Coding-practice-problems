"""
18. Create a program that acts as a calculator capable of handling five basic
arithmetic operations. You‘ll use the symbols `+` for addition, `-` for
subtraction, `*` for multiplication, `/` for division, and `%` for finding the
remainder. How will you design your program to perform these operations
based on user input?
"""

a = int(input("Operand-1 : "))
b = int(input("Operand-2 : "))
operator = input("Enter the operator : ")

match operator :
    case '+' :
        print(a+b)
    case '-' :
        print(a-b)
    case '*' :
        print(a*b)
    case '/' :
        print(a/b)
    case '%' :
        print(a%b)

