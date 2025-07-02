class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
 
    def set_email(self, new_email):
        self.__email = new_email 
    
    def get_info(self):
        print(f"Name : {self.__name}")
        print(f"Email : {self.__email}")
        
class Student(User):
    def __init__(self, name, email):
        self.__enrolled_course = []
        super().__init__(name, email)
    
    def enroll(self, course_name):
        self.__enrolled_course.append(course_name)
    
    def print_student(self):
        super().get_info()
        for i in self.__enrolled_course:
            print("Enrolled Course:", i)

class Instructor(User):
    def __init__(self, name, email):
        self.__teaching_courses = []
        super().__init__(name, email)
    
    def add_course(self, course_name):
        self.__teaching_courses.append(course_name)

    def print_instructor(self):
        super().get_info()
        for i in self.__teaching_courses:
            print("Teaching Course:", i)



u = User("x", "y")
s = Student("s","s1")
i = Instructor("i","i1")

def user():
    u.get_info()
    u.set_email("new_mail")
    u.get_info()
    print("#################")

def student():
    s.enroll("python")
    s.enroll("Java")
    s.print_student()
    print("#################")

def instructor():
    i.add_course("python")
    i.add_course("Java")
    i.print_instructor()
    print("#################")

user()
student()
instructor()