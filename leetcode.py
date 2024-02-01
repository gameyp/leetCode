def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome."""
    # Remove all non-alphanumeric characters and convert to lowercase
    s = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the string is equal to its reverse
    return s == s[::-1]

def fibonacci(n: int) -> int:
    """Calculates the nth Fibonacci number."""
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Calculate Fibonacci number using dynamic programming
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]
