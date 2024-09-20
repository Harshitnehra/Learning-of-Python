thisset = {"apple", "banana", "cherry", True, 1, 2 ,False ,0}
thisset.add("harshit")
# for x in thisset:
    # print(x)
# print(thisset)
# print(len(thisset))
# print(type(thisset))

# print("dfghjk" in thisset)


tropical = {"pineapple", "mango", "papaya"}

tropical.update(thisset)
del thisset
# print(thisset)
tropical.clear()
# print(tropical)



# =============     Join Sets      ============
set1 = {"a", "b", "c","7","8","9"}
set2 = {1, 2, 3, "a" , "b", "c"}

set3 = set1.union(set2)
set3.add("sdfg")
# print(set3)

# set1.intersection_update(set2)
# print(set1)


set4 = set1.difference(set2)
# print(set4)

set1 = {"apple", "banana" , "cherry","hsa"}
set2 = {"google", "microsoft", "apple", "banana" , "cherry"}

set3 = set1.difference(set2)
# print(set3)



# /////////////////////////////

words = {
    "harshit": "good",
    "siddharth": "don",
    "reenu": "girl",
    "shinu": "tai"
}

# word = input("enter name  ")

# print(words[word])


# i = 1
# while i < 9:
#   num = input("enter your number :")
#   i += 1
#   sets = set()
 
#   sets.add(num)

 
# print(sets)


word  = set()
word.add("234")
word.add(234)
word.add(234.0)
# print(len(word))
# print(word)


sum = {}

# name = input("name")
# lang = input("lang name")
# sum.update({name : lang})
# name = input("name")
# lang = input("lang name")
# sum.update({name : lang})
# name = input("name")
# lang = input("lang name")
# sum.update({name : lang})
# name = input("name")
# lang = input("lang name")
# sum.update({name : lang})
# print(sum)
 


cshzvjz = {2,34,5}
print(cshzvjz)