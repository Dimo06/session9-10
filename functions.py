def greet(name):
    """
    simple greet function, prints hello
    :param name: string
    :return:
    """
    print(f"Hello, {name}")

greet("Bogdan")


def special_op(x=10, y=10, z=10):
    """
    some special operation
    :param x: int or float
    :param y: int or float
    :param z: int or float
    :return: the result of the operation
    """
    return x * y + z

result = special_op(2, 3, 4)
print(result)
print()

greet(special_op(2,3,4))

def factorial(n):
    """
    factorial of a number
    :param n: int number
    :return: the value of n
    """
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

