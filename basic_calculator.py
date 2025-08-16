# Program: Simple Calculator with Comparison

# Taking first number as input from user
first_num = input("Enter a number: ")
a = int(first_num)   # converting input string to integer

# Taking second number as input from user
second_num = input("Enter another number: ")
b = int(second_num)

# Asking user to choose the operator
operator = input("Enter the operator (+, -, *, /, //, %): ")

# Valid operators stored in a tuple
operators = "+", "-", "*", "/", "//", "%"

# Case 1: Both numbers are zero
if a == 0 and b == 0:
    print("Both are zeroes")

# Case 2: If operator is valid, perform the calculation
#Perform basic arithmetic operations (+,-,*,/,//,%)
elif operator in operators:
    if operator == "+":
        print("Result:", a + b)
    elif operator == "-":
        print("Result:", a - b)
    elif operator == "*":
        print("Result:", a * b)
    elif operator == "/":
        print("Result:", a / b)
    elif operator == "//":
        print("Result:", a // b)
    elif operator == "%":
        print("Result:", a % b)

# Case 3: If operator is invalid
else:
    print("Invalid operator")

# Additional Comparison Section
# Checking which number is greater, or if they are equal
if a > b:
    print("First number is greater than second number")
elif a < b:
    print("Second number is greater than first number")
else:
    print("Both numbers are equal")
