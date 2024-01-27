class Employee:
    def __init__(self, Name, age, Gender, Department):
        self.Name = Name
        self.age = age
        self.Gender = Gender
        self.Department = Department

    def show_Employee(self):
        print("Employee name:        ", self.Name)
        print("Employee age:         ", self.age)
        print("Employee Gender:      ", self.Gender)
        print("Employee Department:  ", self.Department)

S=Employee("sachin prasad",22,"Male","Product Manager")

S.show_Employee()