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

