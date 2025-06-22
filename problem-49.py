"""
49. ACCENTURE 2023
N-base notation is a system for writing numbers that uses only n different
symbol. The first n symbols from the given notation has to be used (Including the
symbol for o)
Decimal to n base notation are (0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9,
10: A,11: B and so on up to 35: Z).
Implement the following method char [] decimalToBaseN (int n, int number):
The method accepts positive integer n and num. Implement the method to
calculate the n-base equivalent of number and return the same as a string.
Steps:
 Divide the decimal number by n, Treat the division as the integer division
 Write the remainder (in n-base notation)
 Divide the quotient again by n, Treat the division as integer division
 Repeat step 2 and 3 until the quotient is 0
 The n-base value is the sequence of the remainders from last to first
Assumption:1 < base < = 36
Example Input:
12 base
718  n
Output
4BA
"""