

try:
    div = 2/0
except NameError:
    print(NameError)
finally:
    print("Finally")