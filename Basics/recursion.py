import sys

def fun1():
    print('Function 1')

def fun2():
    print('Function 2')
    fun1()
    # fun2() THIS WILL CAUSE AN ERROR. TRY SETTING RECURSION LIMIT

fun2()

print(sys.getrecursionlimit())
sys.setrecursionlimit(5)
