from abc import ABC, abstractmethod

# Abstract Base Class (Blueprint)
class Student(ABC):
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    # Abstract Method: Every child class MUST implement this
    @abstractmethod
    def calculate_fees(self):
        pass

    # Abstract Method: Every child class MUST implement this
    @abstractmethod
    def get_attendance_requirement(self):
        pass

    # Regular Method: Inherited directly by all child classes
    def get_profile(self):
        return f"ID: {self.student_id} | Name: {self.name}"

# Child Class 1: Regular Full-Time Student
class RegularStudent(Student):
    def calculate_fees(self):
        return "Tuition: ₹50,000 + Campus Amenities: ₹10,000"

    def get_attendance_requirement(self):
        return "Minimum 75% attendance required to sit for exams."

# Child Class 2: Distance Learning Student
class DistanceStudent(Student):
    def calculate_fees(self):
        return "Tuition: ₹20,000 (Exam fees included)"

    def get_attendance_requirement(self):
        return "No daily attendance required. Must attend 2 weekend contact classes."

# --- Execution ---

# ❌ This will throw an error because you cannot instantiate an abstract class directly
# trying_to_create = Student("Alex", "S101") 

# Creating instances of child classes
student_a = RegularStudent("Rahul Sharma", "REG2026-04")
student_b = DistanceStudent("Priya Patel", "DIST2026-89")

# Accessing shared and abstracted ERP functions
print(student_a.get_profile())
print(f"Fee Structure: {student_a.calculate_fees()}")
print(f"Policy: {student_a.get_attendance_requirement()}\n")

print(student_b.get_profile())
print(f"Fee Structure: {student_b.calculate_fees()}")
print(f"Policy: {student_b.get_attendance_requirement()}")