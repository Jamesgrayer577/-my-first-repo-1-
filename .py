#Author: James Grayer
#Program: Mod_8 - Modules & Libraries
#Date: Oct, 13, 2026

import math

# Constants
FEET_PER_GALLON = 112
LABOR_HOURS_PER_GALLON = 8
LABOR_CHARGE_PER_HOUR = 35.00


def main():
  # Ask the user for inputs
  square_feet = float(
      input("Enter the square feet of wall space to be painted: ")
  )
  paint_price_per_gallon = float(
      input("Enter the price of the paint per gallon: ")
  )

  # Calculations
  # Using math.ceil to round up to the next whole gallon, or float division depending on assignment rules
  gallons_required = math.ceil(square_feet / FEET_PER_GALLON)
  labor_hours_required = gallons_required * LABOR_HOURS_PER_GALLON
  cost_of_paint = gallons_required * paint_price_per_gallon
  labor_charges = labor_hours_required * LABOR_CHARGE_PER_HOUR
  total_cost = cost_of_paint + labor_charges

  # Display the results
  print("\n--- Paint Job Estimate ---")
  print(f"Number of gallons of paint required: {gallons_required}")
  print(f"Hours of labor required: {labor_hours_required}")
  print(f"Cost of the paint: ${cost_of_paint:,.2f}")
  print(f"Labor charges: ${labor_charges:,.2f}")
  print(f"Total cost of the paint job: ${total_cost:,.2f}")


if __name__ == "__main__":
  main()

    S G:\Users\James\AppData\Local\Programs\Microsoft VS Code> & C:\Users\James\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/James/OneDrive - Laramie County Community College/COSC 1010/python/.py"
Enter the square feet of wall space to be painted: 112
Enter the price of the paint per gallon: 25.98

--- Paint Job Estimate ---
Number of gallons of paint required: 1
Hours of labor required: 8
Cost of the paint: $25.98
Labor charges: $280.00
Total cost of the paint job: $305.98
PS G:\Users\James\AppData\Local\Programs\Microsoft VS Code> 
