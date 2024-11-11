class Addition:
    first = 0
    second = 0
    answer = 0
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


 
obj1 = Addition(1000, 2000)
print("Enter the 2 number for addition")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
obj2 = Addition(a , b)
obj1.calculate()
obj2.calculate()
obj1.display()
obj2.display()

'''class Person:
    def __init__(self, name=None, age=None):
        if name is not None and age is not None:
            self.name = name
            self.age = age
        else:
            self.name = "Unknown"
            self.age = 0
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2024 - birth_year)

# Using default constructor
person1 = Person("Alice", 30)
print(person1.name, person1.age)  # Output: Alice 30

# Using alternative constructor
person2 = Person.from_birth_year("Bob", 1990)
print(person2.name, person2.age) ''' # Output: Bob 34