class employee:
    company = "itc"
    name = "harshit"
    salary = "120000000000"
    def show(self):
        print(f"the name is {self.name} and salary is {self.salary}")

class coder(employee):
    language = "javascript"
    def coderlang(self):
        print(f"coder language is {self.language}")
class programer(coder):
    language = "python"
    def showlanguage(self):
        print(f"my name is {self.name} and my fav language is {self.language}")    
a  = employee()
# a.show("jaat")
b = coder()
b.coderlang()
b.show()
b.showlanguage()
# print(a.company , b.company)

