ar = [1, 2, 3, 4, 5]
print(ar)  # [1, 2, 3, 4, 5]

# MANAGING ARRAY ELEMENTS
ar.append(6)  # ADD AN ELEMENT [1, 2, 3, 4, 5, 6]
ar.remove(6)  # REMOVES AN ELEMENT => [1, 2, 3, 4, 5]
ar[0] = "One"  # MODIFY AN ELEMENT => ['One', 2, 3, 4, 5]
print(ar)  # ['One', 2, 3, 4, 5]

# REMOVE
# => REMOVES THE OCCURRENCE OF AN ELEMENT
ar.append('One')  # ['One', 2, 3, 4, 5, 'One']
ar.remove('One')  # REMOVES ONLY THE FIRST OCCURRENCE
print(ar)  # [2, 3, 4, 5, 'One']


# INSERT
# => INSERTS AN ELEMENT AT THE SPECIFIED INDEX
# => IF AN INDEX IS NOT FOUND, ELEMENT WILL BE ADDED TO THE END
ar.insert(0, 'One')  # ['One', 2, 3, 4, 5, 'One']
ar.insert(20, 'One')  # ['One', 2, 3, 4, 5, 'One', 'One']
print(ar)  # ['One', 2, 3, 4, 5, 'One', 'One']

# DEL
# => DELETES FROM THE SPECIFIED INDEX
del ar[6]  # ['One', 2, 3, 4, 5, 'One']
print(ar)  # ['One', 2, 3, 4, 5, 'One']
# del ar => DELETES THE LIST

# REVERSE
ar.reverse()  # ['One', 5, 4, 3, 2, 'One']
print(ar)  # ['One', 5, 4, 3, 2, 'One']

# LEN
print(len(ar))  # => 6

# POP
ar.pop(5)  # REMOVES THE FIFTH ELEMENT
print(ar)  # => ['One', 5, 4, 3, 2]

# LOOPING
for e in ar:
    print(e, end=" ")  # => One 5 4 3 2
