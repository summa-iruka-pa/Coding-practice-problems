"""
7. Imagine you have two secret letters, ‗A‘ and ‗B‘. Your task is to write a
program that uses different comparison tools to uncover how these letters
relate to each other. Can you figure out which one is greater or less than the
other? Use your program to solve this letter comparison mystery!
For example, consider two characters ‗A‘ and ‗B‘.
‗A‘ < ‗B‘ is true.
‗A‘ <= ‗B‘ is true.
‗A‘ > ‗B‘ is false.
‗A‘ >= ‗B‘ is false.
‗A‘ == ‗B‘ is false.
‗A‘ != ‗B‘ is true
"""
a = 'A'
b = 'B'

print(True if a < b else False)
print(True if a <= b else False)
print(True if a > b else False)
print(True if a >= b else False)
print(True if a == b else False)
print(True if a != b else False)