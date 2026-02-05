print("Welcome to Burger King!")
print("Menu")
print("1. Whopper Burger - Rs.150")
print("2. Crispy Veg - Rs.100")
print("3. Chiken Wings - Rs.120")
choice = input("The user want to order(1,2,3):")
choice1 = 2
choice2 = 4
choice3 = 6
if choice == '1':
    print("Enter quantity:",choice1)
elif choice == '2':
    print("Enter quantity:",choice2)
elif choice == '3':
    print("Enter quantity:",choice3)
else:
    print("Wrong Choice")
coupon_code = input("Do you have a coupon code(Yes,No):")
Discount = 0
print("Enter your coupon code():")
if (coupon_code == "KING50"):
    discount = "total bill * 0.5"
    print("Coupon applied: 50% OFF")
elif (coupon_code == "Bk20"):
    discount = 20
    print("coupon applied: Rs.20 OFF")
elif (coupon_code == "NOCOUPON:"):
    print(" NOVOUPON")
else:
    print("Invalid coupon code")
    print("Applying coupon....")