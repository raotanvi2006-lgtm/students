class Student:
    def __init__(self, roll_no, name, sem):
        self.roll_no = roll_no
        self.name = name
        self.sem = sem

    def display(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Sem: {self.sem}")
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
        students.append(Student(roll_no, name, sem))
    return students

# Main program
student_list = input_students()
print("\nStudent Details:")
for student in student_list:
    student.display()
