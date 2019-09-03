# REVERSE OF A STRING
# METHOD 1
a=input('Enter a string')
res=''
for i in a:
    res = i+res
print(res)
# METHOD 2
# REFER slicing
print(a[::-1])
