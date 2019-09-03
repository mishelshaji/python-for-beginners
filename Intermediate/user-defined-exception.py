# class MyException(Exception):
#     pass
#
# try:
#     raise MyException("An error has occurred")
# except MyException as e:
#     print(e)


# class MyError is derived from super class Exception
class MyError(Exception):

    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return ("The error is : "+str(self.value))

try:
    raise MyError(3 * 2)
except MyError as error:
    print(error)
