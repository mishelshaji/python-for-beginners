# Class
class MyClass:
    name = "Hi from the class"

    # Constructor
    def __init__(self):
        self.age = 22
        gender = 'Male'

    # Method
    def show_data(self):
        print(self.name)
        print(self.age)
        # print(gender)  # Error

# Creating object
obj = MyClass()
obj.show_data()
