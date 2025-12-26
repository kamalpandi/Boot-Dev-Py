class Employee:
    company_name = "Age of Dragons, Inc."
    total_employees = 0

    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary
        Employee.total_employees += 1
        print("self.total_employees", self.total_employees)



    def get_name(self):
        # self.total_employees += 1
        # print("self.total_employees", self.total_employees)
        full_name = self.first_name +" "+self.last_name
        return full_name
        
# self = instance of variable to set
# Class_name. = class variable value to set 