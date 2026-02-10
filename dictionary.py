# 1. Word Frequency with Sorting
sentence = input("Enter a sentence:")
words = sentence.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1
sorted_freq = dict(sorted(freq.items(), key = lambda item : item[1], reverse = True))
print(sorted_freq)

# 2. Student Grade Report
students = {
    "Aman": 76,
    "Neha": 88,
    "Rohit": 69,
    "Pooja": 91,
    "Vikram": 80
}
total_marks = sum(students.values())
average_marks = total_marks / len(students)
print("Average Marks:", average_marks)
print("Students scoring above average:")
for name in students:
    if students[name] > average_marks:
        print(name)

# 3. Combine Dictionaries with Conditions
dict1 = {'a': 50, 'b': 30, 'c': 70}
dict2 = {'b': 60, 'c': 65, 'd': 40}
result = dict1.copy()
for key, value in dict2.items():
    if key in result:
        result[key] = max(result[key], value)
    else:
        result[key] = value
print(result)

# 4. Find key with Maximum Length Value
data = {'name': 'Alice', 'city': 'Bangalore', 'course': 'Data Science'}
max_key = max(data, key=lambda k: len(data[k]))
print(max_key)

# 5. Filter Dictionary by Value Range
data = {'a': 5, 'b': 15,'c': 30,'d': 55,'e': 50}
filtered_dict = {k: v for k, v in data.items() if 10 <= v <= 50}
print(filtered_dict)

# 6. Dictionary-Based Voting System
votes = {}
n = int(input("Enter number of voters: "))
for i in range(n):
    candidate = input("Enter candidate name: ")
    votes[candidate] = votes.get(candidate, 0) + 1
print("\nVote Count:")
for candidate, count in votes.items():
    print(candidate, ":", count)
winner = max(votes, key=votes.get)
print("\nWinner:", winner)

# 7. Replace Values Using Another Dictionary
data = {'a': 10, 'b': 20, 'c': 30}
update = {'b': 200, 'c': 300}
for key in data:
    if key in update:
        data[key] = update[key]
print(data)