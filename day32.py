import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

dino_img = pygame.image.load("dino.png")
dino_img = pygame.transform.scale(dino_img, (50, 50))
cactus_img = pygame.image.load("cactus.png")
cactus_img = pygame.transform.scale(cactus_img, (30, 50))

dino_x, dino_y = 50, HEIGHT - 100
dino_vel_y = 0
ground = HEIGHT - 50
gravity = 0.6
jump_power = -10
is_jumping = False
cactus_x = WIDTH
cactus_speed = 5
score = 0

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                dino_vel_y = jump_power
                is_jumping = True
    
    # Apply gravity
    dino_vel_y += gravity
    dino_y += dino_vel_y
    
    # Prevent falling through the ground
    if dino_y >= ground - 50:
        dino_y = ground - 50
        is_jumping = False
    
    # Move cactus
    cactus_x -= cactus_speed
    if cactus_x < -30:
        cactus_x = WIDTH
        score += 1  # Increase score when a cactus passes
    
    # Collision detection
    if dino_x < cactus_x + 30 and dino_x + 50 > cactus_x and dino_y + 50 > ground - 50:
        print("Game Over! Score:", score)
        running = False
    
    # Draw objects
    screen.blit(dino_img, (dino_x, dino_y))
    screen.blit(cactus_img, (cactus_x, ground - 50))
    
    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()
