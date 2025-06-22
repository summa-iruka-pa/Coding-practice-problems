"""
36. CAPGEMINI 2023
A method is there which tells how many dealerships are there and the total
number of cars and number of two wheelers in each dealership. Your job is to
calculate how many tyres would be there in each dealership and find the total
number of tyres
"""

n = int(input("Enter the number of dealership : "))
wheels = 0

for i in range(1,n+1):
    
    # car wheels
    cars = int(input(f"Enter the number of cars for dealer {i} : "))
    wheels += cars*4

    # bike wheels
    bike = int(input(f"Enter the number of bikes for dealer {i} : "))
    wheels += bike*2

print(f"Total number of wheels{wheels}") 
