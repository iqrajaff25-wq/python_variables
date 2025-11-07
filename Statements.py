# If-Else Statements

var = int(input("Enter the number : "))
if var == 10:
    print("Code Entered")
else:
    print("Enter the correct code!")


#Calculate Discount
price = int(input("Enter the Total Price: "))
dis1 = price * 0.10
price1 = price - dis1
dis2 = price * 0.20
price2 = price - dis2
dis3 = price * 0.30
price3 = price - dis3
final_price = price * 0.50
coupon = int(input("Enter the coupon code: "))
if coupon <= 9230:
    print("Invalid Number Entered")
elif coupon <= 9250 and coupon >= 9230:
    print("10% discount is allowed")
    print(f"Payable Amount with 10% Discount = {price1}")
    
elif coupon >= 9250 and coupon <= 9270:
    print("20% discount is allowed")
    print(f"Payable Amount with 20% Discount = {price2}")

elif coupon >= 9270 and coupon <= 9290:
    print("30% discount is allowed")
    print(f"Payable Amount with 30% Discount = {price3}")
else:
    print("50% dicount allowed")
    print(f"Payable Amount with 50% Discount = {final_price}")