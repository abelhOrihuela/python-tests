print("I will now count my chickens:")
print("Hens: ", 25 + 30 / 6)
print("Roosters:", 100 - 25 * 3 % 4)

print("5 is major to 3:", 5 > 3)

cars = 4
number_of_places_for_car = 4

total_places = cars * number_of_places_for_car

print("There are ", cars, "cars availbales")
print("We can transport ", total_places, "people today")
print("================================================")
print(f"Therea are {cars} cars availables")
print(f"We can transport {total_places} people today")

print(round(3/5))

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3 ,4))
print(formatter.format(formatter, 2, 3 ,4))