class Employee:
    """Stores information about one employee."""

    def __init__(self, employee_id, name, department, position):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.position = position

    def update_information(self, name, department, position):
        self.name = name
        self.department = department
        self.position = position

    def get_details(self):
        return (
            self.employee_id,
            self.name,
            self.department,
            self.position
        )