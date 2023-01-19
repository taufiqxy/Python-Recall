""" dicoding """


# kelas dasar
class Kalkulator:
    """contoh kelas kalkulator sederhana. anggap kelas ini tidak boleh diubah!"""

    def __init__(self, nilai=0):
        self.nilai = nilai

    def tambah_angka(self, angka1, angka2):
        print('method tambah_angka di kelas dasar terpanggil...')
        self.nilai = angka1 + angka2
        if self.nilai > 9:  # kalkulator sederhana hanya memroses sampai 9
            print('kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
        return self.nilai


# kelas turunan dengan kondisi masih memanfaatkan bagian method class dasar
class KalkulatorTambah(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""

    def tambah_angka(self, angka1, angka2):
        if angka1 + angka2 <= 9:  # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
            super().tambah_angka(angka1, angka2)  # panggil fungsi dari Kalkulator lalu isi nilai
        else:  # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            print('method tambah_angka di kelas turunan terpanggil...')
            self.nilai = angka1 + angka2
        return self.nilai


# create object
myCalculator = KalkulatorTambah()
print(myCalculator.tambah_angka(6, 8))
