
# Lesson 7: For Loops
# Exercises 1–10


# Exercise 1: Print numbers from 1 to 5

for i in range(1, 6):
    print(i)


# Exercise 2: Print numbers from 0 to 4

for i in range(0, 5):
    print(i)


# Exercise 3: Print numbers from 5 to 9

for i in range(5, 10):
    print(i)


# Exercise 4: Print numbers from 5 to 10

for i in range(5, 11):
    print(i)


# Exercise 5: Print even numbers from 1 to 10

for i in range(2, 11, 2):
    print(i)


# Exercise 6: Print odd numbers from 1 to 10

for i in range(1, 11, 2):
    print(i)


# Exercise 7: Print numbers from 5 to 1

for i in range(5, 0, -1):
    print(i)


# Exercise 8: Calculate the sum of numbers from 1 to 5

total = 0

for i in range(1, 6):
    total += i

print(total)


# Exercise 9: Calculate the factorial of a number

num = 5
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(factorial)


# Exercise 10: Calculate the sum of all even numbers from 1 to 10

total = 0

for i in range(2, 11, 2):
    total += i

print(total)
