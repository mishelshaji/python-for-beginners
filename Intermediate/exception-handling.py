try:
    # print(a)
    pass
except:
    print('An error occurred')

try:
    # print(a)
    pass
except NameError:
    print('Variable is not declared')

try:
    10/0
except ArithmeticError:
    print('An arithmetic error has occurred')
finally:
    print('I will be executed even if there is no error')

try:
    raise ArithmeticError("An error has occurred")
except Exception as e:
    print(e)

try:
    # raise Exception("An error occurred")
    pass
finally:
    pass

try:
    raise Exception("Some error")
except Exception as e:
    print(e)

try:
    a = int(input("Enter a positive number"))
    if a < 0:
        raise ValueError("Number is not valid")
    if a == 0:
        raise ArithmeticError("Division by zero error")
except (ValueError , ArithmeticError):
    print("A value error or arithmetic error has occured")