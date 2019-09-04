from abc import ABC, abstractmethod

class Class1 (ABC):

    @abstractmethod
    def showmessage(self):
        print('From base class')

    @abstractmethod
    def logic(self):
        print('Logic in the derived class')

    @abstractmethod
    def errorchecking(self):
        print('You should implement logic in the child class')

class Class2(Class1):

    def showmessage(self):
        super().showmessage()

    def logic(self):
        print('Custom logic')

    def errorchecking(self):
        print('Try commenting this method')

obj = Class2()
obj.showmessage()
obj.logic()
obj.errorchecking()
