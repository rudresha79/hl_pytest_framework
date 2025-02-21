

class MyClass:
    def __init__(self,name,age,salary):
            self.name = name
            self.age = age
            self.salary = salary
    def display(self):
        print(self.name,self.age,self.salary)

obj =  MyClass("a",1,1000)

obj.display()

