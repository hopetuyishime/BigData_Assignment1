class StudentManagementSystem:
    def __init__(self):
        self.student = {
            "name": "",
            "age": 0,
            "grades": {}
        }

    def get_student_information(self):
        self.student["name"] = input("Enter your name: ")
        self.student["age"] = int(input("Enter your age: "))

        courses = ["course1", "course2", "course3"]
        for course in courses:
            while True:
                try:
                    grade = int(input(f"Enter your grade for {course}: "))
                    self.student["grades"][course] = grade
                    break
                except ValueError:
                    print("Please enter a valid integer.")

    def calculate_average(self):
        grades = list(self.student["grades"].values())
        if grades:
            average = sum(grades) / len(grades)
            self.student["average"] = round(average, 2)
        else:
            self.student["average"] = None

    def display_student_information(self):
        print("\n📚 Student Information:")
        print(f"Name: {self.student['name']}")
        print(f"Age: {self.student['age']}")
        for course, grade in self.student["grades"].items():
            print(f"{course.title()}: {grade}")
        print(f"Average: {self.student.get('average', 'N/A')}")


# Run the system
system= StudentManagementSystem()
system.get_student_information()
system.calculate_average()
system.display_student_information()
