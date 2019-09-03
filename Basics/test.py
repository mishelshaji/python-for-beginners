class InvalidUsernameError(Exception):
    code = '0x08693F'
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return str(self.message).upper()

try:
    if 10 < 11:
        raise InvalidUsernameError("A custom error")
except InvalidUsernameError as e:
    print(e)

