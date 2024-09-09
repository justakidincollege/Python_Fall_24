# Budget Breakdown Calculator Assignment

# Ask user to input information
total=float(input("Hello user I am a budget calculator.\nPlease input your total budget."))

# Asks user what information to input
print("Now please input the total amount of money spent on these categories.")

# Continue inputs
housing=float(input("Housing:"))
groceries=float(input("Groceries:"))
transportation=float(input("Transportation:"))
health_care=float(input("Health Care:"))
personal_care=float(input("Personal Care:"))
clothing=float(input("Clothing:"))
debt=float(input("Debt:"))

# Calculate percentages
housing_percent=housing/total
groceries_percent=groceries/total
transportation_percent=transportation/total
health_care_percent=health_care/total
personal_care_percent=personal_care/total
clothing_percent=clothing/total
debt_percent=debt/total

# Display results
print("Your percentages are")
print(f"{housing_percent:.2f} for housing")
print(f"{groceries_percent:.2f} for groceries")
print(f"{transportation_percent:.2f} for transportation")
print(f"{health_care_percent:.2f} for health care")
print(f"{personal_care_percent:.2f} for personal care")
print(f"{clothing_percent:.2f} for clothing")
print(f"{debt_percent:.2f} for debt")
print("I hope this was helpful.")
