import utilities

print("Select operation to do: ")
print("1. Sum")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Squareroot")

choice = int(input("Enter operation you want to do: "))

if choice > 0 and choice < 5:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = utilities.calculator(num1, num2, choice)
else:
    num = int(input("Enter number: "))
    result = utilities.calculator_adv(num, choice)
print(result)