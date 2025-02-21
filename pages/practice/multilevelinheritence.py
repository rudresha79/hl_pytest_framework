



class Parent:
    x,y =  10,20
    def add(self):
        return (self.x + self.y)

class Child1(Parent):
    a,b = 200,100
    def sub(self):
        return(self.a-self.b)
class Child2(Child1):
    a,b = 200,100
    def mu(self):
        return(self.a*self.b)

obj1 = Child1()
obj2 = Child2()

print(obj1.sub())
print(obj1.add())
print(obj2.mu())
print(obj2.add())


