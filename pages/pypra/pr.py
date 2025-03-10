# E = input("enter number:")
# print(E)


# A tuple is a collection which is ordered and unchangeable. it means that the items have a defined order, and that order will not change.
tuple_x = (3,2,3)
print(tuple_x)
print(len(tuple_x))
for i in range(len(tuple_x)):
    print(i)
    print(tuple_x[i])
print(type(tuple_x))
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
print(thistuple[2:4])
print(thistuple[2:])
print(thistuple[:-1])

# We cant directly add we should convert it to list,then append convert it back to tuple
a = list(thistuple)
a.append("o")
thistuple =tuple(a)
print(thistuple)


# List
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Note: There are some list methods that will change the order, but in general: the order of the items will not change.
# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist.append("aaaa")
print(thislist)
thislist.insert(1, "orange")
print(thislist)
thislist.remove("orange")
print(thislist)
#Remove Specified Index
thislist.pop((1))
print(thislist)
thislist.reverse()
print(thislist)
thislist.sort()
print(thislist)


# Set
# Sets are used to store multiple items in a single variable.
#A set is a collection which is unordered, unchangeable*, and unindexed.
#* Note: Set items are unchangeable, but you can remove items and add new items.


thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
thisset.add("orange")
print(thisset)
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)