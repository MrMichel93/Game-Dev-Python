"""
Practice Problem 1: Loop Patterns
Task: Create functions that generate patterns and sequences using loops.

Instructions:
Complete the functions below using loops (for or while).
Each function should work independently and return the correct value.
Do NOT modify the function signatures or add/remove parameters.
"""


def sum_range(start, end):
    """
    Calculate the sum of all numbers from start to end (inclusive).
    Use a loop to calculate the sum.
    
    Args:
        start (int): Starting number
        end (int): Ending number
    
    Returns:
        int: Sum of all numbers in range
    
    Example:
        >>> sum_range(1, 5)
        15
        >>> sum_range(10, 15)
        75
    """
    # TODO: Use a loop to calculate the sum
    pass


def count_multiples(n, limit):
    """
    Count how many multiples of n exist from 1 to limit (inclusive).
    
    Args:
        n (int): The number to find multiples of
        limit (int): The upper limit
    
    Returns:
        int: Count of multiples
    
    Example:
        >>> count_multiples(3, 10)
        3
        >>> count_multiples(5, 25)
        5
    """
    # TODO: Use a loop to count multiples
    pass


def create_sequence(start, count, step):
    """
    Create a list of numbers starting from start, with count elements,
    incrementing by step each time.
    
    Args:
        start (int): Starting number
        count (int): How many numbers to generate
        step (int): Increment between numbers
    
    Returns:
        list: List of numbers in the sequence
    
    Example:
        >>> create_sequence(5, 4, 2)
        [5, 7, 9, 11]
        >>> create_sequence(10, 3, 5)
        [10, 15, 20]
    """
    # TODO: Use a loop to create the sequence
    pass


def find_first_divisible(start, divisor):
    """
    Find the first number >= start that is divisible by divisor.
    Use a while loop.
    
    Args:
        start (int): Starting number to check from
        divisor (int): Number to be divisible by
    
    Returns:
        int: First number divisible by divisor
    
    Example:
        >>> find_first_divisible(10, 3)
        12
        >>> find_first_divisible(20, 7)
        21
    """
    # TODO: Use a while loop to find the number
    pass


def generate_grid_positions(rows, cols, cell_size):
    """
    Generate a list of (x, y) positions for a grid.
    Each cell is cell_size pixels, starting from (0, 0).
    
    Args:
        rows (int): Number of rows
        cols (int): Number of columns
        cell_size (int): Size of each cell in pixels
    
    Returns:
        list: List of (x, y) tuples for each grid position
    
    Example:
        >>> generate_grid_positions(2, 2, 50)
        [(0, 0), (50, 0), (0, 50), (50, 50)]
    """
    # TODO: Use nested loops to generate grid positions
    pass


def repeat_pattern(pattern, times):
    """
    Repeat a list pattern a specified number of times.
    
    Args:
        pattern (list): The pattern to repeat
        times (int): How many times to repeat
    
    Returns:
        list: The repeated pattern
    
    Example:
        >>> repeat_pattern([1, 2, 3], 2)
        [1, 2, 3, 1, 2, 3]
        >>> repeat_pattern(['a', 'b'], 3)
        ['a', 'b', 'a', 'b', 'a', 'b']
    """
    # TODO: Use a loop to repeat the pattern
    pass
