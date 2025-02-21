



class Parent:
    x,y =  10,20
    def add(self):
        return (self.x + self.y)

class Child(Parent):
    a,b = 200,100
    def sub(self):
        return(self.a-self.b)


obj = Child()

print(obj.sub())
print(obj.add())


