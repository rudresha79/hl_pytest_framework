numbers = {x: x**2 for x in range(10) if x % 2 == 0}
print(numbers)


original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)

s= {}
for k, v in original.items():
    s[k]=v
    print(s[k])
print(s)

nested_list = [["a", 1, 2], ["b", 3, 4], ["c", 5, 6]]
dictionary = {item[0]: item[1:] for item in nested_list}
print(dictionary)

x = [[1,1,2],[2,3,4]]

a = {y[0]:y[1:] for y in x if y[0]%2==0}

print(a)