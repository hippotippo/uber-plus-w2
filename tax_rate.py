def calculate_tax(filing_status, taxable_income, total_deductions, child_credits):
    taxable_income -= total_deductions
    taxable_income = max(0, taxable_income)
    if filing_status == 1:  # Single
        return calculate_single_tax(taxable_income)
    elif filing_status == 2:  # Head of Household
        return calculate_head_of_household_tax(taxable_income)
    elif filing_status == 3:  # Married Filing Jointly
        return calculate_married_filing_jointly_tax(taxable_income)
    elif filing_status == 4:  # Married Filing Separately
        return calculate_married_filing_separately_tax(taxable_income)
    else:
        return "Invalid filing status"

def calculate_single_tax(income):
    if income <= 11000:
        return income * 0.10
    elif income <= 44725:
        return 1100 + (income - 11000) * 0.12
    elif income <= 95375:
        return 5147 + (income - 44725) * 0.22
    elif income <= 182100:
        return 16290 + (income - 95375) * 0.24
    elif income <= 231250:
        return 37104 + (income - 182100) * 0.32
    elif income <= 578125:
        return 52832 + (income - 231250) * 0.35
    else:
        return 174238.25 + (income - 578125) * 0.37

def calculate_head_of_household_tax(income):
    if income <= 15700:
        return income * 0.10
    elif income <= 59850:
        return 1570 + (income - 15700) * 0.12
    elif income <= 95350:
        return 6868 + (income - 59850) * 0.22
    elif income <= 182100:
        return 14678 + (income - 95350) * 0.24
    elif income <= 231250:
        return 35498 + (income - 182100) * 0.32
    elif income <= 578100:
        return 51226 + (income - 231250) * 0.35
    else:
        return 172623.50 + (income - 578100) * 0.37

def calculate_married_filing_jointly_tax(income):
    if income <= 22000:
        return income * 0.10
    elif income <= 89450:
        return 2200 + (income - 22000) * 0.12
    elif income <= 190750:
        return 10294 + (income - 89450) * 0.22
    elif income <= 364200:
        return 32580 + (income - 190750) * 0.24
    elif income <= 462500:
        return 74208 + (income - 364200) * 0.32
    elif income <= 693750:
        return 105664 + (income - 462500) * 0.35
    else:
        return 186601.50 + (income - 693750) * 0.37
    
def calculate_married_filing_separately_tax(income):
    if income <= 11000:
        return income * 0.10
    elif income <= 44725:
        return 1100 + (income - 11000) * 0.12
    elif income <= 95375:
        return 5147 + (income - 44725) * 0.22
    elif income <= 182100:
        return 16290 + (income - 95375) * 0.24
    elif income <= 231250:
        return 37104 + (income - 182100) * 0.32
    elif income <= 346875:
        return 52832 + (income - 231250) * 0.35
    else:
        return 93300.75 + (income - 346875) * 0.37

def get_standard_deduction(filing_status):
    if filing_status == 1:  # Single
        return 13850
    elif filing_status == 2:  # Head of Household
        return 20800
    elif filing_status == 3:  # Married Filing Jointly
        return 27700
    elif filing_status == 4:  # Married Filing Separately
        return 13850

def get_child_tax_credit(number_of_children, number_of_teens, filing_status):
    credit_per_child = 2000
    credit_per_teen = 1600
    income_limit = 400000 if filing_status == 3 else 200000
    # Modify this as per the actual income limits and calculation rules
    return (number_of_children * credit_per_child) + (number_of_teens * credit_per_teen)

def get_total_income_from_w2s(number_of_w2s):
    total_income = 0
    for i in range(number_of_w2s):
        income = float(input(f"Enter the income from W-2 form {i+1}: "))
        total_income += income
    return total_income

def calculate_side_hustle_tax(net_income, filing_status):
    # This function calculates the tax on side hustle income based on the filing status and net income
    # Assuming the side hustle income is added on top of other income
    return calculate_tax(filing_status, net_income, 0, 0)  # No additional deductions or credits for this part


def main():
    print("Enter your filing status:")
    print("1: Single")
    print("2: Head of Household")
    print("3: Married Filing Jointly")
    print("4: Married Filing Separately")
    filing_status = int(input("Choose (1-4): "))

    number_of_w2s = int(input("How many W-2 forms do you need to enter? "))
    income_from_w2s = get_total_income_from_w2s(number_of_w2s)

    itemize = input("Do you plan to itemize deductions? (yes/no): ").lower().strip() == "yes"
    total_deductions = 0
    if itemize:
        total_deductions = float(input("Enter the total of your itemized deductions: "))
    else:
        total_deductions = get_standard_deduction(filing_status)
    
       # Child tax credits
    number_of_children = int(input("Enter the number of qualifying children under 16: "))
    number_of_teens = int(input("Enter the number of qualifying children between 16 and 23: "))
    child_credits = get_child_tax_credit(number_of_children, number_of_teens, filing_status)

    side_hustle_gross_income = int(input("Enter your total gross income from side hustles: "))
    side_hustle_expenses = int(input("Enter your total expenses from side hustles: "))
    side_hustle_net_income = side_hustle_gross_income - side_hustle_expenses
    total_income = income_from_w2s + side_hustle_net_income

    # Calculate the total tax with and without the side hustle income
    total_tax_with_side_hustle = calculate_tax(filing_status, total_income, total_deductions, child_credits)
    total_tax_without_side_hustle = calculate_tax(filing_status, income_from_w2s, total_deductions, child_credits)

    # The side hustle tax is the difference between these two amounts
    side_hustle_tax = total_tax_with_side_hustle - total_tax_without_side_hustle


    

 

    tax_owed = calculate_tax(filing_status, total_income, total_deductions, child_credits)
    print(f"Total taxable income: {total_income}")
    print(f"Total deductions: {total_deductions}")
    print(f"Total child tax credits: {child_credits}")
    print(f"Tax owed after deductions and credits: {tax_owed:.2f}")
    print(f"Side hustle tax for 2023: {side_hustle_tax:.2f}")
    quarterly_taxes_2024 = (side_hustle_tax)/4
    print(f"2024 Quarterly Taxes Estimate: \033[95m{quarterly_taxes_2024:.2f}\033[0m")
    if side_hustle_tax > 1000:
        print("\033[1mImmediate penalty applicable if above $1000 for the year. Estimated quarterly payments should be submitted.\033[0m")

# Some of the formatiing above looks weird .2f makes sure the money comes out in two digits and the /033 is for colors for things to stand out

if __name__ == "__main__":
    main()
