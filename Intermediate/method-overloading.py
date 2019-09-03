class MyClass:

    def myfun(self, msg=None):
        if msg is not None:
            print(f'Hi {msg}')
        else:
            print('Hi')

obj = MyClass()
obj.myfun()
obj.myfun('John')
