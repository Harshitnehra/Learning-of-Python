low = int(input("enter a num ")) 
upper = int(input("enter a num1 ")) 

for num in range(low , upper):
      if num > 1:
            for i in range(2 , num):
                  if num % i == 0:
                        print("not prime", num)
                        break         
            else:
                  print(num)
