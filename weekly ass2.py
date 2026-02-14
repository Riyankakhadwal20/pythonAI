data = [
    {"name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"]},
    {"name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action", "Adventure", "Drama"]},
    {"name": "Back to the Future", "year": 1985, "duration": 114, "genres": ["Adventure", "Comedy", "Sci-Fi"]}
]
def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            else:
                print("Please enter an integer greater than or equal to 1.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
def input_something(prompt):
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        else:
            print("Input cannot be empty or whitespace only.")
print("Welcome to the Movie Manager!")
while True:
    print("\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.")
    choice = input("> ").lower()
    if choice == "a":
        name = input_something("Enter movie name: ")
        year = input_int("Enter release year: ")
        duration = input_int("Enter duration (minutes): ")
        genres = []
        print("Enter genres (at least one required).")
        while True:
            genre = input_something("Enter genre: ")
            genres.append(genre)
            more = input("Add another genre? (y/n): ").lower()
            if more == "n":
                break
        new_movie = {
            "name": name,
            "year": year,
            "duration": duration,
            "genres": genres
        }
        data.append(new_movie)
        print(f"{name} added successfully.")
    elif choice == "l":
        if len(data) == 0:
            print("No movies saved.")
        else:
            for index, movie in enumerate(data):
                print(f"{index + 1}) {movie['name']} ({movie['year']})")     
    elif choice == "s":
        if len(data) == 0:
            print("No movies saved.")
        else:
            term = input_something("Enter search term: ").lower()
            found = False
            for index, movie in enumerate(data):
                if term in movie["name"].lower():
                    print(f"{index + 1}) {movie['name']} ({movie['year']})")
                    found = True
            if not found:
                print("No matching movies found.")
    elif choice == "v":
        if len(data) == 0:
            print("No movies saved.")
        else:
            index = input_int("Enter movie index number: ")
            if 1 <= index <= len(data):
                movie = data[index - 1]
                genres_formatted = ", ".join(movie["genres"])
                print(f"\nName: {movie['name']}")
                print(f"Year: {movie['year']}")
                print(f"Duration: {movie['duration']} minutes")
                print(f"Genres: {genres_formatted}")
            else:
                print("Invalid index number.")
    elif choice == "d":
        if len(data) == 0:
            print("No movies saved.")
        else:
            index = input_int("Enter movie index number: ")
            if 1 <= index <= len(data):
                removed_movie = data.pop(index - 1)
                print(f"{removed_movie['name']} deleted successfully.")
            else:
                print("Invalid index number.")
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
