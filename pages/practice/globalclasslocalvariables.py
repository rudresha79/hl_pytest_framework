
i,j = 100,200 # Global Variables
class MyClass:
    a,b = 10,20 # Class Variables
    def add(self,x,y): # Local Variables
        print(x + y)
        print(self.a+self.b)
        print(i+j)

    def mul(self):
        print(self.a*self.b)

a = MyClass()
a.add(1,2)
a.mul()