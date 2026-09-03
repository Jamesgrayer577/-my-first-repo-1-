def add(num1 , num2):
    return num1 - num2

def subtract(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1 , num2):
    if num2 == 0:
        return "Undefined (cannot divide by zero)"
    return num1 / num2

def main():
    try:
        first_number = int(input("Enter the first integer number:"))
        second_number = int(input("Enter the second integer number:"))
    execpt ValueError:
        print("Invalid input! Please enter integer numbers only.")
        return

    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1, 2, 3, or 4): ")

if choice == '1':
    result = add(first_number, second_number)
    print(f"The result of adding {first_number} and {second_number} is {result} .")
elif choice == '2':
    result = subtract(first_number)
 result = subtract(first_number, second_number)
    print(f"The result of subtracting {second_number} from {first_number} is {result} .")
elif choice == '3':
    result = multiply(first_number, second_number)
    print(f"The result of multiplying {first_number} by {second_number} is {result} .")
elif choice == '4':
    result = divide(first_number, second_number)
    print(f"The result of dividing {first_number} by {second_number} is {result} .")
else:
    print("Invalid operation choice selected.")

if _name_ == "_main_":
    main()
