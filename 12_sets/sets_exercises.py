
# ============================================================
# Lesson 22: Sets
# ============================================================


# Exercise 1: Create a set containing numbers from 1 to 5

my_set = {1, 2, 3, 4, 5}

print(my_set)


# Exercise 2: Create two sets containing different elements

set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Set 1:", set1)
print("Set 2:", set2)


# Exercise 3: Create a set containing fruit names

fruits_set = {"apple", "banana", "cherry"}

print(fruits_set)


# Exercise 4: Attempt to add a duplicate element to a set

fruits_set = {"apple", "banana", "cherry"}

fruits_set.add("banana")

print(fruits_set)


# Exercise 5: Perform a union operation on two sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)

print("Union set:", union_set)


# Exercise 6: Perform an intersection operation on two sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection_set = set1.intersection(set2)

print("Intersection set:", intersection_set)


# Exercise 7: Check if one set is a subset of another

set1 = {1, 2, 3}
set2 = {3, 4, 5}

is_subset = set1.issubset(set2)

print("Is set1 a subset of set2?", is_subset)


# Exercise 8: Remove an element from a set

my_set = {"apple", "banana", "cherry"}

my_set.remove("banana")

print(my_set)


# Exercise 9: Clear all elements from a set

my_set = {"apple", "banana", "cherry"}

my_set.clear()

print(my_set)


# Exercise 10: Check if a set is empty

my_set = {1, 2, 3}

if not my_set:
    print("The set is empty")
else:
    print("The set is not empty")
