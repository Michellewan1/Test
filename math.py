import math

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b. Raises an error if b is 0."""
    if b == 0:

def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent

def square_root(x):
    """Return the square root of x. Raises an error if x is negative."""
    if x < 0:
    return math.sqrt(x)

def factorial(n):
    """Return the factorial of n. Raises an error if n is negative or not an integer."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(n)

def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0

def is_odd(n):
    """Return True if n is odd, False otherwise."""
    return n % 2 != 0

# Example usage (can be removed if using as a module)
if __name__ == "__main__":
    print("Add: 5 + 3 =", add(5, 3))
    print("Subtract: 5 - 3 =", subtract(5, 3))
    print("Multiply: 5 * 3 =", multiply(5, 3))
    print("Divide: 5 / 3 =", divide(5, 3))
    print("Power: 2^3 =", power(2, 3))
    print("Square root of 16 =", square_root(16))
    print("Factorial of 5 =", factorial(5))
    print("Is 4 even?", is_even(4))
    print("Is 7 odd?", is_odd(7))
