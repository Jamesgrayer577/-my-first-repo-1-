#Author: James Grayer
#Program: Mod_12 - Files
#Date: November, 10, 2026

# Ask the user for the file name
file_name = input("Enter the name of the file: ")

try:
    # Open the file in read-only mode
    with open(file_name, 'r') as file:
        print(f"\n--- First 5 lines of '{file_name}' ---")
        
        # Read and display up to 5 lines
        for i in range(5):
            line = file.readline()
            
            # If line is empty, the end of the file has been reached
            if not line:
                break
                
            # Print the line (strip removes extra trailing newlines)
            print(line.rstrip('\n'))

except FileNotFoundError:
    print(f"Error: The file '{file_name}' could not be found. Please check the name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
