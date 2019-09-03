import functools

def mult(x, y):
    print(f'X = {x} and Y = {y}')
    return x*y

ml = [2, 3, 4]
fact = functools.reduce(mult, ml)
print('Factorial of 3: ', fact)

# def do_sum(x1, x2):
#     print(f'X1 = {x1} and X = {x2}')
#     return x1 + x2
# s = functools.reduce(do_sum, [1, 2, 4, 4])
# print(f'The sum is {s}')
