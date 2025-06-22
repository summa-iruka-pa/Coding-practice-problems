"""
9. You have four secret numbers and your challenge is to write a program
that figures out which one is the largest and which one is the smallest. Use
your trusty if-else statements to solve this number mystery. Can you
determine the highest and lowest numbers among them?

"""
a = 234
b = 275
c = 456
d = 236
max = 0
min = 0

#maximum
if a > b and a > c and a > d :
    max = a
elif b > a and b > c and b > d :
    max = b 
elif c > a and c > b and c > d :
    max = c
else :
    max = d

#minimum
if a < b and a < c and a < d :
    min = a
elif b < a and b < c and b < d :
    min = b 
elif c < a and c < b and c < d :
    min = c
else :
    min = d

print(f"Minimum of all four is {min}")
print(f"Maximum of all four is {max}")