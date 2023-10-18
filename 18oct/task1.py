"""
Fibonacci series: The sequence of numbers in which each number in the sequence is equal to the sum of two numbers before it.
 The Fibonacci Sequence is given as: Fibonacci Sequence = 0, 1, 1, 2, 3, 5, 8, 13, 21,
"""
n = int (input("Enter a number:"))
num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= n:
	print(next_number, end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2

"""Factorial number"""

num= int(input("Enter a number:"))
value=1
for i in range(2,num+1):
    value *= i
print(f' Factorial of {num} is: {value}')


