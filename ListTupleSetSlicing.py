########################################################################################################################
# List
########################################################################################################################

varA = ['first', 10, 2.7, 2 + 5j, 'last']
print(varA)
print(varA[0])
print(varA[-1])
print(varA[-2])
print(varA[2:4])
print(varA[:4])
print(varA[0:-1:2])

varA[2] = 3.14
print(varA[2])

varA.append('last added by append')
print(varA)

del varA[0]
print(varA)

del varA
print()

########################################################################################################################
# Tuple (Immutable String, Can't Assignment)
########################################################################################################################

varA = ('fist', 2, 'third', 4, 'fifth', 6)
print(varA)
print(varA[0])
print(varA[0:])
print(varA[0:-1])

del varA
print()

########################################################################################################################
# Set (Unique List, Can't Access Element)
########################################################################################################################

varA = {1, 2, 3, 4, 5, 1, 4, 9, 9, 9, 4, 5, 6}
print(varA)

del varA
print()

########################################################################################################################
# Dictionary
########################################################################################################################

varA = {'index1': 1, 2: 2, 'index3': 3, 4: 4, 'index5': 5, 6: 6}
print(varA)
print(varA['index5'])

del varA
print()