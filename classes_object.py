

# The class is a template to create/describe an object(like a form).
# _init_ is a constructor, it help to initialise the attribute in a class

class Employees:
    def __init__(self, fname, lname, gender, qualification): # instance
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.qualification = qualification
        self.email = f"{fname}{lname}@gmail.com"

    def fullname(self):
        return(f"{self.fname} {self.lname}")


 # Child Class(subclasses)
class Details(Employees):
    def __init__(self, fname, lname, gender, qualification, marital_status, prog_lang):
        super().__init__(fname, lname, gender, qualification)
        self.marital_status = marital_status
        self.prog_lang = prog_lang

class Manager(Employees):
    def __init__(self, fname, lname, gender, qualification, employees=None):
        super().__init__(fname, lname, gender, qualification)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())

# object is an instance is a collection of data with associated behavior
# (filled form)
emp1 = Details("Tem", "John", "Male","Software developer","Single", "Python")
emp2 = Details("Vic","Alfread", "Female","Data analyst", "Married", "R")
emp3 = Details("Bayo","Shun", "Male","Frontend engineer","Single", "Java")

mgr1 = Manager("Samuel","Abey","Male","Software developer", [emp3])

# isinstance function tells us if an object is the instance of a class
isinstance(mgr1, Manager)

# issubclass function tell us if a class is a subclass of another
issubclass(Manager, Employees)


# mgr1.email
# mgr1.add_emp(emp1)
# mgr1.add_emp(emp2)
# mgr1.remove_emp(emp1)
# mgr1.print_emps()

# e1.email
# e2.prog_lang



# Encapsulation It hide the value of structured data object inside a class, to prevent unauthorised parties direct access to them
# attribute = variables, e.g .shape
# method = function(), e.g .info()

# Inheritance is when a child class can inherit all method and properties from a parent class.This is applied to classes Extend functionality of existing code

# Polymorphism Is the ability to take multiple forms. This is applied to method and functions.

# Abstraction is hiding the internal functionality/ unwanted information from the user and only emphasizing on the usage of it