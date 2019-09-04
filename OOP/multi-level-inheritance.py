class A:

    __m = 'Private'
    def __init__(self):
        self.msg = 'Class 1'

    def fun1(self):
        print('Function 1')

class B (A):

    def fun2(self):
        print('Function 2')

class C (B):

    def fun3(self):
        self.fun1()
        self.fun2()
        # print(self.__m)

obj = C()
obj.fun3()
