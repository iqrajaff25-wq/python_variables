#Assignment#01

total_members = int(input("Enter Total Family Members: "))

#Income Detail
print('''
ENTER INCOME DETAILS;
---------------------''')
father_income = int(input("Enter Father's Income: "))
mother_income = int(input("Enter Mother's Income: "))
side_business_income = int(input("Enter Side Business Income: "))
other_income = int(input("Enter Other Income: "))
total_income = father_income + mother_income + side_business_income + other_income
print(f'TOTAL INCOME = {total_income}')

# #Expenses Detail
print('''ENTER EXPENDITURE DETAILS;
------------------------''')
house_rent = int(input("Enter house rent: "))
utilities = int(input("Enter Utilities: "))
groceries = int(input("Enter Groceries: "))
transport = int(input("Enter Transport: "))
education = int(input("Enter Education: "))
entertainment = int(input("Enter Entertainment: "))
miscellaneous = int(input("Enter Miscellaneous: "))
total_expenses = house_rent + utilities + groceries + transport + education + entertainment + miscellaneous
print(f'''TOTAL EXPENSES = {total_expenses}
    ''')


print('''REQUIREMENTS:
-------------''')
total_savings = total_income-total_expenses
print(f"TOTAL SAVINGS = {total_savings}")
average_income_per_member = total_income / total_members
print(f"AVERAGE INCOME PER MEMBER = {average_income_per_member}")
average_expense_per_member = total_expenses / total_members
print(f"AVERAGE EXPENSE PER MEMBER = {average_expense_per_member}")
saving_per_member = total_savings / total_members
print(f"SAVING PER MEMBER = {saving_per_member}")
percentage_of_saving = total_savings / total_income * 100
print(f"PERCENTAGE OF SAVINGS = {percentage_of_saving}%")
