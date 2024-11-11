class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Emp ID: {self.emp_id}"

emp = Employee("John Doe", 30, "E001")
print(emp.display()) 
