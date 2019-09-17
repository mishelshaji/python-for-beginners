class Calc():
    a = 5
    @classmethod
    def add(self):
        print("Additiion")
        self.data = "my data";

    @staticmethod
    def sub():
        print("Substraction")

cl = Calc()
Calc.sub()
