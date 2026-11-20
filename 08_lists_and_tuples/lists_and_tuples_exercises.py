
# ============================================================
# Section 3: Lists and Tuples
# Lessons 10–14 | Python Fundamentals
# ============================================================


# ============================================================
# Lesson 10: Lists Part 1
# ============================================================

# Exercise 1: Create a list of core programming courses
core = ["C", "C++", "Data Structure"]
print(core)


# Exercise 2: Create a list using a snake_case variable name
abdul_rahman = ["C", "C++", "Python"]
print(abdul_rahman)


# Exercise 3: Collect three course names from the user
courses = []

for _ in range(3):
    course_name = input("Enter a course name: ")
    courses.append(course_name)

print(courses)


# Exercise 4: Create and print a list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)


# Exercise 5: Access the third element in a list
fruits = ["apple", "banana", "cherry", "orange"]
print(fruits[2])


# Exercise 6: Append a new course to a list
courses = ["C", "C++", "Python"]
courses.append("JavaScript")
print(courses)



# Exercise 7: Iterate through numbers and stop when a number is greater than 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num > 5:
        break
    print(num)


# Exercise 8: Iterate through fruits and stop at Banana
fruits = ["Apple", "Orange", "Banana", "Grapes", "Mango"]

for fruit in fruits:
    if fruit == "Banana":
        break
    print(fruit)



# Exercise 9: Collect integers until a negative number is entered
numbers = []

while True:
    number = int(input("Enter an integer: "))

    if number < 0:
        break

    numbers.append(number)

print(numbers)


# Exercise 10: Collect positive integers until zero is entered
numbers = []

while True:
    number = int(input("Enter a positive integer (0 to stop): "))

    if number == 0:
        break

    if number > 0:
        numbers.append(number)
    else:
        print("Please enter a positive number.")

print(numbers)


# ============================================================
# Lesson 11: Lists Part 2
# ============================================================

# Exercise 1: Access the element at index 1
core = ["C", "C++", "Python"]
print(core[1])


# Exercise 2: Repeat a list element
course = ["Course name"] * 4
print(course)


# Exercise 3: Iterate directly through a list
course = ["C", "C++", "Python"]

for course_name in course:
    print(course_name)


# Exercise 4: Modify an element in a list
course = ["C", "C++", "Python", "Java"]
course[2] = "5"

for course_name in course:
    print(course_name)


# Exercise 5: Populate a list using indexes
core = ["", "", "", ""]

for index in range(4):
    core[index] = input("Enter a course name: ")

print(core)


# Exercise 6: Populate a list in reverse index order
core = ["", "", "", ""]

for index in range(3, -1, -1):
    core[index] = input("Enter a course name: ")

print(core)


# Exercise 7: Find the index of an element
core = ["C", "C++", "Python", "Java"]
print(core.index("C++"))


# Exercise 8: Display list elements with their positions
core = ["C", "C++", "Python"]
counter = 0

for course_name in core:
    print(counter, course_name)
    counter += 1


# Exercise 9: Access list elements using a while loop
core = ["C", "C++", "Python"]
index = 0

while index < len(core):
    print(index + 1, core[index])
    index += 1


# Exercise 10: Collect integers and classify them as even or odd
numbers = []

while True:
    number = int(input("Enter an integer (0 to stop): "))

    if number == 0:
        break

    numbers.append(number)

for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


# ============================================================
# Lesson 12: Lists Part 3
# ============================================================

# Exercise 1: Create and print a list of integer values
numbers = [98, 99, 20, 100]
print(numbers)


# Exercise 2: Calculate the sum of all list elements
numbers = [98, 99, 20, 100]
total = 0

for number in numbers:
    total += number

print(total)


# Exercise 3: Calculate the sum of all elements except the last
courses = [98, 99, 20, 100]
total = 0

for index in range(len(courses) - 1):
    total += courses[index]

print(total)


# Exercise 4: Calculate the sum of all elements except the last
# and compare the result with 400
courses = [98, 99, 20, 100]
total = 0

for index in range(len(courses) - 1):
    total += courses[index]

if total == 400:
    print("Done")
else:
    print("Try again")


# Exercise 5: Calculate the sum of the second and third elements
courses = [98, 99, 20, 100]
total = 0

for index in range(1, 3):
    total += courses[index]

if total == 400:
    print("Done")
else:
    print("Try again")


# Exercise 6: Copy a list using slicing
list1 = [1, 2, 3, 4, 5]
list2 = list1[:]

print(list1)
print(list2)


# Exercise 7: Reverse a list using slicing
list1 = [1, 2, 3, 4, 5]
reversed_list = list1[::-1]

print(reversed_list)


# Exercise 8: Create a list without the elements at indexes 1 and 2
list1 = [98, 99, 20, 100, 100]
list2 = list1[:1] + list1[3:]

print(list2)


# Exercise 9: Concatenate two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print(list3)


# Exercise 10: Collect two numbers and sort them
numbers = []

for _ in range(2):
    number = int(input("Enter a number: "))
    numbers.append(number)

numbers.sort()

print(numbers)


# ============================================================
# Lesson 13: Lists Part 4
# ============================================================

# Exercise 1: Trace the program and predict the output
# core_courses = ["C", "CPP", "Python"]
# x = "OOP"
# print(x in core_courses)
# Expected output: False


# Exercise 2: Trace the program and predict the output
# core_courses = ["C", "CPP", "Python"]
# print("CPP" in core_courses)
# Expected output: True


# Exercise 3: Trace the program and predict the output
# core_courses = ["C", "CPP", "Python"]
# if "OOP" in core_courses:
#     print(core_courses.index("OOP"))
# print("Not Found")
# Expected output: Not Found


# Exercise 4: Append OOP if it is not already present
core_courses = ["C", "CPP", "Python"]

if "OOP" not in core_courses:
    core_courses.append("OOP")

print(core_courses)


# Exercise 5: Insert OOP at index 1 if it is not present
core_courses = ["C", "CPP", "Python"]

if "OOP" in core_courses:
    print(core_courses.index("OOP"))
else:
    core_courses.insert(1, "OOP")

print(core_courses)


# Exercise 6: Remove the last element and check the new last element
core_courses = ["C", "CPP", "Python", "C"]

core_courses.pop()

last = len(core_courses)

if core_courses[last - 1] != "C":
    print("Done")
else:
    print("Found")


# Exercise 7: Find the index of the second occurrence of C
core_courses = ["C", "CPP", "Python", "C"]

print(core_courses.index("C", core_courses.index("C") + 1))


# Exercise 8: Sort courses in ascending order
core_courses = ["C", "CPP", "Python", "Algorithms", "Data Structures"]

core_courses.sort()

print(core_courses)


# Exercise 9: Sort courses in descending order
core_courses = ["C", "CPP", "Python", "Algorithms", "Data Structures"]

core_courses.sort(reverse=True)

print(core_courses)


# Exercise 10: Reverse the order of elements in a list
numbers = [9, 20, 2, 5, 3]

numbers.reverse()

print(numbers)


# ============================================================
# Lesson 14: Tuples
# ============================================================

# Exercise 1: Create and print a tuple
my_tuple = ("apple", "banana", "cherry")

print(my_tuple)


# Exercise 2: Unpack a tuple into variables
my_tuple = (10, 20, 30)

a, b, c = my_tuple

print("a:", a)
print("b:", b)
print("c:", c)


# Exercise 3: Concatenate two tuples
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")

concatenated_tuple = tuple1 + tuple2

print(concatenated_tuple)


# Exercise 4: Repeat a tuple three times
my_tuple = ("Hello", "world")

repeated_tuple = my_tuple * 3

print(repeated_tuple)


# Exercise 5: Extract elements using tuple slicing
my_tuple = (1, 2, 3, 4, 5, 6)

sliced_tuple = my_tuple[2:5]

print(sliced_tuple)


# Exercise 6: Check tuple membership
my_tuple = ("apple", "banana", "cherry", "orange")

if "banana" in my_tuple:
    print("banana is present in the tuple")
else:
    print("banana is not present in the tuple")


# Exercise 7: Find the length of a tuple
my_tuple = (10, 20, 30)

print("Length of my_tuple:", len(my_tuple))


# Exercise 8: Convert a list into a tuple
my_list = ["apple", "banana", "cherry"]

my_tuple = tuple(my_list)

print(my_tuple)


# Exercise 9: Iterate through a tuple
my_tuple = ("apple", "banana", "cherry", "orange")

for item in my_tuple:
    print(item)


# Exercise 10: Access an element using its index
my_tuple = ("apple", "banana", "cherry", "orange")

print("Element at index 2:", my_tuple[2])
