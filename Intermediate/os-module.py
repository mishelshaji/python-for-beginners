import os

print(os.getcwd())  # PRINTS THE CURRENT WORKING DIRECTORY
# os.mkdir('my python directory')  # CREATES A DIRECTORY IF NOT EXISTS
os.chdir('my python directory')  # CHANGES CURRENT WORKING DIRECTORY
print(os.getcwd())
os.chdir('..')  # GOES BACK TO PARENT DIRECTORY
print(os.getcwd())
print(os.listdir())  # PRINTS FILES AND FOLDERS OF CURRENT DIRECTORY
# print(os.listdir('my dir'))  # LISTS CONTENTS OF THE SPECIFIED DIRECTORY
