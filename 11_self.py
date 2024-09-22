class employee:
    company = "google"
    language = "python"
    salery = "1200000"
    def getinfo(self):
        print(f"my company name is {self.company} and my selary is {self.salery}")

harshit = employee()
harshit.company= "microsoft"
# harshit.getinfo()
employee.getinfo(harshit)
