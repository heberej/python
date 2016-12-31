#!/usr/bin/python3
pi = 3.14159

radius = float(input("Radius (cm): "))
circumference = 2.0 * pi * radius
area = pi * radius * radius

print ("Circle: ")
print ("  radius            : " + str(radius))
print ("  circumference (cm): " + str(circumference))
print ("  area(cm^2)        : " + str(area))
