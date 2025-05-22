#Dictionary  - {Key:value}
dict1 = {
    "1":"one",
    3:"two",
    2:"Three"
}
print(dict1)
# Accessing the dictionary both key and value
print(dict1["1"])
# Access keys
for x in dict1:
    print(x)
#fetch values from the keys
for x in dict1:
    print(dict1[x])
# prints only values from dictionary
for x in dict1.values():
    print(x)
# print keys along with the value
for x,y in dict1.items():
    print(x,y)
#check key is exist in dictionary or not
if "1" in dict1:
     print("exist")
else:
     print("not exist")
#find number of items in dictionary
print(len(dict1))
#Adding items to dictionary
dict1[4] = "Four"
dict1["5"] = "Five"
print(dict1)
#Remove item from dictionary
dict1.pop("5")
print(dict1)
dict1.pop("1")
print(dict1)
del dict1[2]
print(dict1)
dict1.clear()
print(dict1)   # {}
#Copy dictionary
dict1 = {
    "1":"one",
    2:"two",
    3:"Three"
}
dict2 = dict1.copy()
print(dict2)
dict3 = dict1
print(dict3)
#Get function to fetch the value from the dictionary
print(dict1.get("1"))

