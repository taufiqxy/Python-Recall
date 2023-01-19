########################################################################################################################
# #1
########################################################################################################################

def calculate(v):
    v = v * v
    return v


def cetak(a, b):
    print('hasil kuadarat dari {} adalah {}'.format(a, b))


value = 7
hasil = calculate(value)
cetak(value, hasil)

print()

########################################################################################################################
# #2
########################################################################################################################


def ubah_daftar(myList):
    myList = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    print('nilai variable \'myList\' di dalam function: ' + str(myList))
    return None


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ubah_daftar(myList)
print('nilai variable \'myList\' di luar function: ' + str(myList))

print()

########################################################################################################################
# #3
########################################################################################################################


def printinfo(*args, **kwargs):
    for a in args:
        print('argumen posisi {}'.format(a))
    for key, value in kwargs.items():
        print('argumen kata kunci {}:{}'.format(key, value))
    print('i am in')


# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{'i': 7, 'j': 8})

print()

########################################################################################################################
# #4 Anonymous Function
########################################################################################################################

hasil = lambda v1, v2: (0.5 * v1) + (0.5 * v2)
print(hasil(100, 100))
print(hasil(30, 70))