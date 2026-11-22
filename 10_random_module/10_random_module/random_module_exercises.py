
# ============================================================
# Lesson 16: Import Random / Random Module
# ============================================================

import math
import random


# Exercise 1: Calculate the exponential value using exp()

result = math.exp(5)

print("Exponential value:", result)


# Exercise 2: Calculate the logarithm of 16 with base 2

result = math.log(16, 2)

print("The logarithm of 16 with base 2 is:", result)


# Exercise 3: Calculate the natural logarithm of 100
# and round the result to the nearest integer

result = math.log(100, math.e)

print("Natural logarithm of 100:", round(result))


# Exercise 4: Calculate the cosine of an angle

angle = float(input("Enter the angle in degrees:"))

angle_radians = math.radians(angle)

cosine_value = math.cos(angle_radians)

print("Cosine of", angle, "degrees:", cosine_value)


# Exercise 5: Calculate the sine of an angle

angle = float(input("Enter the angle in degrees:"))

angle_radians = math.radians(angle)

sine_value = math.sin(angle_radians)

print("Sine of", angle, "degrees:", sine_value)


# Exercise 6: Calculate the tangent of an angle

angle = float(input("Enter the angle in degrees:"))

angle_radians = math.radians(angle)

tangent_value = math.tan(angle_radians)

print("Tangent of", angle, "degrees:", tangent_value)


# Exercise 7: Generate a random integer between 1 and 10

random_number = random.randint(1, 10)

print("Random number between 1 and 10:", random_number)


# Exercise 8: Generate a random floating-point number between 0 and 1

random_float = random.random()

print("Random floating-point number between 0 and 1:", random_float)


# Exercise 9: Randomly select an item from a list

items = ["apple", "banana", "orange", "grape", "kiwi"]

random_item = random.choice(items)

print("Randomly selected item:", random_item)


# Exercise 10: Shuffle the elements of a list

elements = [1, 2, 3, 4, 5]

random.shuffle(elements)

print("Shuffled elements:", elements)
