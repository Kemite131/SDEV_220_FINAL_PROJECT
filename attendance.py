class Attendance:
    """Stores an employee's attendance status."""

    VALID_STATUSES = ("Present", "Absent")

    def __init__(self, employee_id, status="Present"):
        self.employee_id = employee_id
        self.set_status(status)

    def set_status(self, status):
        if status not in self.VALID_STATUSES:
            raise ValueError("Attendance status must be Present or Absent.")

        self.status = status

    def get_attendance(self):
        return self.employee_id, self.status