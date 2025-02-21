
class Human:
    def Hello(self,name = None):
        if name is not None:
            print("Hello" + name)
        else:
            print("Hello")

    def Hello(self):
            print("Hello")

a = Human()

a.Hello("aa")
a.Hello()