def fun1(*a):
    print(a)
    print(a[0])

def fun2(**kw):
    print(kw)
    print(kw['msg'], kw['name'], end=" ")

fun1('Hi')
fun2(msg="Hi", name="John")
