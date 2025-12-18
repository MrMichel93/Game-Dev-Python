"""
Practice Problem 1: Boundary Checker
Task: Create functions that check if game objects are within boundaries.

Instructions:
Complete the functions below to check various boundary conditions.
Each function should work independently and return the correct value.
Do NOT modify the function signatures or add/remove parameters.
"""


def is_within_bounds(x, y, width, height):
    """
    Check if a point (x, y) is within the rectangular bounds.
    
    Args:
        x (int): X coordinate to check
        y (int): Y coordinate to check
        width (int): Width of the boundary
        height (int): Height of the boundary
    
    Returns:
        bool: True if point is within bounds (0 <= x < width and 0 <= y < height)
    
    Example:
        >>> is_within_bounds(100, 200, 800, 600)
        True
        >>> is_within_bounds(-10, 200, 800, 600)
        False
    """
    # TODO: Check if the point is within bounds
    pass


def is_at_edge(x, y, width, height, margin=10):
    """
    Check if a point is near the edge of the boundary within the margin.
    
    Args:
        x (int): X coordinate to check
        y (int): Y coordinate to check
        width (int): Width of the boundary
        height (int): Height of the boundary
        margin (int): Distance from edge to be considered "at edge" (default: 10)
    
    Returns:
        bool: True if point is within margin pixels of any edge
    
    Example:
        >>> is_at_edge(5, 300, 800, 600, 10)
        True
        >>> is_at_edge(100, 300, 800, 600, 10)
        False
    """
    # TODO: Check if the point is near any edge
    pass


def clamp_to_bounds(x, y, width, height):
    """
    Clamp coordinates to keep them within bounds.
    If x or y are out of bounds, adjust them to the nearest valid value.
    
    Args:
        x (int): X coordinate to clamp
        y (int): Y coordinate to clamp
        width (int): Width of the boundary
        height (int): Height of the boundary
    
    Returns:
        tuple: (clamped_x, clamped_y)
    
    Example:
        >>> clamp_to_bounds(900, 300, 800, 600)
        (799, 300)
        >>> clamp_to_bounds(-10, 650, 800, 600)
        (0, 599)
    """
    # TODO: Clamp coordinates to bounds
    pass


def get_quadrant(x, y, width, height):
    """
    Determine which quadrant of the screen a point is in.
    Quadrants: "top-left", "top-right", "bottom-left", "bottom-right"
    
    Args:
        x (int): X coordinate
        y (int): Y coordinate
        width (int): Width of the boundary
        height (int): Height of the boundary
    
    Returns:
        str: The quadrant name
    
    Example:
        >>> get_quadrant(100, 100, 800, 600)
        'top-left'
        >>> get_quadrant(700, 500, 800, 600)
        'bottom-right'
    """
    # TODO: Determine the quadrant
    pass


def check_collision_circle(x1, y1, radius1, x2, y2, radius2):
    """
    Check if two circles collide using distance formula.
    Circles collide if distance between centers < sum of radii.
    
    Args:
        x1, y1 (int): Center of first circle
        radius1 (int): Radius of first circle
        x2, y2 (int): Center of second circle
        radius2 (int): Radius of second circle
    
    Returns:
        bool: True if circles collide
    
    Example:
        >>> check_collision_circle(100, 100, 20, 130, 100, 20)
        True
        >>> check_collision_circle(100, 100, 20, 200, 100, 20)
        False
    """
    # TODO: Calculate distance and check collision
    pass
