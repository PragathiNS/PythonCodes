#List is a compound data type
e1 = "My"
e2 = "name"

list1 = [e1, e2, "is", "John"]
print(list1)


#Now let's create another list -- list of student names in a class
s1 = "Ram"
s2 = "Sham"
s3 = "Pam"

studentList = [s1, s2, s3]
print(studentList)

#Grocery list
apples = 10
banana = 12
wheat = 2
faceWash = 1
towel = 3

groceryList = [apples, banana, wheat, faceWash, towel]
print(groceryList)

groceryList = ["apples", apples, "banana", banana, "wheat", wheat, "faceWash", faceWash, "towel", towel]
print(groceryList)


#Now we want to print apples and the quantity together, similarly for all other items
#We use the concept of list of lists

groceryListofLists = [["apples", 10], ["banana", 12], ["wheat", 2], ["faceWash", 1], ["towel", 3]]
print(groceryListofLists)
