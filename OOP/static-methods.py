class MyClass:

    # BY DEFAULT, ALL VARIABLES DECLARED IN CLASS LEVEL ARE STATIC
    # A STATIC METHOD CANNOT CALL NON STATIC METHODS

    def myfun(self):
        print('Non static method')

    @staticmethod
    def fun1():  # YOU DO NOT NEED TO SPECIFY THE SELF PARAMETER
        print('Hello World')

MyClass.fun1()  # THE METHOD CAN BE CALLED WITHOUT CREATING AN OBJECT
