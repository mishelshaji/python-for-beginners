from builtins import list, filter

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))  # => 13


def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11))  # => 22

myset = {1, 2, 3, 4, 10, 123, 22}
print(myset)
lst = list(map(lambda i: i % 2 == 0, myset))
lst1 = list(filter(lambda i: i % 2 == 0, myset))
print(lst)
print(lst1)


