# To find the sum of first n natural number 
n = int(input("Enter a number:"))
sum = 0
for i in range(1, n+1):
 sum = sum + i
 print(" The sum is:",sum)


# To check whether a number is prime or not
n = int(input("Enter number:"))
print(n**0.5)
if n<=1:
    print("False")
else:
    prime = True
for i in range(2,n):
    if n%i==0:
        prime = False
        print(prime)

# Check whether a number is palindrome
a = int(input("Enter a number:"))
temp = a
rev = 0
for _ in range(len(str(a))):
    digit = temp % 10
    rev = rev * 10 + digit
    temp//=10
if a == rev:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
   
# Prime numbers from 1 to 100:
# If divisible by 3 -- print Fizz
for i in range(1,100):
    if i%3 == 0:
        print("Fizz number")
    else:
        print("Not a Fizz number")    

# If divisible by 5 -- print Buzz
for i in range(1,100):
    if i%5 == 0:
        print("Buzz number")
    else:
       print("It is not a Buzz number")    


# If divisible by both -- print FizzBuzz
for i in range(1,100):
    if i%3 == 0 and i%5 == 0:
        print(" It is a FizzBuzz number")
    else:
        print("It is not a FizzBuzz number")    