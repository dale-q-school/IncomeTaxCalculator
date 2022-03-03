# Variables and Input
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 3000
income = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

# Math and Output
income_tax = (income - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * dependents)) * TAX_RATE

print("The income tax is $", income_tax)