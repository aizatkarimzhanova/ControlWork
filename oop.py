### 1. Инкапсуляция
print("1. Инкапсуляция")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, value):
        if value <= 0:
            print(f"Неверный возраст! Age must be positive")
        self.__age = value

person1 = Person("Aizat", 19)
print(person1.get_age())
person1.set_age(25)
print(person1.get_age())
person1.set_age(-25)
print(person1.get_age())

### 2. Наследование
print("2. Наследование")
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")

class Dog(Animal):
    def speak(self):
        return("Woof")

class Cat(Animal):
    def speak(self):
        return("Meow")
    
    
animal = Animal("Bark")
dog = Dog("Buddu")
cat = Cat("Kitty")
animal.speak()
print(dog.name, dog.speak())
print(cat.name, cat.speak())



## 3. Полиморфизм
print("3. Полиморфизм")
class Vehiclе:
    def move(self):
        return("Vehicle is moving")
    
class Car(Vehiclе):
    def move(self):
        return("Car is driving")

class Bicyclе(Vehiclе):
    def move(self):
        return("Bicycle is pedaling")
    
car = Car()
bicycle = Bicyclе()
print(car.move())
print(bicycle.move())


### 4. Абстракция
print("4. Абстракция")
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
import math #тут для math.pi

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
rect = Rectangle(4, 5)
circle = Circle(3)
print(rect.area())
print(circle.area())




