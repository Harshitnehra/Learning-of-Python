userage = int(input("give me a number"))
day = input("enter your day")


if userage <= 17:
  prise = 8
  if day == "wed":
    print(prise-2)
  print(prise)
else:
  prise = 12
  if day == "wed":
    print(prise-2)
  print(prise)
   



