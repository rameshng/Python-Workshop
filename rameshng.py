
import math
import random

# Print pi value and type 
pi = math.pi
print ("The value of pi is ",pi, "and the type is", type(pi))

# Print all values les than 50
i = random.randint(0, 100)
if i<50:
    print("i is less than 50")
elif i>50:
    print("i is greater to 50")
else:
    print("i is equal than 50")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit == 'orange':
    print("The color of the",picked_fruit,"is Orange")
elif picked_fruit == 'strawberry':
    print("The color of the",picked_fruit,"is Red")
elif picked_fruit == 'banana':
    print("The Color of the",picked_fruit,"is Yellow") 

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def multiplication(x,y):
    a=x*y
    return a

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",multiplication(12,96))
print("48 x 17 =",multiplication(48,17))
print("196523 x 87323 =",multiplication(196523,87323))