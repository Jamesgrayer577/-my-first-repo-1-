#Author: James Grayer
#Program: Mod_10 - Lists
#Date: Oct, 27, 2026

def main():
    # Initialize an empty list to store the numbers
    numbers = []
    
    print("Please enter a series of 20 numbers:")
    
    # Loop 20 times to collect numbers from the user
    for i in range(20):
        while True:
            try:
                # Prompt the user for input and convert it to a float
                user_input = input(f"Enter number {i + 1}: ")
                num = float(user_input)
                numbers.append(num)
                break  # Exit the inner loop if conversion is successful
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    # Perform calculations using Python's built-in functions
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    
    # Display the analyzed data
    print("\n--- Number Analysis Results ---")
    print(f"The lowest number in the list:  {lowest}")
    print(f"The highest number in the list: {highest}")
    print(f"The total of the numbers:       {total}")
    print(f"The average of the numbers:     {average}")

# Run the program
if __name__ == "__main__":
    main()

PS G:\Users\James\AppData\Local\Programs\Microsoft VS Code> & C:\Users\James\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/James/OneDrive - Laramie County Community College/COSC 1010/python/.py"
Please enter a series of 20 numbers:
Enter number 1: 5
Enter number 2: 4
Enter number 3: 7
Enter number 4: 8
Enter number 5: 10
Enter number 6: 12
Enter number 7: 14
Enter number 8: 16
Enter number 9: 20
Enter number 10: 20
Enter number 11: 17
Enter number 12: 15
Enter number 13: 13
Enter number 14: 9
Enter number 15: 7
Enter number 16: 2
Enter number 17: 3
Enter number 18: 8
Enter number 19: 1
Enter number 20: 7

--- Number Analysis Results ---
The lowest number in the list:  1.0
The highest number in the list: 20.0
The total of the numbers:       198.0
The average of the numbers:     9.9
PS G:\Users\James\AppData\Local\Programs\Microsoft VS Code> 
