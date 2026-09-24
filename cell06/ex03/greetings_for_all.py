
def greetings(a="nobel stranger"):
    print(f"Hello, {a}.") if isinstance(a, str) else print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)