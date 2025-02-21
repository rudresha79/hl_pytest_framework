import time


class Test_01:
    def test_method1(self,setup):
        print("Method1")
        time.sleep(10)
    def test_method2(self):
        print("Method2")
        x = 121211
        y = str(x)
        rev= ''
        for t in y:
            rev = t + rev
        print(rev)
        
