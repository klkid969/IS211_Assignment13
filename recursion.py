def fibonacci(n):
    """Recursive function to return the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    """Recursive function to return the greatest common divisor of a and b"""
    if b == 0:  # Base case
        return a
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    """Recursive function to compare two strings"""
    if not s1 and not s2:  # Both strings are empty
        return 0
    elif not s1:  # s1 is empty
        return -1
    elif not s2:  # s2 is empty
        return 1
    elif s1[0] != s2[0]:  # First characters differ
        return ord(s1[0]) - ord(s2[0])
    else:  # First characters match, compare the rest
        return compareTo(s1[1:], s2[1:])

if __name__ == "__main__":
    # Test Fibonacci
    print("Fibonacci sequence:")
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")
    
    # Test GCD
    print("\nGCD of 48 and 18:", gcd(48, 18))
    print("GCD of 17 and 5:", gcd(17, 5))
    
    # Test String Comparison
    print("\nString comparisons:")
    print('compareTo("apple", "banana"):', compareTo("apple", "banana"))
    print('compareTo("banana", "apple"):', compareTo("banana", "apple"))
    print('compareTo("apple", "apple"):', compareTo("apple", "apple"))