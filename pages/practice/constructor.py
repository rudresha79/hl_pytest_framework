

class Myclass:

    def __init__(self):
        print("This is constructor method")

    def method_1(self,name):
        print("name")

    def method_2(self,x,y):
        return(x+y)


a = Myclass()
a.method_1("AA")
b = a.method_2(  9 , 9)
print(b)

