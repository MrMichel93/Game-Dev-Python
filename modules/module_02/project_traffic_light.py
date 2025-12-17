"""
Module 2 Project: Traffic Light Reaction Game
Complete solution demonstrating conditional logic
"""

import random

WIDTH = 800
HEIGHT = 600

# Traffic light states
RED = "red"
YELLOW = "yellow"
GREEN = "green"

# Game variables
current_light = RED
score = 0
lives = 3
timer = 0
light_duration = 60  # frames
reaction_window = 30  # frames to react when green

# Game state
game_active = True

def draw():
    screen.fill((50, 50, 50))  # Dark gray background
    
    if game_active:
        # Draw traffic light
        light_y = 150
        
        # Red light circle
        red_color = current_light if current_light == RED else (100, 0, 0)
        screen.draw.filled_circle((WIDTH/2, light_y), 60, red_color)
        
        # Yellow light circle
        yellow_color = current_light if current_light == YELLOW else (100, 100, 0)
        screen.draw.filled_circle((WIDTH/2, light_y + 150), 60, yellow_color)
        
        # Green light circle
        green_color = current_light if current_light == GREEN else (0, 100, 0)
        screen.draw.filled_circle((WIDTH/2, light_y + 300), 60, green_color)
        
        # Draw game info
        screen.draw.text(f"Score: {score}", (10, 10), color="white", fontsize=35)
        screen.draw.text(f"Lives: {lives}", (WIDTH - 150, 10), color="red", fontsize=35)
        
        # Draw instructions based on light
        if current_light == RED:
            screen.draw.text("STOP! Don't press SPACE!", 
                            (WIDTH/2 - 180, HEIGHT - 60), 
                            color="red", fontsize=30)
        elif current_light == YELLOW:
            screen.draw.text("GET READY...", 
                            (WIDTH/2 - 100, HEIGHT - 60), 
                            color="yellow", fontsize=30)
        elif current_light == GREEN:
            screen.draw.text("GO! Press SPACE NOW!", 
                            (WIDTH/2 - 160, HEIGHT - 60), 
                            color="green", fontsize=30)
    else:
        # Game over screen
        screen.fill((100, 0, 0))
        screen.draw.text("GAME OVER", 
                        (WIDTH/2 - 120, HEIGHT/2 - 50), 
                        color="white", fontsize=50)
        screen.draw.text(f"Final Score: {score}", 
                        (WIDTH/2 - 100, HEIGHT/2 + 20), 
                        color="white", fontsize=35)
        screen.draw.text("Press R to Restart", 
                        (WIDTH/2 - 120, HEIGHT/2 + 80), 
                        color="white", fontsize=25)

def update():
    global timer, current_light, lives, score, game_active
    
    if not game_active:
        return
    
    timer += 1
    
    # Change lights after duration
    if timer >= light_duration:
        timer = 0
        
        # Randomly select next light (weighted)
        rand = random.random()
        if current_light == RED:
            current_light = YELLOW if rand < 0.7 else GREEN
        elif current_light == YELLOW:
            current_light = GREEN if rand < 0.8 else RED
        elif current_light == GREEN:
            # If green light expires and player didn't press space, lose life
            lives -= 1
            if lives <= 0:
                game_active = False
            current_light = YELLOW if rand < 0.6 else RED
        
        # Vary the duration for next light
        light_duration = random.randint(40, 100)

def on_key_down(key):
    global score, lives, game_active, current_light, timer
    
    if not game_active:
        if key == keys.R:
            # Restart game
            reset_game()
        return
    
    if key == keys.SPACE:
        # Check response based on current light
        if current_light == GREEN:
            # Correct! Score points
            score += 10
            # Bonus for fast reaction
            if timer < reaction_window:
                bonus = reaction_window - timer
                score += bonus
            # Change to next light
            current_light = YELLOW
            timer = 0
        elif current_light == RED:
            # Wrong! Lose a life
            lives -= 1
            if lives <= 0:
                game_active = False
        # Yellow light - no penalty, just ignore

def reset_game():
    global score, lives, game_active, current_light, timer, light_duration
    score = 0
    lives = 3
    game_active = True
    current_light = RED
    timer = 0
    light_duration = 60
