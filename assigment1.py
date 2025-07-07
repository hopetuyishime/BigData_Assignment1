class StudentManagementSystem:
    def __init__(self):
        # Initialize student information
        self.student = {
            "name": "",
            "age": 0,
            "grades": {}
        }

    def get_student_information(self):
        """Collect student's name, age, and course grades with basic validation."""
        while True:
            name = input("📝 Enter your full name: ").strip()
            if name:
                self.student["name"] = name
                break
            print("⚠️ Name cannot be empty. Please try again.")

        while True:
            try:
                age = int(input("🎂 Enter your age: "))
                if age > 0:
                    self.student["age"] = age
                    break
                else:
                    print("⚠️ Age must be a positive number.")
            except ValueError:
                print("⚠️ Please enter a valid number for age.")

        print("\n🎓 Enter your grades for the following courses (0 - 100):")
        courses = ["Mathematics", "Science", "History"]
        for course in courses:
            while True:
                try:
                    grade = int(input(f"➡️  {course} grade: "))
                    if 0 <= grade <= 100:
                        self.student["grades"][course] = grade
                        break
                    else:
                        print("⚠️ Grade must be between 0 and 100.")
                except ValueError:
                    print("⚠️ Please enter a valid integer for grade.")

    def calculate_average(self):
        """Calculate and store the average grade."""
        grades = list(self.student["grades"].values())
        if grades:
            average = sum(grades) / len(grades)
            self.student["average"] = round(average, 2)
        else:
            self.student["average"] = None

    def display_student_information(self):
        """Display collected student information."""
        print("\n📚 Student Profile:")
        print(f"👤 Name: {self.student['name']}")
        print(f"🎂 Age: {self.student['age']}")
        print("📊 Grades:")
        for course, grade in self.student["grades"].items():
            print(f"   - {course}: {grade}")

        average = self.student.get("average", "N/A")
        print(f"⭐ Average Grade: {average}")


# Run the system
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.get_student_information()
    system.calculate_average()
    system.display_student_information()
