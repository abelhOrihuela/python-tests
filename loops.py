numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print("Number", number)


run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1
