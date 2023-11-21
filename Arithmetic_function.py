#Exercise 6 - Arithmetic_function.py

def display_num(num1, num2):
  sum = int(num1) + int(num2)
  diff = int(num1) - int(num2)
  prod = int(num1) * int(num2)
  quotient = int(num1) / int(num2)
  
  print("The sum of num1 and num2 is:", sum)
  print("The difference of num1 and num2 is:", diff)
  print("The product of num1 and num2 is:", prod)
  print("The quotient of num1 and num2 is:", quotient)

num1 = input("input first number: ")
num2 = input("input second number: ")
display_num(num1, num2)
