from fastmcp import FastMCP
import math

mcp = FastMCP("Calculator")

@mcp.tool
def add(a: float, b: float) -> float: 
    """
    Add two numbers.
    """
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float: 
    """
    Subtract two numbers.
    """
    return a - b

@mcp.tool 
def divide(a: float, b:float) -> float: 
    """
    Divide two numbers.
    """
    if b==0: 
        raise ValueError("Cannot divide by zero")
    return a/b

@mcp.tool 
def multiply(a: float, b:float) -> float: 
    """
    Multiply two numbers.
    """
    return a*b

@mcp.tool 
def power(base: float, exponent: float) -> float:
    """
    Raise a number to a power.
    """
    return pow(base, exponent)

@mcp.tool
def square_root(a: float) -> float: 
    """
        Calculate the square root of a number.
    """
    if a < 0: 
        raise ValueError("Cannot calculate the square root of negative numbers")
    return math.sqrt(a)

@mcp.tool
def factorial(a: int) -> int: 
    """
        Calculate the factorial of a non-negative number.
    """
    if a < 0: 
        raise ValueError("Cannot calculate the factorial of a negative integer")
    return math.factorial(a)

@mcp.tool
def is_prime(n: int) -> bool:
    """
    Check whether the number is prime.
    """
    if n <= 1: 
        return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:  
            return False
    return True


@mcp.tool
def find_gcd(a: int, b:int) -> int:
    """
        Find GCD of two numbers. 
    """
    return math.gcd(a,b)

@mcp.tool
def find_lcm(a: int, b:int) -> int:
    """
        Find GCD of two numbers. 
    """
    return math.lcm(a,b)

@mcp.tool
def modulus(a: float, b: float) -> float:
    """
    Calculate the modulus.
    """
    if b == 0:
        raise ValueError("Cannot calculate modulus with zero")
    return a%b 

if __name__ == "__main__":
    mcp.run()

