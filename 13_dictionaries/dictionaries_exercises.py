
# ============================================================
# Lesson 23: Dictionaries
# ============================================================


# Exercise 1: Create and print an empty dictionary

my_dict = {}

print("Empty Dictionary:", my_dict)


# Exercise 2: Create a dictionary with key-value pairs

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("Dictionary with key-value pairs:", my_dict)


# Exercise 3: Access the value associated with the key 'age'

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("Age:", my_dict["age"])


# Exercise 4: Change the value associated with the key 'city'

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

my_dict["city"] = "Los Angeles"

print("Updated dictionary:", my_dict)


# Exercise 5: Remove the key 'city' from a dictionary

my_dict = {
    "name": "John",
    "age": 35,
    "city": "New York"
}

my_dict.pop("city")

print("Updated dictionary:", my_dict)


# Exercise 6: Check if a key exists in a dictionary

my_dict = {
    "name": "John",
    "age": 35,
    "city": "New York"
}

key_to_check = "age"

if key_to_check in my_dict:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' doesn't exist in the dictionary.")


# Exercise 7: Iterate over dictionary items and print keys and values

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "London"
}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")


# Exercise 8: Add new key-value pairs to an empty dictionary

my_dict = {}

my_dict["name"] = "John"
my_dict["age"] = 25
my_dict["city"] = "New York"

print("Updated dictionary:", my_dict)


# Exercise 9: Iterate over the keys and values of a dictionary

my_dict = {"a": 1, "b": 2, "c": 3}

for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")


# Exercise 10: Check if a user-provided key already exists

my_dict = {"a": 1, "b": 2, "c": 3}

key_to_check = input("Enter a key to check: ")

if key_to_check in my_dict:
    print(f"The key '{key_to_check}' already exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' doesn't exist in the dictionary.")
