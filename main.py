import tkinter as tk
from tkinter import messagebox
from employee_management_system import EmployeeManagementSystem


class EmployeeManagementGUI:
    def __init__(self, root):
        self.system = EmployeeManagementSystem()
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("750x600")

        tk.Label(
            root,
            text="Employee Management System",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        form_frame = tk.Frame(root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Employee ID:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e"
        )
        self.employee_id_entry = tk.Entry(form_frame, width=30)
        self.employee_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Name:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Department:").grid(
            row=2, column=0, padx=5, pady=5, sticky="e"
        )
        self.department_entry = tk.Entry(form_frame, width=30)
        self.department_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Position:").grid(
            row=3, column=0, padx=5, pady=5, sticky="e"
        )
        self.position_entry = tk.Entry(form_frame, width=30)
        self.position_entry.grid(row=3, column=1, padx=5, pady=5)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(
            button_frame,
            text="Add Employee",
            width=15,
            command=self.add_employee
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Search Employee",
            width=15,
            command=self.search_employee
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Update Employee",
            width=15,
            command=self.update_employee
        ).grid(row=0, column=2, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Delete Employee",
            width=15,
            command=self.delete_employee
        ).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Display All",
            width=15,
            command=self.display_all
        ).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(
            button_frame,
            text="Clear Fields",
            width=15,
            command=self.clear_fields
        ).grid(row=1, column=2, padx=5, pady=5)

        tk.Label(root, text="Employee Records").pack(pady=5)

        self.output_text = tk.Text(root, width=85, height=18)
        self.output_text.pack(padx=10, pady=10)

    def get_form_data(self):
        employee_id = self.employee_id_entry.get().strip()
        name = self.name_entry.get().strip()
        department = self.department_entry.get().strip()
        position = self.position_entry.get().strip()

        return employee_id, name, department, position

    def add_employee(self):
        employee_id, name, department, position = self.get_form_data()

        if not employee_id or not name or not department or not position:
            messagebox.showerror("Input Error", "Please complete all fields.")
            return

        success, message = self.system.add_employee(
            employee_id,
            name,
            department,
            position
        )

        if success:
            messagebox.showinfo("Success", message)
            self.clear_fields()
            self.display_all()
        else:
            messagebox.showerror("Error", message)

    def search_employee(self):
        employee_id = self.employee_id_entry.get().strip()

        if not employee_id:
            messagebox.showerror("Input Error", "Enter an employee ID.")
            return

        employee = self.system.search_employee(employee_id)

        if employee is None:
            messagebox.showerror("Error", "Employee not found.")
            return

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, employee.name)

        self.department_entry.delete(0, tk.END)
        self.department_entry.insert(0, employee.department)

        self.position_entry.delete(0, tk.END)
        self.position_entry.insert(0, employee.position)

    def update_employee(self):
        employee_id, name, department, position = self.get_form_data()

        if not employee_id or not name or not department or not position:
            messagebox.showerror("Input Error", "Please complete all fields.")
            return

        success, message = self.system.update_employee(
            employee_id,
            name,
            department,
            position
        )

        if success:
            messagebox.showinfo("Success", message)
            self.display_all()
        else:
            messagebox.showerror("Error", message)

    def delete_employee(self):
        employee_id = self.employee_id_entry.get().strip()

        if not employee_id:
            messagebox.showerror("Input Error", "Enter an employee ID.")
            return

        success, message = self.system.delete_employee(employee_id)

        if success:
            messagebox.showinfo("Success", message)
            self.clear_fields()
            self.display_all()
        else:
            messagebox.showerror("Error", message)

    def display_all(self):
        self.output_text.delete("1.0", tk.END)

        employees = self.system.get_all_employees()

        if not employees:
            self.output_text.insert(tk.END, "No employee records available.")
            return

        for employee in employees:
            employee_id, name, department, position = employee.get_details()

            self.output_text.insert(
                tk.END,
                f"ID: {employee_id}\n"
                f"Name: {name}\n"
                f"Department: {department}\n"
                f"Position: {position}\n"
                f"{'-' * 45}\n"
            )

    def clear_fields(self):
        self.employee_id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)


def main():
    root = tk.Tk()
    EmployeeManagementGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()