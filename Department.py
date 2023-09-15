__departments = 0
__employees = 0

class department:
    def __init__(self, name, emps = 0):
        self._name = name
        __departments += 1
        self._emps = emps
    
    def change_employee_count(self, num):
        print(f"Changing the employee count by {num - self._emps}...")
        self._emps = num
        print(f"It is now {self._emps}")

class employee:
    def __init__(self, id, name, age, email, dept = None):
        self._id = id
        self._name = name
        self._age = age
        self._email = email
        __employees += 1
        self._dept = dept
    
    def change_department(self, dept):
        self._dept = dept
        print(f"The employee has been reassigned to {self._dept}")

