class MyClass:

    pb = 5

    def __init__(self):
        self.a = "MyClass property"

    def method1(self):
        self.b = "MyClass property"
        print(self.a)

cls = MyClass()
cls1 = MyClass()
cls.method1()

del cls.a
# cls.method1()  # THIS WILL CAUSE ERROR

del cls1
# cls1  # THIS WILL ALSO CAUSE ERROR
