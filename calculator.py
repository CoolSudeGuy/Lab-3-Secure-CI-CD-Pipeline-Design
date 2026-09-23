def add(first_number: float, second_number: float) -> float:
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number: float, second_number: float) -> float:
    """Return the difference between two numbers."""
    return first_number - second_number


def multiply(first_number: float, second_number: float) -> float:
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number: float, second_number: float) -> float:
    """Return the quotient of two numbers."""
    if second_number == 0:
        raise ValueError("Cannot divide by zero.")

    return first_number / second_number


if __name__ == "__main__":
    print(f"Build verification result: 2 + 3 = {add(2, 3)}")
