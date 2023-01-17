########################################################################################################################
# Brancing
########################################################################################################################

def hitung(a, b, c):
    nilai = (0.2 * a) + (0.5 * b) + (0.3 * c)
    if nilai >= 70:
        print('Selamat Anda Lulus!')
    elif 60 <= nilai < 70:
        print('Anda Belum Lulus, Namun Anda Masih Bisa Melakukan Perbaikan')
    else:
        print('Mohon Maaf, Anda Gagal Dalam Tes Ini')
    return nilai


nilaiAkhir = hitung(80, 47, 97)
print('Nilai Akhir Anda Adalah: ' + str(nilaiAkhir))

print()

########################################################################################################################
# Ternary Operator
########################################################################################################################

myCond = False
msg = 'Selamat Datang' if myCond else 'Selamat Jalan'
print(msg)

print()

########################################################################################################################
# Ternary Tuples (Not Recommended To Use in Common Case)
########################################################################################################################

myCond = False
msg = ('Hello', 'Hai')[myCond]
print(msg)

print()

########################################################################################################################
# ShortHand Ternary
########################################################################################################################

dataReturn = None  # change to None
myData = dataReturn or 'Data Not Found'
print(myData)
