a,b=100,200 # Global Variables
class MyClass:
    a,b = 10,20 # Class Variables
    def add(self,a,b): # Local Variables
        print(a + b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b']) #Global Varaibles
    def mul(self):
        print(self.a*self.b)

c = MyClass()
c.add(1,2)
c.mul()
