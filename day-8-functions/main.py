def greet(name):
    print(f"Hello, {name}!")
    print("How are you?")
    print("Isn't the weather nice today?")

name = input("What is your name?\n")
greet(name)

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"How is it like in {location}?")

greet_with(location="São Paulo", name="Gabriela")
