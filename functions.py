# arguments for functions
def my_function(name="Anonymous", description="Nothing"):
    print("My name is", name, "And Im", description)

# my_function("Abel", "Fullstack (people says)")
# my_function(description = "Fullstack (people says)", name = "Abel")
# my_function()

# infinite arguments


def print_people(*people):
    for person in people:
        print("This person is", person)

# print_people("Nick", "Dan", "Jack")


def do_math(num1, num2):

    return num1 + num2


math1 = do_math(2, 5)

print("Sum", math1)
