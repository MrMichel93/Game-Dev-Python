"""
Practice Problem 2: Buggy Collision Detection
Students need to find and fix the bugs in this code
"""

# Buggy collision detection
WIDTH = 800
HEIGHT = 600

player_x = 100
player_y = 100
player_size = 30

enemy_x = 400
enemy_y = 300
enemy_size = 25

collision_detected = False

def draw():
    screen.fill((0, 0, 0))
    
    # Draw player
    screen.draw.filled_circle((player_x, player_y), player_size, "blue")
    
    # Draw enemy
    screen.draw.filled_circle((enemy_x, enemy_y), enemy_size, "red")
    
    # Show collision status
    if collision_detected == True:  # Bug 1: Redundant comparison (should be just "if collision_detected:")
        screen.draw.text("COLLISION!", (WIDTH/2 - 50, 50), color="yellow", fontsize=40)

def update():
    global player_x, collision_detected
    
    # Move player toward enemy
    player_x += 2
    
    # Check collision
    distance = ((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2) ** 0.5
    
    # Bug 2: Wrong comparison operator (should be < not >)
    if distance > player_size + enemy_size:
        collision_detected = True
    else:
        collision_detected = False  # Bug 3: Logic is backwards
    
    # Bug 4: No bounds checking - player goes off screen
