"""
29. Generation of Table:
Create a method that prints the multiplication table for a given number (n). The
table should include the first 10 terms. How will you design this method to
generate and display the multiplication table?
void printTable (int n) {
}
Sample Input/ Output:
Input:
n = 5
Output:
5 * 1 =5
5 * 2 =10
5 * 3 =15
5 * 4 =20
Page / 10 of 80 Date : 02/06/2025 ,Version #3
5 * 5 =25
5 * 6 =30
5 * 7 =35
5 * 8 =40
5 * 9 =45
5 * 10 =50 
"""

n = int(input())

for i in range(1,11):
    print(f"{n} X {i} = {i*n}")