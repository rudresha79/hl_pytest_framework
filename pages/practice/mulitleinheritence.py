
class P1:
    x,y =  10,20
    def add(self):
        return self.x + self.y

class P2:
    a,b = 200,100
    def sub(self):
        return self.a-self.b

class C1(P1,P2):
    c,d = 10,20
    def mul(self):
        return self.c * self.d



obj = C1()

print(obj.add())
print(obj.sub())
print(obj.mul())

