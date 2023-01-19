def calculate(a, b, c, d):
    result = (0.3 * a) + (0.2 * b) + (0.4 * c) + (0.1 * d)
    return result


namaFunction = 'nama module ini adalah \'myModule\''


class User:
    def __init__(self, nama, asal, pekerjaan):
        self.name = nama
        self.originate = asal
        self.job = pekerjaan

    def show_info(self):
        print('Data: ' + str(self.name) + ', ' + str(self.originate) + ', ' + str(self.job))


