


def enterage(num):
    if num<0:
        raise ValueError("Only Integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")

print("checking number is even or odd by calling function..")
num=-1
try:
    enterage(num)
except ValueError:
    print("value error exception occured and handled..")
print("program completed....")
