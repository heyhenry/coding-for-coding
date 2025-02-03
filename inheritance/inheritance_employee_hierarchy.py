# practicing usage of inheritance
"""
1. Person Class

-   name (str): The person's name.
-   age (int): The person's age.
-   get_details(): Returns a formatted string with name and age.

2. Employee Class (inherits from Person)

-   employee_id (int): Unique employee identifier.
-   job_title (str): Job position.
-   get_employee_details(): Returns employee details, including inherited properties.

3. Manager Class (inherits from Employee)

-   num_team_members (int): Number of employees managed.
-   get_manager_details(): Returns full details including the team size.
-   add_team_member(): Increments num_team_members by 1.
-   remove_team_member(): Decrements num_team_members by 1 (ensuring it doesn’t go negative).
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age, employee_id, job_title):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.job_title = job_title
    
    def get_employee_details(self):
        return f"{self.get_details()}, Employee ID: {self.employee_id}, Job Title: {self.job_title}"

class Manager(Employee):
    def __init__(self, name, age, employee_id, job_title, num_team_members):
        super().__init__(name, age, employee_id, job_title)
        self.num_team_members = num_team_members

    def get_manager_details(self):
        return f"{self.get_employee_details()}, Team Size: {self.num_team_members}"
    
    def add_team_member(self):
        self.num_team_members += 1

    def remove_team_member(self):
        if self.num_team_members > 0:
            self.num_team_members -= 1


def run_tests():
    print("Running tests...")
    
    # Test Person
    p = Person("John Doe", 30)
    assert p.get_details() == "Name: John Doe, Age: 30"
    
    # Test Employee
    e = Employee("Jane Smith", 25, 101, "Software Engineer")
    assert e.get_employee_details() == "Name: Jane Smith, Age: 25, Employee ID: 101, Job Title: Software Engineer"
    
    # Test Manager
    m = Manager("Alice Brown", 40, 200, "Project Manager", 5)
    assert m.get_manager_details() == "Name: Alice Brown, Age: 40, Employee ID: 200, Job Title: Project Manager, Team Size: 5"
    
    # Test add_team_member
    m.add_team_member()
    assert m.num_team_members == 6
    
    # Test remove_team_member
    m.remove_team_member()
    assert m.num_team_members == 5
    
    # Test remove_team_member when already at zero
    m.num_team_members = 0
    m.remove_team_member()  # Should print a message but not decrement below 0
    assert m.num_team_members == 0
    
    print("All tests passed.")


# Run test cases
if __name__ == "__main__":
    run_tests()