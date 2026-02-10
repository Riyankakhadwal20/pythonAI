# Create a list with 5 friends and ask user.....
friends = ["Rahul","Kunal","Ankit","Anjali","Nikita"]
print("Friends:",friends)
a = input("Enter another name:")
friends.append(a)
print("Friends list are:",friends)
b = input("Enter the most important friend name:")
friends.remove("Kunal")
friends.insert(1,b)
print(friends)

# Create a list of 10 numbers and print the list
numbers = list(range(1,11))
print("Numbers:",numbers)

# Create a list and add following.....
list = [1,10,100,3,6,8]
list.insert(3,59)
list.append(5)
print("List:",list)
print("Length of list :",len(list))

# Find all of the words in a list of strings that are less than 4 letters
words = ["cat","rat","house","python","sun","moon"]
short_words = [w for w in words if len(w) < 4]
print(short_words)


# Given numbers = range(20), produce a list containing......
numbers = range(20)
result = ['Even' if n%2 == 0 else 'Odd' for n in numbers]
print(result)

# Find all of the numbers from 1-1000 that are divisible by 7
numbers = [str(n)
for n in range(1,1001)
if n%7 == 0]
print(numbers)

# Count the numbers of spaces in a string
a = "Count the number of spaces in a string"
spaces = a.count("")
print(spaces)

# Find the common numbers in two lists
list_a = " 1 2 3 4"
list_b = " 2 3 4 5 "
common = ""
for i in list_a:
    if i in list_b  and i != " " :
        common = common + i + ""
    print("Common numbers:",common)
