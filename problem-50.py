"""
50. ACCENTURE 2023
A carry is a digit that is transferred to left if sum of digits exceeds 9 while
adding two numbers from right-to-left one digit at a time. You are required to
implement the following method.
int numberOfCarries (int num1, int num2);
The methods accept two numbers ‗num1‘ and ‗num2‘ as its arguments.
You are required to calculate and return the total number of carries generated
while adding digits of two numbers ‗num1‘ and ‗num2‘.
Assumption: num1, num2>=0
 Carry 0 1 1
number1 = 4 5 1
number2 = 3 4 9
sum = 8 0 0
Output 1: 2
Explanation:
Adding ‗num 1‘ and ‗num 2‘ right-to-left results in 2 carries since (1+9) is 10. 1 is
carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.
Sample Input2:
Number 1: 23
Number 2: 563
Sample Output2: 0 ( as there are no carries generated). 
"""