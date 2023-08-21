class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_info(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print("Department:", self.department)


class Engineer(Employee):
    def __init__(self, emp_id, name, salary, specialization):
        super().__init__(emp_id, name, salary)
        self.specialization = specialization

    def display_info(self):
        super().display_info()
        print("Specialization:", self.specialization)


# Example usage
manager = Manager(1, "John Manager", 80000, "Operations")
engineer = Engineer(2, "Alice Engineer", 60000, "Software Development")

print("Manager Information:")
manager.display_info()

print("\nEngineer Information:")
engineer.display_info()
