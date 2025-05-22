
unlist = (55,1,2,4,54,3,3,33,3,44)
print(tuple((unlist)))
print(list(set(unlist)))
print(list(dict.fromkeys(unlist)))
my_dict = {"a": 1, "b": 2, "c": 3}
keys_list = list(my_dict.keys())
keys_list1 = list(my_dict.values())
print(keys_list1.sort())
print(keys_list + keys_list1)


ins = input("Enter value")
if ins ==ins[::-1]:
    print("polindra")
else:
    print("not polindra")

