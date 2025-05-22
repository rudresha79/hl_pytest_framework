def output(word):
    print(word[::-1])
    if word == word[::-1]:
        return word
abc = input("Enter a string:")
a =  abc.split()
even_numbers = [word for word in a if output(word) and len(word) > 1]
print(even_numbers)
print(''.join(even_numbers))



