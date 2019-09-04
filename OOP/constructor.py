class MyClass:

    def __init__(self, message="Default"):
        self.a = message
        MyClass.b = "From MyClass"

    def print_msg(self):
        print(self.a, MyClass.b, end="\n")

obj = MyClass()
obj.print_msg()

obj1 = MyClass("Hi there")
obj1.print_msg()
