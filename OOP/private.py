class SeeMee:

    def youcanseeme(self):
        return 'you can see me'

    def __youcannotseeme(self):
        return 'you cannot see me'


Check = SeeMee()
print(Check.youcanseeme())
# you can see me
# print(Check.__youcannotseeme())
# AttributeError: 'SeeMee' object has no attribute '__youcannotseeme'


##########BUT YOU CAN STILL ACCESS IT################
print(Check._SeeMee__youcannotseeme())
