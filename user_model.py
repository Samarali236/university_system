class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def get_info(self):
        return {
            "name": self.__name,
            "email": self.__email
        }

    def set_email(self, new_email):
        self.__email = new_email

#student subclass inheriting from user class
class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__enrolled_courses = []

    def enroll(self, course_name):
        if course_name not in self.__enrolled_courses:
            self.__enrolled_courses.append(course_name)
            print(f"Enrolled in {course_name}")
        else:
            print(f"Already enrolled in {course_name}")

#instructor subclass inheriting from user class
class Instructor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__teaching_courses = []

    def add_course(self, course_name):
        if course_name not in self.__teaching_courses:
            self.__teaching_courses.append(course_name)
            print(f"Added {course_name} to teaching courses")
        else:
            print(f"Already teaching {course_name}")


student1 = Student("Aya", "aya@gmail.com")
student1.enroll("Calculus1")
student1.enroll("Physics")
student1.enroll("Calculus1")


instructor1= Instructor("Taha", "taha@gmail.com")
instructor1.add_course("Functions")
instructor1.add_course("Inheritance")
instructor1.add_course("Functions")