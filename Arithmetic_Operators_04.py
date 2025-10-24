#Assignment#01

total_members = int(input("Enter Total Famil Members "))

#Income Detail
father_income = int(input("Enter father_income "))
mother_income = int(input("Enter mother_income "))
side_business_income = int(input("Enter side_business_income "))
other_income = int(input("Enter other_income "))
total_income = father_income + mother_income + side_business_income + other_income
print(f"Total Income = {total_income}")

#Expenses Detail
house_rent = int(input("Enter house_rent "))
utilities = int(input("Enter utilities "))
groceries = int(input("Enter groceries "))
transport = int(input("Enter transport "))
education = int(input("Enter education "))
entertainment = int(input("Enter entertainment "))
miscellaneous = int(input("Enter miscellaneous "))
total_expenses = house_rent + utilities + groceries + transport + education + entertainment + miscellaneous
print(f"Total Expenses = {total_expenses}")


#Requirements:
total_savings = total_income-total_expenses
print(f"Total Savings = {total_savings}")
average_income_per_member = total_income / total_members
print(f"Average Income Per Member = {average_income_per_member}")
average_expense_per_member = total_expenses / total_members
print(f"Average Expense Per Member = {average_expense_per_member}")
saving_per_member = total_savings / total_members
print(f"Saving Per Member = {saving_per_member}")
percentage_of_saving = total_savings / total_income * 100
print(f"Percentage of Savings = {percentage_of_saving}")
