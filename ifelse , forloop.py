# Question.1: To input a number and their month number
a = int(input("Enter a month(1-12):"))
if a == 1:
    print("January")
elif a == 2:
  print("February")
elif a == 3:
  print("March")
elif a == 4:
  print("April")
elif a == 5:
  print("May")
elif a == 6:
  print("June")
elif a == 7:
  print("July")
elif a == 8:
  print("August")
elif a == 9:
  print("September")
elif a == 10:
  print("October")
elif a == 11:
  print("November")
elif a == 12:
  print("December")
else:
  print("Wrong Choice")

# Question.2: To input 2 number and tell the following:
# 1. Both number are equal or not
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
if a==b:
    print("Both number are equal")
else:
    print("Numbers are not equal")

# 2. Which is bigger in both
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
if a>b:
    print("a is bigger")
else:
    print("b is bigger")

# 3. Either first number is smaller or equal to second number
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
if a <= b:
    print("a is smaller than b")
else:
    print("a is equal to b")

# 4. Print your firstname 5 times is first number is greater than second and print your surname 3 times if 1st no is less than second
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
Firstname = input("Enter your Firstname:")
Surname = input("Enter your Surname:")
if (a>b):
 for i in range(1,6):
  print("your name:",Firstname)
else:
  for i in range(1,4):
   print("your surname is:",Surname)

# Question.3: Input 2 string and tell following
# 1. using == tell both string equal or not
str1 = input("Enter first string:")
str2 = input("Enter second string:")
if(str1==str2):
  print("str1 and str2 are equal")
else:
  print("Both strings are not equal")

# 2. using is tell both string equal or not
str1 = input("Enter first string:")
str2 = input("Enter second string:")
if(str1 is str2):
  print("str1 and str2 are equal")
else:
  print("Both strings are not equal")

# Question.4: To input two string  and convert it into numbers and using is op tell both are equal or not
str1 = str(input("Enter first name:"))
str2 = str(input("Enter second name:"))
num1 = int(str1)
num2 = int(str2)
if num1 is num2:
    print("num1 and num2 are equal")
else:
    print("num1 and num2 are not equal")

# Question.5: To calculate sum of all numbers from 1 to a given number
a = int(input("Enter a number:"))
total =0
for i in range(1, a + 1):
    total = total+i
    print("the result is:",total)

#  Question.6: To input a number and tell all even number upto all number
a = int(input("Enter a number:"))
for i in range(2, a + 1, 2):
    print(i)

#  Question.7: To input a number and with + and - and perform following output 
a = int(input("Enter a number:"))
op = input("Enter OP(+,_):");
if op == '+':
    for i in range(0, a ):
        print(i, end=",")
elif op == '_':
    for i in range(a,0,-1):
        print(i,end=",")
else:
    print("Invalid opertor")