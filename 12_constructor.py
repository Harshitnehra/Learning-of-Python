class employee:
    company = "google"
    language = "python"
    salery = "1200000"
    def __init__(self, name , salery, language) :
        self.name = name 
        self.salery = salery
        self.language = language
        print(f"i am a creating a object{salery}")
        

harshit = employee("harshit", 1400000, "javascript")
# harshit.company= "microsoft"
print(harshit.name, harshit.company, harshit.salery, harshit.language)


class programer:
    company = "microsoft"
    def __init__(self, name ,salary, pinno):
        self.name = name
        self.salary = salary
        self.pinno = pinno
        


harshit  = programer("harshit" , 120000000000, 1234567)
print(harshit.company, harshit.salary , harshit.pinno)


# ************************************

class calculator:
    def __init__(self , n):
        self.n = n
        print("hllo user")

    def square(self):
        print(f"square of a number is {self.n**0.5}")  

    @ staticmethod    
    def hllo():
        print("hllo user harshit")    

a = calculator(5)
a.hllo()
a.square()