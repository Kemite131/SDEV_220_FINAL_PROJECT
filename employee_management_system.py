from employee import Employee
from attendance import Attendance


class EmployeeManagementSystem:
    """Manages employee records and attendance."""

    def __init__(self):
        self.employees = {}
        self.attendance_records = []

    def add_employee(self, employee_id, name, department, position):
        if employee_id in self.employees:
            return False, "Employee ID already exists."

        employee = Employee(employee_id, name, department, position)
        self.employees[employee_id] = employee

        return True, "Employee added successfully."

    def search_employee(self, employee_id):
        return self.employees.get(employee_id)

    def update_employee(self, employee_id, name, department, position):
        employee = self.search_employee(employee_id)

        if employee is None:
            return False, "Employee not found."

        employee.update_information(name, department, position)
        return True, "Employee information updated successfully."

    def delete_employee(self, employee_id):
        if employee_id not in self.employees:
            return False, "Employee not found."

        del self.employees[employee_id]
        return True, "Employee deleted successfully."

    def mark_attendance(self, employee_id, status):
        if employee_id not in self.employees:
            return False, "Employee not found."

        try:
            attendance = Attendance(employee_id, status)
            self.attendance_records.append(attendance)

            return True, "Attendance recorded successfully."

        except ValueError as error:
            return False, str(error)

    def get_all_employees(self):
        return list(self.employees.values())

    def get_attendance_records(self):
        return tuple(
            record.get_attendance()
            for record in self.attendance_records
        )