"""
Practice Problem 3: Health System Solution
Extended version with armor and shield mechanics
"""

# Extended health system
WIDTH = 800
HEIGHT = 600

# Player variables
player_health = 100
max_health = 100
armor = 50  # Added: Armor variable
shield_active = True  # Added: Shield status variable

def draw():
    screen.fill((50, 50, 50))  # Gray background
    
    # Draw health bar background
    screen.draw.filled_rect(Rect(10, 10, 200, 30), "red")
    
    # Draw current health
    health_width = (player_health / max_health) * 200
    screen.draw.filled_rect(Rect(10, 10, health_width, 30), "green")
    
    # Draw health text
    screen.draw.text(f"Health: {player_health}/{max_health}", (15, 15), color="white")
    
    # Added: Display armor value
    screen.draw.text(f"Armor: {armor}", (15, 50), color="cyan", fontsize=20)
    
    # Added: Display shield status
    shield_status = "Active" if shield_active else "Down"
    shield_color = "yellow" if shield_active else "gray"
    screen.draw.text(f"Shield: {shield_status}", (15, 75), color=shield_color, fontsize=20)

def update():
    global player_health, armor, shield_active
    
    # Calculate damage based on shield status
    damage = 1
    if shield_active:
        damage = damage / 2  # Modified: Reduce damage by half if shield is active
    
    # Apply damage to armor first, then health
    if armor > 0:
        armor -= damage
        if armor < 0:
            armor = 0
    else:
        player_health -= damage
    
    # Modified: Deactivate shield when armor reaches 0
    if armor <= 0:
        shield_active = False
    
    # Prevent health from going below 0
    if player_health < 0:
        player_health = 0
    
    # Bonus: Regenerate health slowly when below 50 and shield is active
    if player_health < 50 and shield_active:
        player_health += 0.1
        if player_health > max_health:
            player_health = max_health
