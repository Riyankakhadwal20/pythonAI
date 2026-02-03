#Pyhton program to print name, class, section and percentage
Name = input("Enter a name:")
Student_Class = input("Enter class:")
Section = input("Enter section:")
m1 = float(input("Enter marks of subject1:"))
m2 = float(input("Enter marks of subject2:"))
m3 = float(input("Enter marks of subject3:"))
m4 = float(input("Enter marks of subject4:"))
m5 = float(input("Enter marks of subject5:"))
Total = m1+m2+m3+m4+m5
Percentage = Total/5
print("\n__Student Result__")
print("Name:",Name)
print("Student_Class:",Student_Class)
print("Section:",Section)
print("Percentage:",Percentage)


#Input three number and return sum of them
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
c = int(input("Enter a number:"))
sum =  a+b+c
print("The sum is:",sum)


#Input a number and return square of them
num = int(input("Enter a number:"))
square = num*num
print("Square of the number is:",square)


#Take temperature in celsius as input
celsius = input("Enter temperature in Celsius:")
print("Temperature in Celsius (string):",celsius)

#Convert it into float
temp_c = float(celsius)
print("Temperature in celsius is:",temp_c)

#Calculate the equivalent temperature in fahrenheit using formula
fahrenhrit = (temp_c * 9/5) + 32
print("Temperature in Fahrenheit is:", fahrenhrit)

#Print the result in Celsius and fahrenheit
print("Temperature in Celsius is:", celsius)
print("Temperature in Fahrenheit is:", fahrenhrit)

#Program to calculate the remainder
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
quotient = a//b
remainder = a%b
print("quotient=",quotient)
print("remainder=",remainder)

#Program to calculate using the formula
P = float(input("Enter Principal amount:"))
R = float(input("Enter Rate of interest:"))
T = float(input(""))
SI = (P * R * T) / 100
print("Simple Interest is:", SI)