# a = int(input("enter a fist number "))
# b = int(input("enter a second numder"))

# if(b == 0):
#     raise ZeroDivisionError("hey, our program is not divided by 0 ")
# else:
#     print(f"{a/b}")    

# *************** try with else ****************

# try:
#     print("harshit")
# except:
#     print("nehra")
# else:
#     print("jaat")        

# ****************try with finally************

def my_function():
    try:
        x = int(input("enter a valid number"))
        print(x)
        return
    except:
        print("error")
        return
    finally:
        print("jaat")  


my_function()
print("dfxmghc,hj")