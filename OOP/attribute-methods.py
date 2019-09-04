class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showdata(self):
        print(f'Name: {self.name}, Age: {self.age}')

cls = MyClass('John Doe', 25)
print(getattr(cls, 'name'))
setattr(cls, 'age', 22)
print(getattr(cls, 'age'))
print(hasattr(cls, 'name'))
delattr(cls, 'age')
print(hasattr(cls, 'age'))
