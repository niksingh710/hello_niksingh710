def say_hello(name=None):
    if name:
        return f"Hello, {name} :)"
    return f"Hello, World! :)"


if __name__ == '__main__':
    print(say_hello("Nikhil Singh"))
