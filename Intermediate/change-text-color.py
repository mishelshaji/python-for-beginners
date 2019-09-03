import colorama
from colorama import Fore, Back, Style

colorama.init()

text = "The quick brown fox jumps over the lazy dog"

print(Fore.RED + text)
print(Back.WHITE + text + Style.RESET_ALL)
print(text)
