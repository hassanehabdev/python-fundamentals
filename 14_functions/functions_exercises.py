
# Python Functions Exercises
# Lessons 24–27
#
# This file contains reviewed solutions for:
# - Lesson 24: Functions Part 1
# - Lesson 25: Functions Part 2
# - Lesson 26: Functions Part 3
# - Lesson 27: Global Variables (output tracing)
#
# Each exercise is kept in its lesson order. Run individual sections
# when practicing, especially exercises that request user input.

# ============================================================
# Lesson 24 – Functions Part 1
# ============================================================

# Exercise 1: Define and call a function that prints a message.

def gamma_tech():
    print("hello gammal tech")


gamma_tech()


# Exercise 2: Print "done", then call the function.

def gamma_tech():
    print("hello gammal tech")


print("done")
gamma_tech()


# Exercise 3: Call a function three times using a loop.

def gamma_tech():
    print("hello gammal tech")


for i in range(3):
    gamma_tech()


# Exercise 4: Print a message n times using a function parameter.

def gamma_tech(n):
    for i in range(n):
        print("hello gammal tech")


gamma_tech(3)


# Exercise 5: Get a number from the user and use it as the argument.

def gamma_tech(n):
    for i in range(n):
        print("hello gammal tech")


num = int(input("Enter the num: "))
gamma_tech(num)


# Exercise 6: Print a message |n| times.

def gamma_tech(n):
    for i in range(abs(n)):
        print("hello gammal tech")


gamma_tech(-3)


# Exercise 7: Print "hello" if x > 3; otherwise, print "hi", n times.

def gamma_tech(n, x):
    if x > 3:
        for i in range(n):
            print("hello")
    else:
        for i in range(n):
            print("hi")


x = int(input("Enter the number: "))
gamma_tech(3, x)


# Exercise 8: Return the sum of two numbers.

def add_numbers(num1, num2):
    return num1 + num2


result = add_numbers(5, 3)
print("Sum:", result)


# Exercise 9: Return the product of two numbers.

def multiply_numbers(num1, num2):
    return num1 * num2


product = multiply_numbers(3, 5)
print("Product:", product)


# Exercise 10: Get a name from the user and print a greeting.

def greet(name):
    print(f"Hello, {name}! Welcome.")


name = input("Enter your name: ")
greet(name)


# ============================================================
# Lesson 25 – Functions Part 2
# ============================================================

# Exercise 1: Accept and print a variable number of arguments.

def gammal_tech(*x):
    for n in x:
        print(n)


gammal_tech(5, 6, 7)


# Exercise 2: Print the type of each argument.

def gammal_tech(*x):
    for n in x:
        print(type(n))


gammal_tech(5, 6.6, "str")


# Exercise 3: Determine whether each argument is even or odd.

def gammal_tech(*x):
    for n in x:
        if n % 2 == 0:
            print("even")
        else:
            print("odd")


gammal_tech(5, 6, 7)


# Exercise 4: Read space-separated numbers and pass them as arguments.

def gammal_tech(*x):
    for n in x:
        if n % 2 == 0:
            print("even")
        else:
            print("odd")


user_input = input("Enter a series of numbers separated by spaces: ")
numbers = [int(num) for num in user_input.split()]
gammal_tech(*numbers)


# Exercise 5: Accept one tuple and print each of its elements.

def gammal_tech(x):
    for n in x:
        print(n)


y = (5, 6, 7, 8)
gammal_tech(y)


# Exercise 6: Calculate the sum of a member's grades.
# If no grades are provided, the total is 0.

def gammal_tech(member_name, *member_grades):
    if len(member_grades) != 0:
        total = sum(member_grades)
    else:
        total = 0

    print(member_name, total)


gammal_tech("Wael", 50, 75, 100)


# Exercise 7: Calculate the average of a member's grades.
# If no grades are provided, the average is 0.

def gammal_tech(member_name, *member_grades):
    if len(member_grades) != 0:
        avg = sum(member_grades) / len(member_grades)
    else:
        avg = 0

    print(member_name, avg)


gammal_tech("Wael", 50, 75, 100)


# Exercise 8: Calculate and return the area of a rectangle.

def calculate_area(width, height):
    return width * height


area = calculate_area(5, 10)
print("Area:", area)


# Exercise 9: Return True if a number is even; otherwise, return False.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


result = is_even(7)
print("Is 7 even?", result)


# Exercise 10: Accept a list and return its maximum number.

def find_max(numbers):
    max_num = max(numbers)
    return max_num


numbers = [10, 20, 5, 30, 15]
max_number = find_max(numbers)
print("Maximum number:", max_number)


# ============================================================
# Lesson 26 – Functions Part 3
# ============================================================

# Exercise 1: Return the sum of two numbers.

def add_numbers(num1, num2):
    return num1 + num2


result = add_numbers(5, 3)
print("Result:", result)


# Exercise 2: Return the product of two numbers.

def multiply_numbers(num1, num2):
    return num1 * num2


result = multiply_numbers(5, 3)
print("Result:", result)


# Exercise 3: Return the result of raising a base to an exponent.

def calculate_power(base, exponent):
    return base ** exponent


result = calculate_power(2, 3)
print("Result:", result)


# Exercise 4: Return True if a number is even; otherwise, return False.

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


result = is_even(5)
print("Result:", result)


# Exercise 5: Calculate and return the factorial of a number.

def calculate_factorial(num):
    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    return factorial


result = calculate_factorial(5)
print("Result:", result)


# Exercise 6: Return a string in reverse order.

def reverse_string(text):
    reversed_string = ""

    for i in range(len(text) - 1, -1, -1):
        reversed_string += text[i]

    return reversed_string


result = reverse_string("hello")
print("Result:", result)


# Exercise 7: Count and return the vowels in a string.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count


result = count_vowels("hello")
print("Result:", result)


# Exercise 8: Calculate and return the average of a list of numbers.

def calculate_average(numbers):
    return sum(numbers) / len(numbers)


result = calculate_average([1, 2, 3, 4, 5])
print("Result:", result)


# Exercise 9: Return the sum of the squares of a list of numbers.

def sum_of_squares(numbers):
    total = 0

    for num in numbers:
        total += num ** 2

    return total


result = sum_of_squares([1, 2, 3, 4, 5])
print("Result:", result)


# Exercise 10: Return one list containing the elements of both lists.

def merge_lists(list1, list2):
    return list1 + list2


result = merge_lists([1, 2, 3], [4, 5, 6])
print("Result:", result)


# ============================================================
# Lesson 27 – Global Variables (Output Tracing)
# ============================================================

# Exercise 1: Trace access to a global variable inside and outside a function.
#
# Expected output:
# The value of num inside function: 15
# The value of num outside function: 15

num = 15


def display():
    print("The value of num inside function:", num)


display()
print("The value of num outside function:", num)


# Exercise 2: Trace a local variable that has the same name as a global variable.
#
# Expected output:
# Inside function: 5
# Outside function: 10

x = 10


def shadow():
    x = 5
    print("Inside function:", x)


shadow()
print("Outside function:", x)


# Exercise 3: Use global to modify a global variable.
#
# Expected output:
# 1

count = 0


def increment():
    global count
    count += 1


increment()
print(count)


# Exercise 4: Call a function twice to increment a global counter.
#
# Expected output:
# Counter: 2

counter = 0


def increment_counter():
    global counter
    counter += 1


# Test the function
increment_counter()
increment_counter()
print("Counter:", counter)


# Exercise 5: Add values to a global total.
#
# Expected output:
# Total: 12

total = 0


def add_to_total(number):
    global total
    total += number


# Test the function
add_to_total(5)
add_to_total(7)
print("Total:", total)


# Exercise 6: Add text to a global string.
#
# Expected output:
# Message: Hello, World!

message = ""


def add_to_message(new_text):
    global message
    message += new_text


# Test the function
add_to_message("Hello, ")
add_to_message("World!")
print("Message:", message)


# Exercise 7: Add names to a global list.
#
# Expected output:
# Names: ['Alice', 'Bob']

names = []


def add_name(new_name):
    global names
    names.append(new_name)


# Test the function
add_name("Alice")
add_name("Bob")
print("Names:", names)


# Exercise 8: Update a global dictionary.
#
# Expected output:
# Config: {'name': 'John', 'age': 30}

config = {}


def update_config(key, value):
    global config
    config[key] = value


# Test the function
update_config("name", "John")
update_config("age", 30)
print("Config:", config)


# Exercise 9: Add students to a global set.
#
# Expected contents:
# Students: {'Alice', 'Bob'}
# Note: The order of set elements may vary.

students = set()


def add_student(new_student):
    global students
    students.add(new_student)


# Test the function
add_student("Alice")
add_student("Bob")
print("Students:", students)


# Exercise 10: Add product IDs to a global set.
#
# Expected contents:
# Product IDs: {101, 102}
# Note: The order of set elements may vary.

product_ids = set()


def add_product_id(new_id):
    global product_ids
    product_ids.add(new_id)


# Test the function
add_product_id(101)
add_product_id(102)
print("Product IDs:", product_ids)
