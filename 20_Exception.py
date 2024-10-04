# try:
#     a = int(input("hey , enter  a valid number "))
#     print(a)

# except Exception as e:
#     print(e)

x = "harshit"
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
