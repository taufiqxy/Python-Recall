########################################################################################################################
# Data Type: Integer, Float, Complex Number, String
########################################################################################################################

varA = 2
varB = 3.14
varC = 5 + 3j
varD = 'hello, i am back to code in python!'

print(str(varA) + ' || ' + str(type(varA)))
print(str(varB) + ' || ' + str(type(varB)))
print(str(varC) + ' || ' + str(type(varC)))
print(str(varD) + ' || ' + str(type(varD)))

del varA
del varB
del varC
del varD

print()

########################################################################################################################
# Limit Float, Assigment String in Multiple Line
########################################################################################################################

varA = 0.123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
varB = '''
first line string
second line string, \
still in second line
third line string
fourth line string
'''

print(varA)
print(varB)

del varA
del varB

print()

########################################################################################################################
# Boolean
########################################################################################################################

varA = True
varB = False

print('Data Type of Variable A: ' + str(type(varA)))
print(varA == varB)
