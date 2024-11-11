# def great():
#     print("Good Morning")
#
# great()

# def greet_with_name(name):
#     print(f"Good Morning {name}")
#     print(f"How do you do {name}")
#
# greet_with_name("Angela")
# greet_with_name("Ishfaq")

# def life_in_weeks(current_age):
#     lifespan = 90
#     weeks_left = (lifespan - current_age) * 52
#     # Output the result in the correct format using f-string
#     print(f"You have {weeks_left} weeks left.")
# life_in_weeks(45)

# def greet(name, location):
#     print(f"your name is {name} and your location is {location}")
# greet("Ishfaq",  "khuzdar")

# def calculate_love_score(name1, name2):
#     combined_name = (name1 + name2).lower()
#     true_count = combined_name.count("t"), combined_name.count("r"), combined_name.count("u"), combined_name.count("e")
#     love_count = combined_name.count("l"), combined_name.count("o"), combined_name.count("v"), combined_name.count("e")
#
#     love_score = int(f"{true_count}{love_count})"
#     print(love_score)
#
# calculate_love_score("ishfaq", "suman")

def calculate_love_score(name1, name2):
    # Convert both names to lowercase to make the counting case-insensitive
    combined_names = (name1 + name2).lower()

    # Count occurrences of the letters in "TRUE"
    true_count = combined_names.count('t') + combined_names.count('r') + combined_names.count(
        'u') + combined_names.count('e')

    # Count occurrences of the letters in "LOVE"
    love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count(
        'v') + combined_names.count('e')

    # Combine the counts to form a two-digit number
    love_score = int(f"{true_count}{love_count}")

    # Print the result
    print(love_score)


# Example usage
calculate_love_score("ishfaq", "suman")
