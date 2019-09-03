class MyClass:
    """Ths is a class"""

    def myfun(self):
        """This is myfun"""

def demofunc():
    """This is a demo function"""

print(MyClass.__doc__)
print(demofunc.__doc__)

# PRINTING DOCSTRINGS OF A CLASS AND ITS METHODS
obj = MyClass()
print(obj.__doc__)
# DISPLAYING DOCSTRING OF A METHOD
print(obj.myfun.__doc__)