list_obj = [10,20,21,2,11]
even_numbers = [x for x in list_obj if x%2==0]
print(even_numbers)
strng = 'Hello water level malayalam'
lis = strng.split()
polin = [word for word in lis if word==word[::-1] and len(word) > 1]
print(' '.join(polin))
rev = "hello"
print(rev[::1])
nested_list= [['1','2'],['o','3','4']]

for x in nested_list:
    for y in x:
        print(y)
str = ''
for x in nested_list:
    str = str + ' '.join(x) + "-"
print(str)

x = [10,20,1,3,22,30]

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i] > x[j]:
            temp = x[j]
            x[j] = x[i]
            x[i] = temp
print(x)

y = [[1,2,3],[4,5,6],[7,8,9]]

z = [[1,2,3],[4,5,6],[7,8,9]]

g = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(y)):
    for j in range(len(y[i])):
        g[i][j] = y[i][j] + z[i][j]

for k in g:
    print(k)

nested_list = [["a", 1], ["b", 2], ["c", 3]]
dictionary = dict(nested_list)
print(dictionary)


nested_list = [["a", 1, 2], ["b", 3, 4], ["c", 5, 6]]
dictionary = {item[0]: item[1:] for item in nested_list}
print(dictionary)






