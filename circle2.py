#!/usr/bin/python3
pi = 3.14159

radius = float(input("Radius (cm): "))
circumference = 2.0 * pi * radius
area = pi * radius * radius

print ("Circle: ")
print ("  radius            : %6.3f" % radius)	
print ("  circumference (cm): %6.3f" % circumference)
print ("  area(cm^2)        : %6.3f" % area)
