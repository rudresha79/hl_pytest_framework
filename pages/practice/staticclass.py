

class Myclass:
    def method_1(self):
        pass
    @staticmethod
    def method_2(self,num2):
        print(self,num2)


ac = Myclass()
ac.method_1()
Myclass.method_2(10,20)




