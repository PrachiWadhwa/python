# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# num1= int(num1)
# num2= int(num2)
# print(f"The sum of {num1} and {num2} is {num1 + num2}.")
import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(f"The sum of {num1} and {num2} is {num1 + num2}.")