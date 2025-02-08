def calc_fact(n):
    """
    Recursively computes the factorial of a given number.

    Parameters:
    n (int): The number for which the factorial is to be computed.

    Returns:
    int: The factorial of n.

    Example:
    calc_fact(5) returns 120 (i.e., 5 * 4 * 3 * 2 * 1).
    """
    
    # Base case: factorial of 1 is 1
    if n == 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return calc_fact(n - 1) * n

# Calculate and print the factorial of 5
answer = calc_fact(5)
print(answer)
