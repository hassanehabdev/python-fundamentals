
# ============================================================
# Section 4: Working with Strings
# Lessons 17–21 | Python Fundamentals
# ============================================================


# ============================================================
# Lesson 17: Strings Part 1
# ============================================================

# Exercise 1: Concatenate the first name and last name

first_name = input("Enter your first name:")
last_name = input("Enter your last name:")

full_name = first_name + " " + last_name

print("Full name:", full_name)


# Exercise 2: Repeat a string three times

repeated_string = "Gammal Tech " * 3

print("Result:", repeated_string)


# Exercise 3: Print the first character of a string

full_name = "Gammal Tech"

print("First character:", full_name[0])


# Exercise 4: Print the last character of a string

full_name = "Gammal Tech"

print("Last character:", full_name[-1])


# Exercise 5: Extract a substring using slicing

full_name = "Gammal Tech"

print("Substring:", full_name[0:6])


# Exercise 6: Calculate the length of a string

full_name = "Gammal Tech"

print("Length of the string:", len(full_name))


# Exercise 7: Use string formatting to print a message

full_name = "Gammal Tech"

print("I l@ike %s" % full_name)


# Exercise 8: Take the user's name and age and print them

full_name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("My name is %s" % full_name)
print("My age is %d" % age)


# Exercise 9: Print escape characters as literal text

print("\\n\\t\\t")


# Exercise 10: Check if a substring exists in a string

full_name = input("Enter the name: ")

substring = "al Te"

print("'al Te' is present in the entered name:", substring in full_name)


# ============================================================
# Lesson 18: Strings Part 2
# ============================================================

# Exercise 1: Count occurrences of the character 'a'

full_name = "Gammal Tech"

count_a = full_name.count("a")

print("Number of occurrences of 'a':", count_a)


# Exercise 2: Find the index of the first occurrence of 'a'

full_name = "Gammal Tech"

print("Index of 'a':", full_name.index("a"))


# Exercise 3: Find the index of the second occurrence of 'a'

full_name = "Gammal Tech"

print(
    "Index of second occurrence of 'a':",
    full_name.index("a", full_name.index("a") + 1)
)


# Exercise 4: Check if the digit '1' is present in a name

name = input("Enter a name: ")

if "1" in name:
    print("found")
else:
    print("not found")


# Exercise 5: Count occurrences of 'a' if present in a name

name = input("Enter a name: ")

if "a" in name:
    print("The number of occurrences of 'a':", name.count("a"))
else:
    print("not found")


# Exercise 6: Find the index of the substring 'Tech'

full_name = "Gammal Tech"

print("Index of 'Tech':", full_name.index("Tech"))


# Exercise 7: Find the index of the last occurrence of 'a'

full_name = "Gammal Tech"

print("Index of last 'a':", full_name.rfind("a"))


# Exercise 8: Find a substring within a specified range

full_name = "Gammal Tech"

print(
    "Index of 'al' between indices 4 and 10:",
    full_name.find("al", 4, 11)
)


# Exercise 9: Split a string based on spaces

phrase = input("Enter a string: ")

phrase_list = phrase.split(" ")

print(phrase_list)


# Exercise 10: Split a string into separate lines

my_string = "C\nCPP\nOOP"

my_list = my_string.splitlines()

print(my_list)


# ============================================================
# Lesson 19: Translate
# ============================================================

# Exercise 1: Replace a specific substring

string1 = "Gammal Tech HTML course is available now"

string2 = string1.replace("HTML", "Python")

print(string2)


# Exercise 2: Replace a substring with user-provided text

string1 = "Gammal Tech HTML course is available now"

replacement = input("Enter the replacement word: ")

string2 = string1.replace("HTML", replacement)

print(string2)


# Exercise 3: Replace all occurrences of 'a' with '%'

string1 = "Gammal Tech HTML course is available now"

translation_table = str.maketrans("a", "%")

string2 = string1.translate(translation_table)

print("Original string:", string1)
print("Modified string:", string2)


# Exercise 4: Replace a user-specified character with '%'

string1 = "Gammal Tech HTML course is available now"

character = input("Enter the character: ")

translation_table = str.maketrans(character, "%")

string2 = string1.translate(translation_table)

print("Original string:", string1)
print("Modified string:", string2)


# Exercise 5: Translate 'a' to '*' and 'G' to '-'

string1 = "Gammal Tech HTML course is available now"

translation_table = str.maketrans("aG", "*-")

string2 = string1.translate(translation_table)

print("Original string:", string1)
print("Translated string:", string2)


# Exercise 6: Translate 'a' to '&*#'

string1 = "Gammal Tech HTML course is available now"

translation_table = str.maketrans({"a": "&*#"})

string2 = string1.translate(translation_table)

print("Original string:", string1)
print("Translated string:", string2)


# Exercise 7: Translate 'a' to a user-specified character or string

string1 = "Gammal Tech HTML course is available now"

replacement = input("Enter the character or string to replace 'a': ")

translation_table = str.maketrans({"a": replacement})

string2 = string1.translate(translation_table)

print("Original string:", string1)
print("Translated string:", string2)


# Exercise 8: Convert all uppercase letters to lowercase

string1 = "GAMMAL TECH"

translation_table = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz"
)

string2 = string1.translate(translation_table)

print("Original string:", string1)
print("Translated string:", string2)


# Exercise 9: Remove digits from a string

string1 = "GammalTech123"

translation_table = str.maketrans("", "", "0123456789")

string2 = string1.translate(translation_table)

print("Original string:", string1)
print("Translated string:", string2)


# Exercise 10: Replace a specified character with another character

string1 = "Gammal Tech HTML course is available now"

char_to_replace = input("Enter character to replace: ")

replacement_char = input("Enter the replacement character: ")

translation_table = str.maketrans(char_to_replace, replacement_char)

string2 = string1.translate(translation_table)

print("Original string:", string1)
print("Translated string:", string2)


# ============================================================
# Lesson 20: Strip and String Methods
# ============================================================

# Exercise 1: Convert all characters to uppercase

s = "Gammal Tech PYTHON course is available now"

uppercase_string = s.upper()

print("Original string:", s)
print("Uppercase string:", uppercase_string)


# Exercise 2: Convert all characters to lowercase

s = "Gammal Tech PYTHON course is available now"

lowercase_string = s.lower()

print("Original string:", s)
print("Lowercase string:", lowercase_string)


# Exercise 3: Choose between uppercase, lowercase, or unchanged

s = "Gammal Tech PYTHON course is available now"

print("1- Convert to uppercase")
print("2- Convert to lowercase")
print("3- Leave unchanged")

user_selection = int(input("Enter the number: "))

if user_selection == 1:
    converted_string = s.upper()
    print("Uppercase:", converted_string)
elif user_selection == 2:
    converted_string = s.lower()
    print("Lowercase:", converted_string)
elif user_selection == 3:
    print("Original string:", s)
else:
    print("Invalid selection")


# Exercise 4: Convert all characters to titlecase

s = "Gammal Tech PYTHON course is available now"

titlecase_string = s.title()

print(titlecase_string)
print("-----")
print(s)


# Exercise 5: Capitalize the first character of a string

user_string = input("Enter a string: ")

capitalized_string = user_string.capitalize()

print("Capitalized string:", capitalized_string)


# Exercise 6: Join characters using a specified delimiter

s = input("Enter a string: ")
delimiter = input("Enter a delimiter: ")

joined_string = delimiter.join(s)

print("Joined string:", joined_string)


# Exercise 7: Center a string within a specified width

s = input("Enter a string: ")
width = int(input("Enter the width: "))

centered_string = s.center(width)

print("Centered string:", centered_string)


# Exercise 8: Center a string using a specified fill character

s = input("Enter a string: ")
width = int(input("Enter the width: "))
fill_character = input("Enter the fill character: ")

centered_string = s.center(width, fill_character)

print("Centered string:", centered_string)


# Exercise 9: Expand tabs within a string

s = input("Enter a string containing tabs: ")
tab_size = int(input("Enter the tab size: "))

expanded_string = s.expandtabs(tab_size)

print("Expanded string:", expanded_string)


# Exercise 10: Remove leading and trailing asterisks

s = "**********GammalTech**********"

stripped_string = s.strip("*")

print("Stripped string:", stripped_string)


# ============================================================
# Lesson 21: Startswith and String Testing Methods
# ============================================================

# Exercise 1: Check if a string starts with a specific prefix

s = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")

if s.startswith(prefix):
    print("The string starts with the prefix")
else:
    print("The string doesn't start with the prefix")


# Exercise 2: Check if a string starts with a prefix from a specific index

s = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
start_index = int(input("Enter the index to start checking from: "))

if s.startswith(prefix, start_index):
    print("The string starts with the prefix from the specified index")
else:
    print("The string doesn't start with the prefix from the specified index")


# Exercise 3: Check if a string starts with any prefix in a tuple

s = "Gammal Tech"

prefixes = ("Gammal", "gammal")

if s.startswith(prefixes):
    print("The string starts with one of the prefixes in the tuple.")
else:
    print("The string doesn't start with one of the prefixes in the tuple.")


# Exercise 4: Check a prefix without considering letter case

s = "GaMmAl Tech"

if s.lower().startswith("gammal"):
    print("The string starts with the prefix 'gammal' (case insensitive).")
else:
    print("The string doesn't start with the prefix 'gammal' (case insensitive).")


# Exercise 5: Check a suffix without considering letter case

s = "GaMmAl Tech"

if s.lower().endswith("tech"):
    print("The string ends with the suffix 'tech' (case insensitive).")
else:
    print("The string doesn't end with the suffix 'tech' (case insensitive).")


# Exercise 6: Check if a string consists entirely of alphabetic characters

s = "GaMmA 56l Tech"

if s.isalpha():
    print("The string consists entirely of alphabetic characters.")
else:
    print("The string contains non-alphabetic characters.")


# Exercise 7: Check if a string consists entirely of numeric characters

s = "01033998844"

if s.isnumeric():
    print("The string consists entirely of numeric characters.")
else:
    print("The string contains non-numeric characters.")


# Exercise 8: Check if a string consists entirely of alphanumeric characters

s = "01033GAMMAL998844"

if s.isalnum():
    print("The string consists entirely of alphanumeric characters.")
else:
    print("The string contains non-alphanumeric characters.")


# Exercise 9: Check if all cased characters in a string are uppercase

s = "01033GAMMAL998844"

if s.isupper():
    print("All characters in the string are uppercase.")
else:
    print("Not all characters in the string are uppercase.")
