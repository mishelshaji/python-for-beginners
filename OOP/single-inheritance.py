class A:

    def fun1(self):
        print('Function 1')

class B (A):

    def fun2(self):
        print('Function 2')

obj = B()
obj.fun1()
obj.fun2()