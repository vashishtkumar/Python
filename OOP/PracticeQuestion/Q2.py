class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
            print(f"The role of employee is {self.role} , department is {self.department} and salary is {self.salary}")

class Engineer(Employee):
      def __init__(self, role, department, salary,name,age):
            self.age=age
            self.name=name
            print(f"The name of Employee is {self.name} and the age of Employee is {self.age}", end=" .")
            super().__init__(role, department, salary)


e1=Engineer("SDET","CSE","20K","Vashisht",20)
e1.showDetails()

