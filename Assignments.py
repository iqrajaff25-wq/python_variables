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

#Expenses Detail
print('''
ENTER EXPENDITURE DETAILS;
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



#Assignment # 03
#  Battery Health Analyzer
#  Objective: To analyze phone battery status based on percentage and charging condition.

#  Requirements:
#  1. Ask the user for current battery percentage (0–100) and whether the phone is charging
#  (yes/no).
#  2. Use only if-else, logical, and comparison operators to print the correct message.
#  Formula:
#  Logical conditions used for decision making (e.g., If (Battery ≤ 10) and (Charging == 'no')).
#  Conditions:- Battery ≤ 10 and not charging →  Battery Critical – Plug in immediately!- 
#  Battery ≤ 10 and charging →  Charging started just in time!-
#  10 < Battery ≤ 30 and not charging → Battery Low – Consider charging soon. 
#  30 < Battery ≤ 60 and not charging →  Battery OK – Moderate usage allowed.
#  60 < Battery ≤ 90 and charging →  Battery good – you can unplug soon. 
#  Battery > 90 and charging →  Battery Full – Unplug charger to save energy. 
#  Otherwise →  Battery sufficient – all good!

battery = int(input("Enter Battery's Current Percentage! (0-100): "))
charging = input("Is the device charging? (yes/no): ").lower()
def battery_analyzer():
    if battery < 0 or battery >100:
        print("❌ Invalid Percentage Entered!")
    elif battery <= 10 and charging == "no":
        print("🔴 Battery Health is Critical. Charge immediately!")
    elif battery <=10 and charging == "yes":
        print("⚡Charging Started Just In Time")
    elif battery >10 and battery <=30 and charging == "no":
        print("🟠 Battery is low. Consider Charging Soon!")
    elif battery >10 and battery <=30 and charging == "yes":
        print("⚡ Battery chearging started just in time!")
    elif battery >30 and battery <=60 and charging == "no":
        print("🟡 Moderate usage allowed!")
    elif battery >30 and battery <= 60 and charging =="yes":
        print("⚡Battery is Sufficient, you can unplug soon!")
    elif battery >60 and battery <=90 and charging =="no":
        print("🟢 Battery sufficient")
    elif battery >60 and battery <=90 and charging == "yes":
        print("⚡Battery sufficient!")
    elif battery >90 and battery <=100 and charging == "yes":
        print("💯 Battery Full. Unplug the charger to save energy!")
    else:
        print("✅ Battery Sufficient. All Good!")

battery_analyzer()

    
    

