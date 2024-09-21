import random
computer = random.choice([-1,0,1])

youstr = input("enter your choici")
youDist = {"s": 1 ,"w":-1 ,"g": 0}
reveseDist = { 1:"snack", -1:"water", 0:"gun"}

you = youDist[youstr]
print(f"your choice {reveseDist[you]} : computer choice {reveseDist[computer]}")

if(computer == you):
    print("its is a draw")
else:
    if(computer== -1 and you == 1):
        print("you win")
    elif(computer== -1 and you == 0):
        print("you loss")
    elif(computer== 1 and you == -1):
        print("you loss")
    elif(computer== 1 and you == 0):
        print("you win")
    elif(computer== 0 and you == -1):
        print("you win")
    elif(computer== 0 and you == 1):
        print("you loss")