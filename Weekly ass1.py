# Q.1: Print the numbers from 1 to 50......
for i in range(1,51):
    if i%3 == 0:
        print("Fizz number:",i)
    elif i%5 == 0:
        print("Buzz number:",i)
    elif i%3 == 0 and i%5 == 0:
        print("FizzBuzz number")
    else:
        print(i)

# Q.2: Print all prime numbers between 1 to 100.....
for n in range(1,100):
    if n> 1:  
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)
    
# Q.3: To ask the user for a score between 0 and 100 and print the corresponding grade.....
score = int(input("Enter the score between 0 and 100:"))
if score >= 90 and score <= 100:
    print("Grade:A")
elif score >= 80 and score < 90:
    print("Grade:B")
elif score >= 70 and score < 80:
    print("Grade:C")
elif score >= 60 and score < 70:
    print("Grade:D")
else:
    print("Grade:F")

# Q.4: To print the multiplication table(from 1 to 10) of a given number 
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number*i)

# Q.5: To create a list of the squares of the even numbers from 1 to 20
squares =[]
for i in range(1,21):
    if i%2 == 0:
        squares.append(i**2)
        print(squares)

# Q.6: To check given year is a leap year.....
year = int(input("Enter a year:"))
if (year % 4 == 0 and year %  100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# Q.7: To take the lengths of three sides of a triangle as input and determines the type of triangle..
side1 = float(input("Enter the Length of the first side:"))
side2 = float(input("Enter the Length of the second side:"))
side3 = float(input("Enter the Length of the third side:"))
if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")

# Q.8: To take an integer input from the user and classifies it as positive, negative or zero.
number = int(input("Enter an integer:"))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Q.9: To calculates the body mass index (BMI) and categorizes it.....
weight = float(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in meters:"))
BMI = weight / (height ** 2)
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 25:
    print("You have a normal weight.")
elif 25 <= BMI < 30:
    print("You are overweight.")
else:
    print("You are obesity.")

# Q.10: To take an integer input representing a day of the week.....
day = int(input("Enter a number (1-7) representing a day of the week:"))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input.")

# Q.11: To calculates the discount on a product based on the following criteria.....
price = float(input("Enter your price:"))
if price > 1000:
    discount = price * 0.10
elif 500 <= price <= 1000:
    discount = price * 0.05
else:
    discount = 0
final_price = price - discount
print(f"Original Price: ${price:.2f}")
print(f"Discount Applied: ${discount:.2f}")
print(f"Final Price after Discount: ${final_price:.2f}")

# Q.12: To find the sum of first n natural numbers
n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("The sum of the first n natural numbers is:", sum)

# Q.13: Given a dictionary employee_details .....
employee_details = {
    101: {"name": "Alice", "department": "HR", "salary": 60000},
    102: {"name": "Bob", "department": "IT", "salary": 45000},
    103: {"name": "Charlie", "department": "Finance", "salary": 75000},
    104: {"name": "Govind", "department": "Marketing", "salary": 50000}
}
high_salary_employees = [
    details["name"]
    for details in employee_details.values()
    if details["salary"] > 50000
]
print(high_salary_employees)

# Q.14: To count the number of vowels in a given string
a = input("Enter a string:")
vowel_count = 0
vowels = "aeiouAEIOU"
for char in a:
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

# Q.15: To find the sum of the digits of a given number
number = int(input("Enter a number: "))
number = abs(number)
sum = 0
while number > 0:
    digit = number % 10        
    sum += digit     
    number //= 10           
print("Sum of digits:", sum)

# Q.16: To print a pattern of stars.....
n = 5
for i in range(1, n + 1):
    print("*" * i)

# Q.17: Program for a number guessing game....
import random
secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        break

# Q.18: To input a number and show all even numbers....
for i in range(1,15):
    if i%2 == 0:
        print(i,end =" ")

# Q.19: To perform a list of 10 numbers and perform the following.....
numbers = [10, 25, 30, 45, 25, 60, 75, 25, 90, 100]
if 25 in numbers:
    print("25 exists in the list")
else:
    print("25 does not exist in the list")
print("Total length of the list:", len(numbers))
print("Total occurrence of 25:", numbers.count(25))
print("Traversing all elements:")
for num in numbers:
    print(num)
print("Even numbers in the list:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")

# Q.20: To input a string of min 10 words and max 19 words and perform the following....
text = input("Enter a string (min 10 words and max 19 words): ")
words = text.split()
if len(words) < 10 or len(words) > 19:
    print("Please enter between 10 and 19 words.")
else:
    print("\nFull String:", text)
print("Length of String (characters):", len(text))
clean_text = text.replace(" ", "").lower()
if clean_text == clean_text[::-1]:
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")
middle_index = len(words) // 2
print("Middle word:", words[middle_index])
print("Second last word:", words[-2])

# Q.21: To perform the following task as per the output.....
print("Welcome to Calci:")
print("1. Power")
print("2. Sum")
print("3. Sub")
print("4. Multiple")
choice = int(input("Enter your choice. --> "))
if choice == 1:
    num1 = int(input("Enter base number: "))
    num2 = int(input("Enter power: "))
    result = num1 ** num2
    print("Power is", result)
elif choice == 2:
    num1 = int(input("Enter 1st Number for Sum: "))
    num2 = int(input("Enter 2nd number for SUm: "))
    result = num1 + num2
    print("Sum is", result)
elif choice == 3:
    num1 = int(input("Enter 1st Number for Sub: "))
    num2 = int(input("Enter 2nd number for Sub: "))
    result = num1 - num2
    print("Subtraction is", result)
elif choice == 4:
    num1 = int(input("Enter 1st Number for Multiple: "))
    num2 = int(input("Enter 2nd number for Multiple: "))
    result = num1 * num2
    print("Multiplication is", result)
else:
    print("Invalid choice!")

# Q.22: To count the number of strings ....
X = ['abc', 'xyz', 'aba', '1221']
count = 0
for item in X:
    if len(item) >= 2 and item[0] == item[-1]:
        count += 1
print(count)





