def greeter(name: str) -> str:
    """
    :param name:
    :return:
    """
    return f"Hello, {name}!"


if __name__ == '__main__':
    greeting: str = greeter('Aaron')
    print(greeting)
