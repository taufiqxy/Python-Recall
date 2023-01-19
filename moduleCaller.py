import myModule

result = myModule.calculate(100, 100, 50, 90)

# call method
print(result)

# call attribute
print(myModule.namaFunction)

# call class object
obj = myModule.User('Alfa', 'Padang Panjang', 'Programmer')

obj.show_info()
print(obj.name)
print(obj.originate)
print(obj.job)
