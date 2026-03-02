import utilities

print("Select operation to do: ")
print("1. Sum")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter operation you want to do: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = utilities.calculator(num1, num2, choice)
print(result)