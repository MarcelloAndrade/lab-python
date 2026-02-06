import random

def add(x: int) -> int:
    return x + 2

def subtract(x: int) -> int:
    raise NotImplementedError("This function is not yet implemented.")

def multiply(x: int) -> int:
    value = multiply_value()
    return x * value

def multiply_value() -> int:
    return 2 * random.randint(1, 5)