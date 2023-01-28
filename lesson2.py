# class Student:
#     amount_of_student = 0
#     group = "S 2929"
#     height = 150
#     def __init__(self, height = 160):
#         self.height = height
#         Student.amount_of_student += 1
#
# st1 = Student()
# st2 = Student()
# st3 = Student()
# st4 = Student()
#print(st1.height)
#print(st2.height)
#print(Student.amount_of_student)
# print(st1.group)
# print(st2.group)
# print(st3.group)
# print(st4.group)
#
# st1.group = "V 2929"
# st2.group = "S 4040"
# st3.group = "SP1215"
# st4.group = "STEP"
#
# print(st1.group)
# print(st2.group)
# print(st3.group)
# print(st4.group)
#
# print(Student.group)
# class Student:
#     height = 150
#     def __init__(self):
#         print(self.height)
#         self.height += 20
#         print(self.height)
#
#
# st1 = Student()
# st2 = Student()
# class Student:
#
#     def __init__(self):
#         self.height = 175
#
#     height = 150
#
#     def printer (self):
#         print(self.height)
#
# st1 = Student()
# st1.printer()
class Student:
    amount_of_students = 0

    def __init__(self,height = 160):
        self.height = height
        Student.amount_of_students += 1

    def grow(self, height=1):
        self.height += height

nick = Student()
kate = Student(height = 175)
nick.grow(height = 25)

print(nick.height)
print(kate.height)
kate.grow(height=10)
print(kate.height)

