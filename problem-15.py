"""
15. TCS 2023.
A washing machine works on the principle of Fuzzy System, the weight of
clothes put inside it for washing is uncertain but based on weight measured
by sensors and the water level chosen, it decides total time needed.
For low level water, the time estimate is 25 minutes, where approximately
weight is between 2000 grams or any nonzero positive number below that.
For medium level water, the time estimate is 35 minutes, where
approximately weight is between 2001 grams and 4000 grams.
For high level water, the time estimate is 45 minutes, where approximately
weight is above 4000 grams. Assume the capacity of machine is maximum
7000 grams.
When the weight is zero, time needed is 0 minutes.
If the weight exceeds maximum weight limit, then, print ―OVERLOADED‖,
and for all negative weights, the output is ―INVALID INPUT‖.
"""

weight = int(input())
time = 0

if weight < 0 :
    print("INVALID INPUT")
elif weight > 7000 :
    print("OVERLOADED")
else:
    if weight == 0 :
        time = 0
    elif weight <= 2000 :
        time = 25
    elif 2001 <= weight <= 4000 :
        time = 35
    elif 4001 <= weight <= 7000 :
        time = 45
    print(f"Estimated Time : {time}")
