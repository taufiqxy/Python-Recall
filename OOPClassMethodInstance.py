class Hitung:
    i = 76
    my_list = [2, 3, 5, 7, 11, 13, 19, 31]

    def __init__(self, a):
        self.a = a
        self.i = 'ini adalah nilai i'  # this value will replace i in above function
        self.x = 'ini adalah nilai x'

    def hello(self, x, y):
        x = x ** 2
        y = y ** 2
        mystr = 'nilai x dan y adalah: ' + str(x) + ', ' + str(y) + ', nilai x: ' + str(self.x)
        return mystr

    @classmethod
    def hai(cls, v1, v2):
        return 'nilai v1 = {} dan v2 = {}'.format(v1, v2)

    @staticmethod
    def hola(nilai1, nilai2):
        hasil = nilai1 + nilai2
        return 'jumlah kedua nilai adalah {}'.format(hasil)


# explore class
obj = Hitung('nilai a')
print(obj.hello(4, 5))
print(obj.i)
print(obj.my_list)

print()

obj.i = 100
obj.my_list = [1, 2, 3, 4, 5, 6, 7, 9, 10]

print(obj.i)
print(obj.my_list)
print(obj.x)

print()

# equivalent way to acces method
obj2 = Hitung('nilai a')
print(Hitung.hello(obj2, 90, 100))

# class method
print(Hitung.hai(6, 7))

h = Hitung('nilai a')
print(h.hai(6, 7))

# static method
print(Hitung.hola(9, 10))

h = Hitung('nilai a')
print(h.hola(9, 10))
