# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Harshit")

# print("Before:", s1.name)

# # Modify attribute
# s1.name = "Rahul"

# print("After:", s1.name)


# class Student:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Student Name: {self.name}"

# s1 = Student("Harshit")

# print(s1)   # Calls __str__()


# class Student:

#     count = 0

#     def __init__(self):
#         Student.count += 1

# s1 = Student()
# s2 = Student()

# print(Student.count)



class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(B , A):
    pass

obj = C()
obj.show()