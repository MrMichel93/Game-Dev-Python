"""
Practice Problem 2: Particle System Functions
Task: Create functions to manage particle effects using loops.

Instructions:
Complete the functions below for a simple particle system.
Each function should work independently and return the correct value.
"""


def create_particles(count, x, y):
    """
    Create a list of particle dictionaries at position (x, y).
    Each particle should have: {'x': x, 'y': y, 'speed': 2, 'alive': True}
    
    Args:
        count (int): Number of particles to create
        x (int): X position
        y (int): Y position
    
    Returns:
        list: List of particle dictionaries
    
    Example:
        >>> particles = create_particles(2, 100, 200)
        >>> len(particles)
        2
        >>> particles[0]['x']
        100
    """
    # TODO: Create and return list of particles
    pass


def update_particles(particles):
    """
    Update all particles by moving them down (increase y by speed).
    Mark particles as not alive if y > 600.
    
    Args:
        particles (list): List of particle dictionaries
    
    Returns:
        None (modifies particles in place)
    
    Example:
        >>> particles = [{'x': 100, 'y': 590, 'speed': 15, 'alive': True}]
        >>> update_particles(particles)
        >>> particles[0]['alive']
        False
    """
    # TODO: Update all particles
    pass


def count_alive_particles(particles):
    """
    Count how many particles are still alive.
    
    Args:
        particles (list): List of particle dictionaries
    
    Returns:
        int: Count of alive particles
    
    Example:
        >>> particles = [{'alive': True}, {'alive': False}, {'alive': True}]
        >>> count_alive_particles(particles)
        2
    """
    # TODO: Count alive particles
    pass


def remove_dead_particles(particles):
    """
    Create a new list containing only alive particles.
    
    Args:
        particles (list): List of particle dictionaries
    
    Returns:
        list: New list with only alive particles
    
    Example:
        >>> particles = [{'alive': True}, {'alive': False}, {'alive': True}]
        >>> alive = remove_dead_particles(particles)
        >>> len(alive)
        2
    """
    # TODO: Return list of only alive particles
    pass


def get_particle_positions(particles):
    """
    Get a list of (x, y) tuples for all particles.
    
    Args:
        particles (list): List of particle dictionaries
    
    Returns:
        list: List of (x, y) tuples
    
    Example:
        >>> particles = [{'x': 10, 'y': 20}, {'x': 30, 'y': 40}]
        >>> get_particle_positions(particles)
        [(10, 20), (30, 40)]
    """
    # TODO: Extract and return positions
    pass
