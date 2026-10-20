#Author: James Grayer
#Program: Mod_9 - Strings
#Date: Oct, 20, 2026

def main():
    # Prompt the user for input
    user_input = input("Enter a 10-character telephone number (XXX-XXX-XXXX): ")
    
    # Initialize an empty string to store the translated number
    translated_number = ""
    
    # Loop through each character in the input string
    for char in user_input.upper():
        if char in "ABC":
            translated_number += "2"
        elif char in "DEF":
            translated_number += "3"
        elif char in "GHI":
            translated_number += "4"
        elif char in "JKL":
            translated_number += "5"
        elif char in "MNO":
            translated_number += "6"
        elif char in "PQRS":
            translated_number += "7"
        elif char in "TUV":
            translated_number += "8"
        elif char in "WXYZ":
            translated_number += "9"
        else:
            # Keep numbers, hyphens, or any other characters as they are
            translated_number += char
            
    # Display the result
    print(f"Translated phone number: {translated_number}")

# Call the main function to run the program
if __name__ == "__main__":
    main()

PS C:\Users\James> & C:/Users/James/.local/bin/python3.14.exe "c:/Users/James/OneDrive - Laramie County Community College/COSC 1010/python/.py"
Enter a 10-character telephone number (XXX-XXX-XXXX): 555-GET-FOOD
Translated phone number: 555-438-3663
PS C:\Users\James> 
