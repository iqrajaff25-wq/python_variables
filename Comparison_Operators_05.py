#Equal to ( == )
num1 = 20
num2 = 20
equality = num1 == num2
print(f"{num1} is equal to {num2} : {equality}")


#Not-Equal to ( != )
salary = 200000
pension = 75000
not_equal = salary != pension
print(f"{salary} is not equal to {pension} : {not_equal}")


#Greater Than ( > )
greater = salary > pension
print(f"{salary} is greater than {pension} : {greater}")


#Greater Than Equal to ( >= )
greater_equal = salary >= pension
print(f"{salary} is greater equal to {pension} : {greater_equal}")
if salary >= pension:
    print("Condition is true")
else:
    print("condition is false")


#Less Than ( < )
lesser = pension < salary
print(f"{pension} is lesser than {salary} : {lesser}")


#Lesser_than equalto ( <= )
less_equal = pension <= salary
print(f"{pension} is less than equal to {salary} : {less_equal}")


#AND Operator
age = 50
if age >= 18 and age <= 65:
    print("You are eligible for entry test")
else:
    print("You are not eligible!")
