class Employee:
    def __init__(self, name: str, manager=None):
        self.name = name
        self.manager = manager

    def __str__(self):
        if self.manager:
            return f'{self.name}: managed by: {self.manager.name}.'
        return f'{self.name}.'
    
    def __repr__(self):
        return str(self)
    
class Department:
    def __init__(self, name: str, head: Employee=None):
        self.name = name
        self.head = head
        self.team = []

    def with_team(self, *members):
        self.team += members
        return self
    
    def with_head(self, head):
        self.head = head
        return self
    
    def __str__(self):
        return f'{self.name}: headed by: {self.head}. Team: {self.team}'
    
    def __repr__(self):
        return str(self)
    
class Company:
    def __init__(self):
        self.c_suite = [
            Employee('Q Q'),
            Employee('R R'),
            Employee('S S'),
        ]

        self.departments = [
            Department('HR').with_team(
                Employee('A A'),
                Employee('B B'),
            ).with_head(
                Employee('Y Y')
            ),
            Department('DEV').with_team(
                Employee('C C'),
                Employee('D D'),
            ).with_head(
                Employee('Z Z')
            ),
        ]

    def __str__(self):
        return f'C Suite: {self.c_suite} Departments: {self.departments}'
    
    def __repr__(self):
        return str(self)
    
if __name__ == '__main__':
    company = Company()
    print(company)