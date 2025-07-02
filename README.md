# Inheritance-and-Encapsulation-Direct-Application-
Instructions:

Create a base class User:
Private attributes: __name, __email
Having public methods:
get_info() → returns name and email
set_email(new_email) → updates the email

Create a subclass Student(User):
Private attribute: __enrolled_courses (list)
Method: enroll(course_name)

Create a subclass Instructor(User):
Private attribute: __teaching_courses (list)
Method: add_course(course_name)
