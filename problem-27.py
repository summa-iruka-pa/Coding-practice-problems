"""
27. Generation of odd series.
Create a method that prints the first (n) odd numbers, where (n) is provided as
input. How will you design this method to generate and display the sequence of
odd numbers correctly?
void oddSeries (int n) {
}
Sample Input/ Output:
Input: n = 5
Output: 1 3 5 7 9

"""

print(' '.join(map(str,(i for i in range(1,int(input())*2,2)))))
