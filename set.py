#  Q.1: The Guest List
Friday = {"Alice", "Bob", "Charlie"}
Saturday = {"Charlie", "David", "Eve"}
common_guest = Friday.intersection(Saturday)
print("The guest attending one night:",common_guest)
all_guests = Friday.union(Saturday)
print("The guest attending both night:",all_guests)

# Q.2: List Cleaner
data = [1,2,2,3,4,4,4,5]
new_data = set(data)
new_data.add(6)
print(new_data)

# Q.3: The Library Audit
library_books = {"Hobbit", "1984", "Gatsby", "Odyssey", "Hamlet"}
checked_out = {"1984", "Hamlet"}
available_books = library_books.difference(checked_out)
print("Available books:", available_books)
new_book = "Don Quixote"
if new_book not in library_books:
    library_books.add(new_book)
    print("Don Quixote added to library")
else:
    print("Don Quixote is already in the library")
print("Updated library collection:" , library_books)

# Q.4: Permission Checker
user_permission = {"read", "write"}
admin_reqs = {"read", "write", "execute"}
admin_access = user_permission.issuperset(admin_reqs)
print("User has admin request:",admin_access)
missing_permission = admin_reqs.difference(user_permission)
print("Missing permission:", missing_permission)

# Q.5: The Log Analyzer
logs = {
    "404" : [10,12,15,20],
    "500" : [12,20,22,25],
    "403" : [10,20,30]
}
error_404 = set(logs["404"])
error_500 = set(logs["500"])
error_403 = set(logs["403"])
error_servers = { 
    server for server in error_404 if server in error_500 and server in error_403
}
print("Servers with all errors:", error_servers)
critical_servers = error_500.difference(error_404)
print("Critical servers:", critical_servers)