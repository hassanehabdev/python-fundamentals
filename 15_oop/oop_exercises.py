# Object-Oriented Programming (OOP) Exercises
# Lessons 28–32
#
# Reviewed solutions arranged in the original lesson and exercise order.
# Several exercises request user input; run individual sections when practicing.
#
# Lesson 29 note: The original exercises demonstrate a two-file workflow.
# Put the class-definition section in hassan.py and the corresponding
# `from hassan import ClassName` line plus object creation in main.py.
# The definitions and main-program examples are shown together here so this
# consolidated file can also be read as one exercise collection.

import math
from abc import ABC, abstractmethod


# ============================================================
# Lesson 28 – OOP (Introduction)
# ============================================================

# Exercise 1: Define a Car class with make and model attributes.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Toyota", "Corolla")
print("Car make:", car1.make)
print("Car model:", car1.model)


# Exercise 2: Define a Circle class and calculate its area.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

circle1 = Circle(5)
print("Area of Circle:", circle1.calculate_area())


# Exercise 3: Count the number of Employee objects created.
class Employee:
    num_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.num_employees += 1

employee1 = Employee("Abdulrahman")
employee2 = Employee("Ahmed")
print("Number of Employees:", Employee.num_employees)


# Exercise 4: Define a Person class with optional parameters.
class Person:
    def __init__(self, name="Anonymous", age=0):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
person2 = Person()
print("Person 1 Name:", person1.name)
print("Person 1 Age:", person1.age)
print("Person 2 Name:", person2.name)
print("Person 2 Age:", person2.age)


# Exercise 5: Get car make and model from the user.
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car_make = input("Enter car make: ")
car_model = input("Enter car model: ")
car2 = Car(car_make, car_model)
print("Car make:", car2.make)
print("Car model:", car2.model)


# Exercise 6: Get a circle radius from the user and calculate its area.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

circle_radius = float(input("Enter circle radius: "))
circle2 = Circle(circle_radius)
print("Area of Circle:", circle2.calculate_area())


# Exercise 7: Get an employee name and display the employee count.
class Employee:
    num_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.num_employees += 1

user_input = input("Enter employee name: ")
employee3 = Employee(user_input)
print("Number of Employees:", Employee.num_employees)


# Exercise 8: Get an employee's name and salary from the user.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

user_input_name = input("Enter employee name: ")
user_input_salary = float(input("Enter employee salary: "))
employee4 = Employee(user_input_name, user_input_salary)
print("Employee Name:", employee4.name)
print("Employee Salary:", employee4.salary)


# Exercise 9: Get a book's title and author from the user.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book_title = input("Enter book title: ")
book_author = input("Enter book author: ")
book1 = Book(book_title, book_author)
print("Book Title:", book1.title)
print("Book Author:", book1.author)


# Exercise 10: Get a movie's title and director from the user.
class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

movie_title = input("Enter movie title: ")
movie_director = input("Enter movie director: ")
movie1 = Movie(movie_title, movie_director)
print("Movie Title:", movie1.title)
print("Movie Director:", movie1.director)


# ============================================================
# Lesson 29 – Import
# ============================================================
# For each exercise, the class below represents hassan.py.
# The commented import represents the corresponding line in main.py.

# Exercise 1: Book.
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def print_data(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Genre:", self.genre)

# main.py: from hassan import Book
book2 = Book("Python Programming", "John Smith", "Programming")
book2.print_data()


# Exercise 2: Rectangle.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_data(self):
        print("Width:", self.width)
        print("Height:", self.height)

# main.py: from hassan import Rectangle
rectangle1 = Rectangle(10, 5)
rectangle1.print_data()


# Exercise 3: Product.
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def print_product_info(self):
        print("Name     :", self.name)
        print("Price    :", self.price)
        print("Category :", self.category)

# main.py: from hassan import Product
phone = Product("Smartphone", 500, "Electronics")
phone.print_product_info()


# Exercise 4: Animal.
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def print_info(self):
        print("Name    :", self.name)
        print("Species :", self.species)
        print("Sound   :", self.sound)

# main.py: from hassan import Animal
animal1 = Animal("Dog", "Canine", "Bark")
animal1.print_info()


# Exercise 5: GammalTechEmployee.
class GammalTechEmployee:
    def __init__(self, name, employee_id, age, department):
        self.name = name
        self.employee_id = employee_id
        self.age = age
        self.department = department

    def print_employee_info(self):
        print("Name        :", self.name)
        print("Employee ID :", self.employee_id)
        print("Age         :", self.age)
        print("Department  :", self.department)

# main.py: from hassan import GammalTechEmployee
employee5 = GammalTechEmployee("John Doe", "E123", 35, "IT")
employee5.print_employee_info()


# Exercise 6: GammalTechProduct.
class GammalTechProduct:
    def __init__(self, name, product_id, price, category):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.category = category

    def print_product_info(self):
        print("Name       :", self.name)
        print("Product ID :", self.product_id)
        print("Price      : $", self.price)
        print("Category   :", self.category)

# main.py: from hassan import GammalTechProduct
laptop = GammalTechProduct("Laptop", "P001", 1200.0, "Electronics")
laptop.print_product_info()


# Exercise 7: GammalTechCustomer.
class GammalTechCustomer:
    def __init__(self, name, customer_id, age, email):
        self.name = name
        self.customer_id = customer_id
        self.age = age
        self.email = email

    def print_info(self):
        print("Name        :", self.name)
        print("Customer ID :", self.customer_id)
        print("Age         :", self.age)
        print("Email       :", self.email)

# main.py: from hassan import GammalTechCustomer
customer = GammalTechCustomer("Alice", "C001", 25, "alice@example.com")
customer.print_info()


# Exercise 8: GammalTechMember with a destructor.
class GammalTechMember:
    def __init__(self, name, phone, age, membership):
        self.name = name
        self.phone = phone
        self.age = age
        self.membership = membership

    def print_data(self):
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Age:", self.age)
        print("Membership:", self.membership)

    def __del__(self):
        print(self.name, "has been deleted")

# main.py: from hassan import GammalTechMember
member = GammalTechMember("AbdurRahman El Gammal", "123", 40, "standard")
member.print_data()
del member


# Exercise 9: Employee with a destructor.
class Employee:
    def __init__(self, name, employee_id, position, salary):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary

    def print_data(self):
        print("Name        :", self.name)
        print("Employee ID :", self.employee_id)
        print("Position    :", self.position)
        print("Salary      :", self.salary)

    def __del__(self):
        print(self.name, "has been deleted")

# main.py: from hassan import Employee
employee6 = Employee("John Doe", "E001", "Software Engineer", 60000)
employee6.print_data()
del employee6


# Exercise 10: Book with publisher, price, and a destructor.
class Book:
    def __init__(self, title, author, publisher, price):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.price = price

    def print_data(self):
        print("Title     :", self.title)
        print("Author    :", self.author)
        print("Publisher :", self.publisher)
        print("Price     : $", self.price)

    def __del__(self):
        print(f"Book '{self.title}' has been deleted")

# main.py: from hassan import Book
python_book = Book("Python Programming", "John Smith", "Tech Books Inc.", 29.99)
python_book.print_data()
del python_book


# ============================================================
# Lesson 30 – Inheritance 1
# ============================================================

# Exercise 1: Shape and Rectangle inheritance.
class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

rectangle2 = Rectangle(5, 4)
print("Area      :", rectangle2.calculate_area())
print("Perimeter :", rectangle2.calculate_perimeter())


# Exercise 2: Calculate the area of a circle.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

circle2 = Circle(3)
print("Area of circle:", circle2.calculate_area())


# Exercise 3: Calculate the area of a triangle.
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 1 / 2 * self.base * self.height

triangle1 = Triangle(6, 8)
print("Area of Triangle:", triangle1.calculate_area())


# Exercise 4: Vehicle and Car inheritance with acceleration.
class Vehicle:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

class Car(Vehicle):
    def accelerate(self):
        self.speed += 10

car3 = Car("Red", 60)
print("Color:", car3.color)
print("Speed:", car3.speed)
car3.accelerate()
print("Accelerated Speed:", car3.speed)


# Exercise 5: Animal and Dog inheritance.
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

class Dog(Animal):
    def make_sound(self):
        print(self.sound)

dog1 = Dog("Canis lupus familiaris", "Woof!")
print("Species:", dog1.species)
print("Sound:", dog1.sound)
print("Dog sound:")
dog1.make_sound()


# Exercise 6: Fruit and Apple inheritance.
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Apple(Fruit):
    def __init__(self, name, color, taste):
        super().__init__(name, color)
        self.taste = taste

    def describe(self):
        print("Name  :", self.name)
        print("Color :", self.color)
        print("Taste :", self.taste)

apple = Apple("Apple", "Red", "Sweet")
apple.describe()


# Exercise 7: Product and Electronic inheritance.
class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class Electronic(Product):
    def __init__(self, name, price, description, brand):
        super().__init__(name, price, description)
        self.brand = brand

    def display_info(self):
        print("Name        :", self.name)
        print("Price       : $", self.price)
        print("Description :", self.description)
        print("Brand       :", self.brand)

electronic_product = Electronic("Laptop", 1000, "15-inch screen, 8GB RAM", "Dell")
electronic_product.display_info()


# Exercise 8: Person and Employee inheritance.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_info(self):
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Salary : $", self.salary)

john = Employee("John Doe", 35, 50000)
john.display_info()


# Exercise 9: Shape and Rectangle inheritance with attributes.
class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Rectangle(Shape):
    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rectangle3 = Rectangle("Rectangle", "Blue", 5, 4)
area = rectangle3.calculate_area()
print("Name  :", rectangle3.name)
print("Color :", rectangle3.color)
print("Area  :", area)


# Exercise 10: Animal and Cat inheritance.
class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

class Cat(Animal):
    def __init__(self, species, sound, breed):
        super().__init__(species, sound)
        self.breed = breed

    def make_sound(self):
        print(self.sound)

cat = Cat("Felis catus", "Meow!", "Siamese")
print("Species :", cat.species)
print("Sound:")
cat.make_sound()
print("Breed   :", cat.breed)


# ============================================================
# Lesson 31 – Inheritance 2
# ============================================================

# Exercise 1: Animal and Dog inheritance.
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking!")

dog2 = Dog("Buddy")
dog2.eat()
dog2.bark()


# Exercise 2: Shape, Square, and Circle with area methods.
class Shape:
    def area(self):
        raise NotImplementedError("subclasses must implement area()")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

square2 = Square(5)
circle3 = Circle(3)
print(f"Area of Square: {square2.area()}")
print(f"Area of Circle: {circle3.area()}")


# Exercise 3: Employee and Manager inheritance.
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def work(self):
        print(f"{self.name} is working in the {self.department} department.")

class Manager(Employee):
    def __init__(self, name, department, salary):
        super().__init__(name, department)
        self.salary = salary

    def manage(self):
        print(f"{self.name} is managing the {self.department} team.")

    def get_salary(self):
        print(f"{self.name}'s salary: ${self.salary}")

employee7 = Employee("Alice", "Marketing")
employee7.work()
manager = Manager("Bob", "Engineering", 80000)
manager.work()
manager.manage()
manager.get_salary()


# Exercise 4: Vehicle, Car, and Airplane with method overriding.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print(f"{self.make} {self.model} is moving.")

class Car(Vehicle):
    def move(self):
        super().move()
        print("...on the road")

class Airplane(Vehicle):
    def move(self):
        super().move()
        print("...through the air")

car4 = Car("Tesla", "Model S")
car4.move()
airplane = Airplane("Boeing", "747")
airplane.move()


# Exercise 5: Shape, Rectangle, and Triangle with draw methods.
class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        raise NotImplementedError("subclasses must implement draw()")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a {self.color} rectangle with width {self.width} and height {self.height}")

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def draw(self):
        print(f"Drawing a {self.color} triangle with base {self.base} and height {self.height}")

rectangle4 = Rectangle("red", 5, 10)
rectangle4.draw()
triangle2 = Triangle("blue", 3, 4)
triangle2.draw()


# Exercise 6: Character, Warrior, and Mage with attack methods.
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} performs a basic attack!")

class Warrior(Character):
    def attack(self):
        super().attack()
        print(f"{self.name} swings a mighty sword!")

class Mage(Character):
    def attack(self):
        super().attack()
        print(f"{self.name} casts a powerful spell!")

warrior = Warrior("Aragorn", 100)
mage = Mage("Gandalf", 80)
warrior.attack()
mage.attack()


# Exercise 7: Shape and Square with an area method.
class Shape:
    def area(self):
        raise NotImplementedError("subclasses must define the area()")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

square3 = Square(5)
print(f"Square Area: {square3.area()}")


# Exercise 8: Figure, Circle, and Triangle inheritance.
class Figure:
    def __init__(self, name):
        self.name = name

class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

class Triangle(Figure):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

circle4 = Circle("My Circle", 3)
triangle3 = Triangle("My Triangle", 4, 5)
print(f"Circle name: {circle4.name}")
print(f"Triangle name: {triangle3.name}")


# Exercise 9: Vehicle and Car with an additional attribute.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print(f"The {self.make} {self.model} is moving.")

class Car(Vehicle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels

    def move(self):
        super().move()
        print("...on the road")

car5 = Car("Tesla", "Model S", 4)
car5.move()


# Exercise 10: Garment and Shirt with conditional sleeve descriptions.
class Garment:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def wear(self):
        print(f"Wearing a {self.color} garment (size {self.size}).")

class Shirt(Garment):
    def __init__(self, size, color, sleeves):
        super().__init__(size, color)
        self.sleeves = sleeves

    def wear(self):
        super().wear()
        if self.sleeves == "long":
            print("...with long sleeves")
        else:
            print("...with short sleeves")

shirt = Shirt("Medium", "blue", "long")
shirt.wear()


# ============================================================
# Lesson 32 – Abstract Class
# ============================================================

# Exercise 1: Abstract Shape class and Square subclass.
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

square4 = Square(5)
print("Area of square:", square4.get_area())


# Exercise 2: Abstract Animal class with Dog and Cat subclasses.
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog3 = Dog()
cat2 = Cat()
dog3.make_sound()
cat2.make_sound()


# Exercise 3: Abstract Operation class with Addition and Subtraction.
class Operation(ABC):
    @abstractmethod
    def calculate(self, num1, num2):
        pass

class Addition(Operation):
    def calculate(self, num1, num2):
        return num1 + num2

class Subtraction(Operation):
    def calculate(self, num1, num2):
        return num1 - num2

addition = Addition()
subtraction = Subtraction()
print("Addition result:", addition.calculate(5, 3))
print("Subtraction result:", subtraction.calculate(10, 4))


# Exercise 4: Abstract Authentication class.
class Authentication(ABC):
    @abstractmethod
    def verify_credentials(self, username, password):
        pass

class UsernamePasswordAuth(Authentication):
    def verify_credentials(self, username, password):
        if username == "admin" and password == "secret":
            print("Login Successful!")
        else:
            print("Invalid credentials!")

auth = UsernamePasswordAuth()
auth.verify_credentials("admin", "secret")


# Exercise 5: Abstract Shape class with Rectangle and Circle subclasses.
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

rectangle5 = Rectangle(5, 4)
circle5 = Circle(3)
print("Area of Rectangle:", rectangle5.calculate_area())
print("Area of Circle:", circle5.calculate_area())


# Exercise 6: Abstract Shape class with Triangle and Square subclasses.
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

triangle4 = Triangle()
square5 = Square()
triangle4.draw()
square5.draw()


# Exercise 7: Abstract Food class with Pizza and Broccoli subclasses.
class Food(ABC):
    @abstractmethod
    def is_tasty(self):
        pass

class Pizza(Food):
    def is_tasty(self):
        return True

class Broccoli(Food):
    def is_tasty(self):
        return False

pizza = Pizza()
broccoli = Broccoli()
print("Is pizza tasty?", pizza.is_tasty())
print("Is broccoli tasty?", broccoli.is_tasty())


# Exercise 8: Abstract Vehicle class with Car and Bicycle subclasses.
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is moving")

class Bicycle(Vehicle):
    def move(self):
        print("Bicycle is moving")

car6 = Car()
bicycle = Bicycle()
car6.move()
bicycle.move()


# Exercise 9: Abstract Person class with Teacher and Student subclasses.
class Person(ABC):
    @abstractmethod
    def speak(self):
        pass

class Teacher(Person):
    def speak(self):
        print("Good morning, class!")

class Student(Person):
    def speak(self):
        print("Good morning, teacher!")

teacher = Teacher()
student = Student()
teacher.speak()
student.speak()


# Exercise 10: Abstract PaymentProcessor class.
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} via credit card.")

creditcard = CreditCardProcessor()
creditcard.process_payment(100)
