class MyClass:

    def __init__(self):
        self.__Name = ''

    def setname(self, name):
        self.__Name = name

    def getname(self):
        return self.__Name

    name = property(getname, setname)

cls = MyClass()
cls.name = "John Doe"
print(cls.name)
