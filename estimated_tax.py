def calculate_estimated_tax_2023():
    # Inputs
    adjusted_gross_income = float(input("Enter adjusted gross income you expect in 2023: "))
    itemized_deductions = float(input("Enter itemized deductions (if applicable): "))
    qualified_business_income_deduction = float(input("Enter qualified business income deduction (if applicable): "))
    tax_rate_schedule_amount = float(input("Enter the amount from the 2023 Tax Rate Schedules: "))
    alternative_minimum_tax = float(input("Enter alternative minimum tax from Form 6251 (if applicable): "))
    other_taxes = float(input("Enter any other taxes expected to include: "))
    credits = float(input("Enter credits (excluding any income tax withholding): "))
    self_employment_tax = float(input("Enter self-employment tax: "))
    refundable_credits = float(input("Enter total refundable credits (if applicable): "))
    income_tax_withheld = float(input("Enter income tax withheld and estimated to be withheld during 2023: "))
    
    # Calculations
    deductions_total = itemized_deductions + qualified_business_income_deduction
    taxable_income = adjusted_gross_income - deductions_total
    total_tax = tax_rate_schedule_amount + alternative_minimum_tax
    total_tax_after_credits = total_tax - credits
    total_2023_tax = total_tax_after_credits + self_employment_tax + other_taxes
    total_estimated_tax = total_2023_tax - refundable_credits
    required_payment_90_percent = total_estimated_tax * 0.90
    # Assuming user is not a farmer or fisherman for simplicity
    required_annual_payment = required_payment_90_percent  # or 12b if available
    tax_due_after_withholding = total_estimated_tax - income_tax_withheld

    # Initialize first_payment variable
    first_payment = 0

    # Decision making for payment
    if tax_due_after_withholding < 1000:
        print("You are not required to make estimated tax payments.")
    else:
        first_payment = tax_due_after_withholding / 4  # Assuming payments are divided equally
        print(f"First estimated tax payment due (if by April 18, 2023): {first_payment}")

    return first_payment

# Uncomment below line to run the function
calculate_estimated_tax_2023()


