# Open a file
fo = open("file.txt", "rb")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.close()