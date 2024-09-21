# num1 = 1
# while num1 < 9:
#   num = input("enter your number :")
#   sets = set()
#   sets.add(num)
#   num1 += 1
# print(sets)
# ********************   while loop   ************************

# numder = int(input("number : "))
# while(numder < 20):
#   if(numder%2 ==0):
#     print(numder)
#   numder+= 1

# **************    break    *********************
# num1 = int(input("numder: "))

# while(num1 <= 10):
#   print(num1)
#   if num1 == 10:
#     break
#   num1 += 1


# **************   continue    ********************

# i = 0
# while i < 10:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# ***********************************************

# for i in range(11):
#   print(i)

# list = ["mango", "pineapple","banana", "papaya"]  
# for x in list:
#   print(x)
#   if x == "banana":
#     break  


#   # *******************************
# for x in list:
#   print(x)
#   if x == "banana":
#     continue  

#   # *******************************
#   for x in list:
#     print(x)
#     if x == "banana":
#       pass  


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# for i in range(1, 5,3):
    # print(i)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
    # print(x, y) 
 
# i = 1
# while(i< 5):
#     i +=1
#     print("hats")
#     if(i == 3):
#         break
# mytuple = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


# for i in mytuple:
#     print(mytuple[i])

# for i in range(10):
#     if (i == 4):
#         continue
#     print(i)

# num = int(input("enter a number :"))
# i = 1
# while(i <= 10):
#     print(f"{num} * {i} = {num*i}")
#     i += 1 

# for i in range(1,11):
#      print(f"{num} * {i} = {num*i}")

# mylist = ["apple", "banana", "banana", "banana", "banana", "cherry"]
# for i in mylist:
#     if(i.startswith("b")):
#        print(i)
      
n = int(input("number : "))
i= 1
sum = 1
while(i <= n):
    sum *= i
    i +=1
print(sum)

