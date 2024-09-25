class employee:
    company = "itc"
    name = "harshit"
    salary = "120000000000"
    def show(self, cast):
        self.cast = cast
        print(f"the name is {self.name, self.cast} and salary is {self.salary}")

# class programer:
#     company = "itc info"
#     def show(self):
#         print(f"the name is {self.name} and salary is {self.salary}")

    # def showlanguage(self):
    #     print(f"my name is {self.name} and my fav language is {self.language}")

class programer(employee):
    language = "python"
    def showlanguage(self):
        print(f"my name is {self.name} and my fav language is {self.language}")    
# a  = employee()
# a.show("jaat")
# b = programer()
# b.show("jaat")
# b.showlanguage()
# print(a.company , b.company)




class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    print(F"{self.firstname}{self.lastname}")
  def printname(self):
    print(self.firstname, self.lastname)

class siddharth:
   siddharth = "donkey"
   nehra = "jaat"
   print(f"{siddharth}{nehra}")

class Student(Person, siddharth):
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    print(F"{self.firstname}  {self.lastname}")
    Person.__init__(self, fname, lname)
    


    
# x = Student("Mike", "Olsen")
# y = Person("harshit", "nehra")
# a = siddharth()

class a:
   def __init__(self):
      print("hllo a")

class b:
   def __init__(self):
      print(f"hllo b")


class c(b): 
   name = "hasshit"
   print(f"{name}")
   def __init__(self):
      # super().__init__()
      print(f"hllo c {self.name}")  
   @classmethod      
   def show(self):
      print (f"print the name {self.name}")

q = c()      
q.name= "nehra jaat"     
q.show()