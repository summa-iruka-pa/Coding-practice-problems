"""
19. Imagine you‘re on a quest to discover never-ending loops. Create a
program that demonstrates two types of endless journeys: one using a `for`
loop and another using a `while` loop. How will you set up these loops to keep
running forever, showcasing their infinite nature?
"""

# for loop

for _ in iter(int,1):
    print("Infinite loop")

# while loop

while True :
    print("Infinite loop")