#it is the representation of the array in python it will gave item in a listed format
#eg:
shopping=["bread","coffee","sugar"]
print(shopping)
for i in shopping:
    print(i)
#append is a keyword used to adding a new element into the list
#adding a new element into the list of shopping
shopping.append("curd")
print(shopping)
for i in shopping:
    print(i)
print(shopping[1])
#insert is a function used to insert an element into the list and also put the element at specific position
shopping.insert(0,"oil")
print(shopping)
#count is a function that is used to find out how many same numbers are present inside a list
age=[1,2,3,4,1,4,43,3,5,6,5,6,6,6,5,4,8,90]
a=age.count(5)
print(age)
print(a)
#len is a function used to find the length of the elements in the list
b=len(age)
print(b)
for i in range(len(shopping)):
    print(shopping[i])
#sorting is a function used to sort elements in a list in increasing or decreasing order
age.sort()
print("sorted elements are : \t",age)
#reverse is a function used to reverse the list
age.reverse()
print("reverse list : \t",age)
students=["ray","shiv","mah","aahna","adhitya","keerthy","lekha"]
for i in students:
    print(i)
    students.sort()
    print(students)
students.insert(0,"joy")
print(students)
#slicing is a function used to print values in the list from a specific start value to specific end value
#SYNTAX :
    #list_name[start_index : end_index + 1]
print(students[1:5])
