

class Bank:
    def rateofinterest(self):
        return 4

class XBank(Bank):
    def rateofinterest(self):
        return 10

class YBank(Bank):
    def rateofinterest(self):
        return 12,12


ab = XBank()
print(ab.rateofinterest())

ab1 =YBank()
print(ab1.rateofinterest())