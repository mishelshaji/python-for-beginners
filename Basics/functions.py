def myfun():
    print('myfun: Hello World')

myfun()

def myfn(a, b):
    print(f'myfn: {a+b}')

myfn(10, 20)

def fn(a=5, b=0):
    print(f'fn: {a+b}')

fn()
fn(1, 2)

li = [1, 2, 3, 4, 5]
def fnli(a):
    print('fnli: ')
    for x in a:
        print(x, end=" ")
    return "Completed"

print(f'\n{fnli(li)}')
