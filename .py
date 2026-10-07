#Author: James Grayer
#Program: Mod_7 - Functions
#Date: Oct, 7, 2026

def get_expenses():
    "Prompts the user to enter monthly costs for automobile expenses."
    loan = float(input("Enter monthly loan payment: $"))
    insurance = float(input("Enter monthly insurance cost: $"))
    gas = float(input("Enter monthly gas cost: $"))
    oil = float(input("Enter monthly oil cost: $"))
    tires = float(input("Enter monthly tires cost: $"))
    maintenance = float(input("Enter monthly maintenance cost: $"))
    return loan, insurance, gas, oil, tires, maintenance


def show_expenses(loan, insurance, gas, oil, tires, maintenance):
    "Calculates and displays the total monthly and annual automobile costs."
    total_monthly = loan + insurance + gas + oil + tires + maintenance
    total_annual = total_monthly * 12

    print(f"\nTotal Monthly Cost: ${total_monthly:,.2f}")
    print(f"Total Annual Cost: ${total_annual:,.2f}")


def main():
    loan, insurance, gas, oil, tires, maintenance = get_expenses()
    show_expenses(loan, insurance, gas, oil, tires, maintenance)


if __name__ == "__main__":
    main()
PS G:\Users\James\AppData\Local\Programs\Microsoft VS Code> & C:\Users\James\.local\bin\python3.14.exe "c:/Users/James/OneDrive - Laramie County Community College/COSC 1010/python/.py"
Enter monthly loan payment: $30.05
Enter monthly insurance cost: $129.99
Enter monthly gas cost: $50.00
Enter monthly oil cost: $30.00
Enter monthly tires cost: $25.00
Enter monthly maintenance cost: $20.00

Total Monthly Cost: $285.04
Total Annual Cost: $3,420.48
PS G:\Users\James\AppData\Local\Programs\Microsoft VS Code> 
