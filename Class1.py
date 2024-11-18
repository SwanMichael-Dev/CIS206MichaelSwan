class Employee:
    def __init__(self, name="", idNumber=0, department="", position=""):
        self.__name = name
        self.__idNumber = idNumber
        self.__department = department
        self.__position = position

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_idNumber(self, idNumber):
        self.__idNumber = idNumber

    def get_idNumber(self):
        return self.__idNumber

    def set_department(self, department):
        self.__department = department

    def get_department(self):
        return self.__department

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position


emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

print("Employee 1:")
print("Name:", emp1.get_name())
print("ID Number:", emp1.get_idNumber())
print("Department:", emp1.get_department())
print("Position:", emp1.get_position())

print("\nEmployee 2:")
print("Name:", emp2.get_name())
print("ID Number:", emp2.get_idNumber())
print("Department:", emp2.get_department())
print("Position:", emp2.get_position())

print("\nEmployee 3:")
print("Name:", emp3.get_name())
print("ID Number:", emp3.get_idNumber())
print("Department:", emp3.get_department())
print("Position:", emp3.get_position())