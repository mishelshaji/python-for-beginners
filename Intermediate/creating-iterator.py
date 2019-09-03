class MyClass:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a <= 3:
            t = self.a
            self.a += 1
            return t
        else:
            raise StopIteration

obj = MyClass()
i = iter(obj)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
# print(next(i))
