class MyClass:

    a = 'Static method will print this'
    @staticmethod
    def my_static_method():
        print('Hi from static method')
        print(MyClass.a)

    def my_method(self):
        self.a = 'Instance method'
        print(f'Hi from {self.a}')

cls = MyClass()
cls.my_method()
MyClass.my_static_method()
# Hi from Instance method
# Hi from static method
# Static method will print this
