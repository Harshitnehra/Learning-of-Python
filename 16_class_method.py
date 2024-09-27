# class employee: 
#     name = "harshit"
#     @classmethod
#     def show(self):
#         print(f"my name is {self.name}")

# a = employee()
# a.name = "hittu nehra"
# a.show()        


class employee:
    language = "py"
    salary = 120000000
    def getinffo(self , name ,roll):
        self.name = name 
        self.roll = roll 
        print(f"my name is harshit {self.salary}{name}{roll}")

    
    def __init__(self, name ,roll):
        self.name = name 
        self.roll = roll 
        print(f"my name is harshit {self.salary}{name}{roll}")

    @staticmethod    
    def greet():
        print("hllo harshit")    
    
mohan = employee("tiger",1234)
# mohan.cast = "jaat"
# mohan.salary = 147800000000000
# print(mohan.language, mohan.cast, mohan.salary)    
# mohan.getinffo("chittaaa",1234)
# mohan.greet()