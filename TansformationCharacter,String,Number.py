########################################################################################################################
# String Operation: Upper Case and Lower Case
########################################################################################################################
varA = 'Hari Senin Harga Naik'
varA = varA.upper()
print(varA)

varA = varA.lower()
print(varA)

del varA
print()

########################################################################################################################
# String Operation: Clean/Strip WhiteSpace in Left and Right
########################################################################################################################

varA = 'Selamat Datang       \t\n'
varA = varA.rstrip()
print(varA)

varB = '\t\n       Selamat Datang'
varB = varB.lstrip()
print(varB)

varC = '\n\t       Selamat Datang        \t\t\n'
varC = varC.strip()
print(varC)

del varA
del varB
del varC
print()

########################################################################################################################
# String Operation: Check StartWith or EndWith
########################################################################################################################

varA = 'Good Noon Everyone'
print(varA.startswith('Good'))
print(varA.endswith('Everyone'))

del varA
print()

########################################################################################################################
# String Operation: Split and Join
########################################################################################################################

varA = 'hello'
varB = 'i am'
varC = 'a coder'
varD = '|'.join([varA, varB, varC])
print(varD)

varE = varD.split('|')
print(varE)

del varA
del varB
del varC
del varD
del varE
print()

########################################################################################################################
# String Operation: Element Replacement
########################################################################################################################

varA = 'Hello There I Am a Programmer!'
varA = varA.replace('Programmer', 'Code Writer')
print(varA)

del varA
print()

########################################################################################################################
# String Operation: String Checking
########################################################################################################################

varA = 'DILARANG MASUK'
print(varA.isupper())
print(varA.islower())
print()

print('Sungai'.isalpha())
print('Sungai Amazon Sangat Pajang'.isalpha())
print('hola4334'.isalnum())
print('hola 4334'.isalnum())
print('911'.isdecimal())
print('911'.isnumeric())
print('   '.isspace())
print('\t\n'.isspace())
print('Piramida Giza Mesir'.istitle())

del varA
print()

########################################################################################################################
# String Operation: Zero Fill (zfill)
########################################################################################################################

varA = 55
print(str(varA).zfill(4))
print('300'.zfill(4))
print('0.05'.zfill(5))
print('0xx089'.zfill(7))
print('-94'.zfill(4))
print('-0.13'.zfill(6))

del varA
print()

########################################################################################################################
# String Operation: Adjust Text
########################################################################################################################

varA = 'hello'
print(varA.rjust(10, '-'))
print(varA.ljust(10, '-'))
print(varA.center(11, '-'))

del varA
print()
