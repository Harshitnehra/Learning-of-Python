import random
n = random.randint(1,10)
a = -1
g = 0
while(a != n):
    a = int(input("enter a number 1 - 10: "))
    # print(a)
    if(a > n):
        print("guess the smaller number")
    elif(a < n):
        print("guess the larger number")
    g += 1    
print(f" correct number is  {n} and total number of attemp is {g}")
    








