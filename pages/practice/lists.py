#List
List = [1,2,3]
#Add an itme to the list
List.append(4)
print(List)
#Insert to the list at the index
List.insert(2,"5")
print(List)
#Remove using pop - removes last item
List.pop()
print(List)
#at index
List.pop(0)
print(List)
#Remove an item
List.remove('5')
print(List)
del List[0]
print(List)
#el List
mylist = ["apple", "banana", "cherry"]
mylist.clear()
print(mylist)
mylist = ["apple", "banana", "cherry"]
mylist1 = mylist.copy()
print(mylist1)
#Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
    print(list1)
#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
#Tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)
a= 1,2,3
print(a)
b = list(a)
b[0]= 100
a = tuple(b)
print(a)
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)
mytuple = ("apple", "banana", "cherry")
if "apple" in mytuple:
    print("Yes, 'apple' is in the fruits tuple")
#Join two tuples:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
List = [1,2,3,3]
print(List)
List1 = (1,2,3,3)
print(List1)
for i in range(10):
    print(i)
