from employee_management_system import EmployeeManagementSystem


def main():
    system = EmployeeManagementSystem()

    success, message = system.add_employee(
        "1001",
        "John Smith",
        "Information Technology",
        "Data Analyst"
    )

    print(message)

    employee = system.search_employee("1001")

    if employee:
        print(employee.get_details())

    success, message = system.mark_attendance("1001", "Present")
    print(message)

    print(system.get_attendance_records())


if __name__ == "__main__":
    main()