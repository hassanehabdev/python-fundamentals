
# Lesson 8: While Loops
# Exercises 1–10


# Exercise 1: Count from 1 to 5 using a while loop

count = 1

while count <= 5:
    print(count)
    count += 1


# Exercise 2: Print even numbers from 2 to 10 using a while loop

num = 2

while num <= 10:
    print(num)
    num += 2


# Exercise 3: Calculate the sum of numbers from 1 to 5

num = 1
total = 0

while num <= 5:
    total += num
    num += 1

print("Sum:", total)


# Exercise 4: Print numbers from 5 to 1 using a while loop

num = 5

while num >= 1:
    print(num)
    num -= 1


# Exercise 5: Calculate the factorial of 5 using a while loop

num = 5
factorial = 1

while num >= 1:
    factorial *= num
    num -= 1

print("Factorial:", factorial)


# Exercise 6: Print numbers divisible by 3 from 1 to 10

num = 1

while num <= 10:
    if num % 3 == 0:
        print(num)
    num += 1


# Exercise 7: Print the first 5 multiples of 2

multiple = 2
count = 1

while count <= 5:
    print(multiple * count)
    count += 1


# Exercise 8: Print numbers from 1 to 10, skipping every other number

num = 1

while num <= 10:
    print(num)
    num += 2


# Exercise 9: Calculate the sum of even numbers from 1 to 10

num = 2
total = 0

while num <= 10:
    total += num
    num += 2

print("Sum of even numbers from 1 to 10:", total)


# Exercise 10: Calculate the sum of odd numbers from 1 to 10

num = 1
total = 0

while num <= 10:
    total += num
    num += 2

print("Sum of odd numbers from 1 to 10:", total)
