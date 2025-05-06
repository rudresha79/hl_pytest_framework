lis_obj = [10,6,7,19,5]
for i in range(len(lis_obj)):
    for j in range(i+1,len(lis_obj)):
        if lis_obj[i]> lis_obj[j]:
            temp = lis_obj[j]
            lis_obj[j] = lis_obj[i]
            lis_obj[i] = temp
print(lis_obj)
print(lis_obj[-1])







