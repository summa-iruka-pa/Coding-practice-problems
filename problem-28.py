"""
28. Generation of even series:
Create a method that prints the first (n) even numbers, where (n) is the input. How
will you design this method to generate and display the sequence of even numbers
correctly?
void evenSeries (int n) {
}
Sample Input/ Output:
Input: n = 5
Output: 2 4 6 8 10 
"""
print(' '.join(map(str,(i for i in range(2,int(input())*2 + 1,2)))))