


class Parent:
    x,y =  10,20
    def add(self):
        print(self.x + self.y)
        print("Parent")

class Child(Parent):
    x, y = 100, 200
    def add(self):
        print(self.x + self.y)
        print("Child")
        print(super().y)
        print(super().add())


    


obj = Child()
obj.add()

