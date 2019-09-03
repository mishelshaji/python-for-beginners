def myGenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30

gen = myGenerator()
next(gen)
next(gen)
next(gen)
# next(gen)

next(myGenerator())
next(myGenerator())
next(myGenerator())

myGenerator()
myGenerator()
myGenerator()

