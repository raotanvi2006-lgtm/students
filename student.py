class Student:
    def __init__(self, roll_no, name, sem, course):
        self.roll_no = roll_no
        self.name = name
        self.sem = sem
        self.course = course

    def display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Sem: {self.sem}")
        print(f"Course: {self.course}")
        print("-" * 30)

# Function to input student details
def input_students():
    students = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        roll_no = input("Roll No: ")
        name = input("Name: ")
        sem = input("sem: ")
        course = input("Course: ")
        students.append(Student(roll_no, name, sem, course))
    return students

# Main program
student_list = input_students()
print("\nStudent Details:")
for student in student_list:
    student.display()
