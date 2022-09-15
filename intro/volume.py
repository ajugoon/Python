# A simple program that uses the calculates the volume of a sphere.
# The answer is given to 3 decimal places.
# area = pi * r * r where pi = 3.14 and "r" is the radius.

import math

# "float" refers to a decimal
radius = float(input("Please enter the radius of the sphere \n"))

volume = 4/3 * (math.pi * radius ** 3)

volumeRounded = round(volume, 3) 

print ("")
print ("The volume of the sphere is " + str(volumeRounded) + " cubic units")