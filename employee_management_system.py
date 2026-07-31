import json

from employee import Employee
from attendance import Attendance


class EmployeeManagementSystem:
    """Manages employee records and attendance."""

    def __init__(self):
        self.employees = {}
        self.attendance_records = []
        self.data_file = "employee_data.json"
        self.load_data()

    def add_employee(self, employee_id, name, department, position):
        if employee_id in self.employees:
            return False, "Employee ID already exists."

        employee = Employee(employee_id, name, department, position)
        self.employees[employee_id] = employee
        self.save_data()

        return True, "Employee added successfully."

    def search_employee(self, employee_id):
        return self.employees.get(employee_id)

    def update_employee(self, employee_id, name, department, position):
        employee = self.search_employee(employee_id)

        if employee is None:
            return False, "Employee not found."

        employee.update_information(name, department, position)
        self.save_data()

        return True, "Employee information updated successfully."

    def delete_employee(self, employee_id):
        if employee_id not in self.employees:
            return False, "Employee not found."

        del self.employees[employee_id]

        self.attendance_records = [
            record
            for record in self.attendance_records
            if record.employee_id != employee_id
        ]

        self.save_data()

        return True, "Employee deleted successfully."

    def mark_attendance(self, employee_id, status):
        if employee_id not in self.employees:
            return False, "Employee not found."

        try:
            attendance = Attendance(employee_id, status)
            self.attendance_records.append(attendance)
            self.save_data()

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

    def save_data(self):
        employee_data = {}

        for employee_id, employee in self.employees.items():
            employee_data[employee_id] = {
                "name": employee.name,
                "department": employee.department,
                "position": employee.position
            }

        attendance_data = []

        for record in self.attendance_records:
            attendance_data.append({
                "employee_id": record.employee_id,
                "status": record.status
            })

        data = {
            "employees": employee_data,
            "attendance": attendance_data
        }

        try:
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        except OSError as error:
            print(f"Unable to save data: {error}")

    def load_data(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            employee_data = data.get("employees", {})

            for employee_id, details in employee_data.items():
                employee = Employee(
                    employee_id,
                    details["name"],
                    details["department"],
                    details["position"]
                )

                self.employees[employee_id] = employee

            attendance_data = data.get("attendance", [])

            for record in attendance_data:
                attendance = Attendance(
                    record["employee_id"],
                    record["status"]
                )

                self.attendance_records.append(attendance)

        except FileNotFoundError:
            pass

        except (json.JSONDecodeError, KeyError, TypeError) as error:
            print(f"Unable to load saved data: {error}")