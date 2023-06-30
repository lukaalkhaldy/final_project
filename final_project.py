import uuid

class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = uuid.uuid4()
        self.course_name = course_name
        self.course_mark = course_mark

class Student:
    total_student_count = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = uuid.uuid4()
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.total_student_count += 1

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_details(self):
        return self.__dict__

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course Name: {course.course_name}, Course Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        average = total_marks / len(self.courses_list)
        return average

students_list = []

while True:
    try:
        selection = int(input("1. Add New Student\n"
                              "2. Delete Student\n"
                              "3. Display Student\n"
                              "4. Get Student Average\n"
                              "5. Add Course to Student with Mark\n"
                              "6. Exit\n"))

        if selection == 1:
            student_number = input("Enter Student Number: ")
            student_name = input("Enter Student Name: ")
            while True:
                try:
                    student_age = int(input("Enter Student Age: "))
                    break
                except ValueError:
                    print("Invalid Value")

            if any(student.student_number == student_number for student in students_list):
                print("Student Number already exists!")
            else:
                new_student = Student(student_name, student_age, student_number)
                students_list.append(new_student)
                print("Student Added Successfully")

        elif selection == 2:
            student_number = input("Enter Student Number: ")
            for student in students_list:
                if student.student_number == student_number:
                    students_list.remove(student)
                    print("Student Deleted Successfully")
                    break
            else:
                print("Student Not Found")

        elif selection == 3:
            student_number = input("Enter Student Number: ")
            for student in students_list:
                if student.student_number == student_number:
                    print("Student Details:")
                    student_details = student.get_student_details()
                    for key, value in student_details.items():
                        print(f"{key}: {value}")
                    break
            else:
                print("Student Not Found")

        elif selection == 4:
            student_number = input("Enter Student Number: ")
            for student in students_list:
                if student.student_number == student_number:
                    average = student.get_student_average()
                    print(f"Student Average: {average}")
                    break
            else:
                print("Student Not Found")

        elif selection == 5:
            student_number = input("Enter Student Number: ")
            for student in students_list:
                if student.student_number == student_number:
                    course_name = input("Enter Course Name: ")
                    course_mark = float(input("Enter Course Mark: "))
                    new_course = Course(course_name, course_mark)
                    student.enroll_course(new_course)
                    print("Course Added Successfully")
                    break
            else:
                print("Student Not Found")

        elif selection == 6:
            print("Exiting the program...")
            break

        else:
            print("Invalid selection. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")



