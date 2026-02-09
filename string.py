<<<<<<< HEAD
# Python program to get a string made of first 2 and last 2 chars....
str1 = "Coder"
str2 = "roots"
print("Sample String:",str1,str2)
new_str1 = str1[0] + str1[1]
new_str2 = str2[3] + str2[4]
result = new_str1 + "" + new_str2
print("Excepted result:",result)
str3 = "New"
str4 = "year"
print("Sample string:",str3,str4)
new_str1 = str3[0] + str3[1]
new_str2 = str4[2] + str4[3]
result = new_str1 + "" + new_str2
print("Excepted result:",result)
a = input("Enter a string:")
if len(a)<2:
    print("Not a valid string")
else:
    result = a[:3] + a[-1]
    print("Result:",result)


# Python program to get a single string from two given string.....
str1 = "coder"
str2 = "roots"
result = str1 + ',' + str2
print("Sample String:",result)
new_str1 = str2[0] + str1[1:]
new_str2 = str1[0] + str2[1:]
result = new_str1 + " " + new_str2
print("Excepted result:", result)


# Python program to add 'ing' at the end of a given string....
str = input("Enter a string:")
if len(str)>=3:
    if str.endswith("ing"):
        s = str + "ly"
        print("Excepted Result:",s)
    else:
        s = str + "ing"
    print("Excepted Result:",s)
else:
    print("Invalid string")
 
# Python program to remove the nth index character from a nonempty string
str = "Python"
n = 3
result = str[:n] + str[n+1:]
print("Oroginal string:",str)
=======
# Python program to get a string made of first 2 and last 2 chars....
str1 = "Coder"
str2 = "roots"
print("Sample String:",str1,str2)
new_str1 = str1[0] + str1[1]
new_str2 = str2[3] + str2[4]
result = new_str1 + "" + new_str2
print("Excepted result:",result)
str3 = "New"
str4 = "year"
print("Sample string:",str3,str4)
new_str1 = str3[0] + str3[1]
new_str2 = str4[2] + str4[3]
result = new_str1 + "" + new_str2
print("Excepted result:",result)
a = input("Enter a string:")
if len(a)<2:
    print("Not a valid string")
else:
    result = a[:3] + a[-1]
    print("Result:",result)


# Python program to get a single string from two given string.....
str1 = "coder"
str2 = "roots"
result = str1 + ',' + str2
print("Sample String:",result)
new_str1 = str2[0] + str1[1:]
new_str2 = str1[0] + str2[1:]
result = new_str1 + " " + new_str2
print("Excepted result:", result)


# Python program to add 'ing' at the end of a given string....
str = input("Enter a string:")
if len(str)>=3:
    if str.endswith("ing"):
        s = str + "ly"
        print("Excepted Result:",s)
    else:
        s = str + "ing"
    print("Excepted Result:",s)
else:
    print("Invalid string")
 
# Python program to remove the nth index character from a nonempty string
str = "Python"
n = 3
result = str[:n] + str[n+1:]
print("Oroginal string:",str)
>>>>>>> ba623225df9877f8dc3639ad567d4bf4fa6e8122
print("String after removing index",n,":",result)