class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
if __name__ == "__main__":
    # Sample student objects
    students = [
        Student("Alice", "A123", 3.8),
        Student("Bob", "B456", 3.5),
        Student("Charlie", "C789", 4.0),
        Student("David", "D987", 3.2),
    ]

    # Sort students by CGPA
    sorted_students = sort_students(students)

    # Print the sorted list
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")