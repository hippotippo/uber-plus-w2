def calculate_tax(filing_status, taxable_income):
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

def get_total_income_from_w2s(number_of_w2s):
    total_income = 0
    for i in range(number_of_w2s):
        income = float(input(f"Enter the income from W-2 form {i+1}: "))
        total_income += income
    return total_income

# Main function to prompt user input
def main():
    print("Enter your filing status:")
    print("1: Single")
    print("2: Head of Household")
    print("3: Married Filing Jointly")
    print("4: Married Filing Separately")
    filing_status = int(input("Choose (1-4): "))

    number_of_w2s = int(input("How many W-2 forms do you need to enter? "))
    income_from_w2s = get_total_income_from_w2s(number_of_w2s)

    side_hustle_income = float(input("Enter your total income from side hustles: "))
    total_income = income_from_w2s + side_hustle_income

    tax_owed = calculate_tax(filing_status, total_income)
    print(f"Total taxable income: {total_income}")
    print(f"Tax owed for filing status {filing_status} with a taxable income of {total_income}: {tax_owed}")


main()