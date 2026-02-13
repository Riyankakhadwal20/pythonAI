# Railway Ticket Booking System:-
print("Welcome to CodeRai`l Railway Booking System")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Choose travel class:")
print("1. First Class")
print("2. Second Class")
print("3. Sleeper Class")
choice = input("Enter choice (1/2/3): ")
if choice == "1":
    travel_class = "First Class"
    price = 1500
elif choice == "2":
    travel_class = "Second Class"
    price = 1000
elif choice == "3":
    travel_class = "Sleeper Class"
    price = 500
else:
    print("Invalid choice! Please restart the program.")
    exit()
if age < 5:
    price = 0
elif age >= 60:
    price = price * 0.8  
meal_choice = input("Do you want to add a meal? (yes/no): ").lower()
if meal_choice == "yes":
    price += 200
    meal_added = "Yes"
else:
    meal_added = "No"
print("----- Ticket Summary -----")
print("Passenger Name:", name)
print("Age:", age)
print("Class:", travel_class)
print("Meal Added:",meal_added)
print("Final Price:", price)
print("\nEnjoy your journey!")


# Burger King:-
print("Welcome to Burger King!")
print("Menu:")
print("1. Whopper Burger - Rs.150")
print("2. Crispy Veg - Rs.100")
print("3. Chiken Wings - Rs.120")
price1 = 150
price2 = 100
price3 = 120
item = int(input("Enter the item number (1/2/3): "))
quantity = int(input("Enter quantity: "))
if item == 1:
    total = price1 * quantity
elif item == 2:
    total = price2 * quantity
elif item == 3:
    total = price3 * quantity
else:
    print("Invalid item selected!")
    total = 0
coupon_code = input("Do you have a coupon code(Yes,No):").lower()
Discount = 0
if (coupon_code == "yes"):
    coupon = input("Enter your coupon code: ").upper()
    print("Applying coupon...")
    if coupon == "KING50":
        discount = total * 0.50
        print("Discount Applied:50%")
    elif coupon == "BK20":
        discount = 20
        print("Discount Applied: ₹20")
    elif coupon == "NOCOUPON":
        discount = 0
        print("No discount applied.")
    else:
        print("Invalid coupon code! No discount applied.")
final_price = total - discount               
print("Original Price: Rs", total)
print("Final Price: Rs", final_price)
print("Thanks for ordering at Burger King!")