names = ['zen', 'abelh', 'luis', 'pedro']


print("Initial list")
print(names)
names.sort()

print("Sorted list")
print(names)

print("Type")
print(type(names))

names.append('Asun')
print(names)

names.extend(['pablo', 'mada'])
names.sort()
print(names)

print(names.index('abelh'))

print(max(names))
print(min(names))
print(len(names))
print(list(('Hola', 'Perro',)))

