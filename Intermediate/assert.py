a = int(input('Enter a number'))
assert a < 10, "Please enter a number less than 10"
print(f'You entered {a}')

# try:
#     num = int(input('Enter a number: '))
#     assert(num == 0), "Please enter a different number"
#     print(num)
# except AssertionError as msg:
#     print(msg)
