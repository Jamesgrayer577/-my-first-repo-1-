#Author: James Grayer
#Program: Mod_5 - Loops and Iteration 
#Date: Sept, 24, 2026

# Initialize total bugs collected
total_bugs = 0

# Loop for 5 days
for day in range(1, 6):
    num_bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += num_bugs

# Display the total number of bugs collected
print(f"Total number of bugs collected over 5 days: {total_bugs}")
Enter the number of bugs collected on day 1: 3
Enter the number of bugs collected on day 2: 5
Enter the number of bugs collected on day 3: 2
Enter the number of bugs collected on day 4: 1
Enter the number of bugs collected on day 5: 4
Total number of bugs collected over 5 days: 15


#Author: James Grayer
#Program: Mod_5 - Loops and Iteration 
#Date: Sept, 24, 2026

# Initialize variables
total_rainfall = 0.0
total_months = 0

# Get the number of years
years = int(input("Enter the number of years: "))

# Outer loop for each year
for year in range(1, years + 1):
    print(f"\n--- Year {year} ---")
    # Inner loop for each month
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        total_rainfall += rainfall
        total_months += 1

# Calculate average rainfall per month
average_rainfall = total_rainfall / total_months

# Display results
print("\n=== Rainfall Summary ===")
print(f"Total number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")# Initialize variables
total_rainfall = 0.0
total_months = 0

# Get the number of years
years = int(input("Enter the number of years: "))

# Outer loop for each year
for year in range(1, years + 1):
    print(f"\n--- Year {year} ---")
    # Inner loop for each month
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        total_rainfall += rainfall
        total_months += 1

# Calculate average rainfall per month
average_rainfall = total_rainfall / total_months

# Display results
print("\n=== Rainfall Summary ===")
print(f"Total number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")

PS C:\Users\James\OneDrive - Laramie County Community College\COSC 1010\python>  & 'C:\Users\James\AppData\Local\Python\pythoncore-3.14-64\python.exe' 'c:\Users\James\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\launcher' '54011' '--' 'c:\Users\James\OneDrive - Laramie County Community College\COSC 1010\python\.py 1.py' 
Enter the number of years: 3

--- Year 1 ---
Enter the inches of rainfall for month 1: 2.5
Enter the inches of rainfall for month 2: 1.5
Enter the inches of rainfall for month 3: 7.5
Enter the inches of rainfall for month 4: 4.5
Enter the inches of rainfall for month 5: 5.5
Enter the inches of rainfall for month 6: 4
Enter the inches of rainfall for month 7: 4
Enter the inches of rainfall for month 8: 2
Enter the inches of rainfall for month 9: 3
Enter the inches of rainfall for month 10: 2
Enter the inches of rainfall for month 11: 2
Enter the inches of rainfall for month 12: 1

--- Year 2 ---
Enter the inches of rainfall for month 1: 2.5
Enter the inches of rainfall for month 2: 3.5
Enter the inches of rainfall for month 3: 3.5
Enter the inches of rainfall for month 4: 2
Enter the inches of rainfall for month 5: 1
Enter the inches of rainfall for month 6: 2
Enter the inches of rainfall for month 7: 2
Enter the inches of rainfall for month 8: 3
Enter the inches of rainfall for month 9: 4
Enter the inches of rainfall for month 10: 2
Enter the inches of rainfall for month 11: 2
Enter the inches of rainfall for month 12: 3

--- Year 3 ---
Enter the inches of rainfall for month 1: 6.5
Enter the inches of rainfall for month 2: 5.5
Enter the inches of rainfall for month 3: 5
Enter the inches of rainfall for month 4: 4
Enter the inches of rainfall for month 5: 8
Enter the inches of rainfall for month 6: 7
Enter the inches of rainfall for month 7: 7
Enter the inches of rainfall for month 8: 3
Enter the inches of rainfall for month 9: 2
Enter the inches of rainfall for month 10: 4
Enter the inches of rainfall for month 11: 2
Enter the inches of rainfall for month 12: 1.5

=== Rainfall Summary ===
Total number of months: 36
Total inches of rainfall: 125.50
Average rainfall per month: 3.49 inches
