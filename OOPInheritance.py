""" Dicoding """


class Kalkulator:
    """contoh kelas kalkulator sederhana. anggap kelas ini tidak boleh diubah!"""

    def __init__(self, nilai=0):
        self.nilai = nilai

    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:  # kalkulator sederhana hanya memroses sampai 9
            print('kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
        return self.nilai


myCalculator = Kalkulator()
print(myCalculator.tambah_angka(7, 5))

print()


class KalkulatorTambahKali(Kalkulator):
    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai


myCalculator2 = KalkulatorTambahKali()
print(myCalculator2.tambah_angka(5, 4))
print(myCalculator2.kali_angka(5, 4))
