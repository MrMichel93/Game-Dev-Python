"""
Module 2 Example: Boundary Checking with Conditionals
Demonstrates how conditionals control player movement within game boundaries
"""

WIDTH = 800
HEIGHT = 600

# Player state
player_x = 400
player_y = 300
player_size = 30
player_speed = 5

# Movement flags
move_left = False
move_right = False
move_up = False
move_down = False

def draw():
    screen.fill((0, 100, 0))  # Green background
    
    # Draw boundaries
    screen.draw.rect(Rect(0, 0, WIDTH, HEIGHT), "white")
    
    # Change color if at boundary
    color = "red" if is_at_boundary() else "blue"
    screen.draw.filled_circle((player_x, player_y), player_size, color)
    
    # Display position and status
    screen.draw.text(f"Position: ({player_x}, {player_y})", 
                    (10, 10), color="white", fontsize=25)
    
    if is_at_boundary():
        screen.draw.text("At Boundary!", (10, 40), color="red", fontsize=25)
    
    # Instructions
    screen.draw.text("Use Arrow Keys to Move", 
                    (WIDTH/2 - 100, HEIGHT - 30), 
                    color="white", fontsize=20)

def update():
    global player_x, player_y
    
    # Calculate new position
    new_x = player_x
    new_y = player_y
    
    if move_left:
        new_x -= player_speed
    if move_right:
        new_x += player_speed
    if move_up:
        new_y -= player_speed
    if move_down:
        new_y += player_speed
    
    # Only update position if within boundaries
    if new_x >= player_size and new_x <= WIDTH - player_size:
        player_x = new_x
    if new_y >= player_size and new_y <= HEIGHT - player_size:
        player_y = new_y

def is_at_boundary():
    """Check if player is touching any boundary"""
    return (player_x <= player_size or 
            player_x >= WIDTH - player_size or
            player_y <= player_size or
            player_y >= HEIGHT - player_size)

def on_key_down(key):
    global move_left, move_right, move_up, move_down
    if key == keys.LEFT:
        move_left = True
    elif key == keys.RIGHT:
        move_right = True
    elif key == keys.UP:
        move_up = True
    elif key == keys.DOWN:
        move_down = True

def on_key_up(key):
    global move_left, move_right, move_up, move_down
    if key == keys.LEFT:
        move_left = False
    elif key == keys.RIGHT:
        move_right = False
    elif key == keys.UP:
        move_up = False
    elif key == keys.DOWN:
        move_down = False
