class A:

    __m = 'Private'
    def __init__(self):
        self.msg = 'Class 1'

    def fun1(self):
        print('Function 1')

    def same(self):
        print('Same A')

class B:

    def fun2(self):
        print('Function 2')

    def same(self):
        print('Same B')

class C (A, B):

    def fun3(self):
        self.fun1()
        self.fun2()
        self.same()
        # print(self.__m)

    # def same(self):
    #    print("override")

obj = C()
obj.fun3()
