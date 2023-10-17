"""  Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.
3 Input
side 1, side 2 and side 3
output - Eq, Iso, Scalene -
Eq. = side 1 == side 2 = side 3  """

s1 = int(input("Enter the side1:"))
s2 = int(input("Enter the side2:"))
s3 = int(input("Enter the side3:"))

if s1 == s2 and s1 != s3:
    print ("It is an isosceles triangle ")
elif s1 == s2 and s2 == s3:
    print ("It is an equilateral triangle")
else:
    print ("It is a scalene triangle")