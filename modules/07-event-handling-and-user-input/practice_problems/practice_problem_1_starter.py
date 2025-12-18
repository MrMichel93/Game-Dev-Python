"""
Practice Problem 1: Input State Management
Task: Create functions to manage input states.
"""


def create_input_state():
    """Create an input state dictionary with all keys set to False."""
    # TODO: Return dict with 'up', 'down', 'left', 'right', 'space' all False
    pass


def update_key_state(input_state, key, pressed):
    """Update the state of a specific key."""
    # TODO: Set input_state[key] to pressed
    pass


def is_key_pressed(input_state, key):
    """Check if a key is currently pressed."""
    # TODO: Return input_state.get(key, False)
    pass


def get_movement_direction(input_state):
    """Return (dx, dy) based on arrow keys. -1, 0, or 1 for each."""
    # TODO: Calculate direction from up/down/left/right
    pass


def any_key_pressed(input_state):
    """Check if any key is pressed."""
    # TODO: Return True if any value is True
    pass
