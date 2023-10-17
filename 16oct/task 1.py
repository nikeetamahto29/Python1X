"""
Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
input- score - 89
output- B
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
If, elif, else
"""

p = int(input("Enter the marks:"))
if p >=90 and p <=100:
    print ("Grade A")
elif p >=80 and p <=89:
    print ("Grade B")
elif p >=70 and p <=79:
    print ("Grade C")
elif p >=60 and p<=69:
    print ("Grade D")
elif p >=0 and p <=59:
    print ("Grade F")
else:
    print ("Positive integer required")

