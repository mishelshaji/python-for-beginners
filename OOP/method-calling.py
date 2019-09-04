import sys

class MyClass:

    def method1(self):
        print('Method 1')

    def method2(self):
        print('Method 2')

    def method3(self):
        self.method1()
        self.method2()
        #self.method3()

cls = MyClass()
cls.method3()

# SET RECURSION LIMIT
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5)
# print(sys.getrecursionlimit())