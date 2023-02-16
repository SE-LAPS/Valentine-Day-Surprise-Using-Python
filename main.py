import pygame

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Happy valentine")

# Load the background image
bg_img = pygame.image.load('background.png')
bg_rect = bg_img.get_rect()

# Load the heart image
heart_img = pygame.image.load('heart.png')
heart_rect = heart_img.get_rect()

# Set up the initial position of the heart
x = 200
y = 200

# Set up the speed of the heart
speed_x = 2
speed_y = 2

# Start the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the heart
    x += speed_x
    y += speed_y

    # Bounce the heart off the edges of the screen
    if x < 0 or x > 450:
        speed_x = -speed_x
    if y < 0 or y > 550:
        speed_y = -speed_y

    # Draw the background on the screen
    screen.blit(bg_img, bg_rect)

    # Draw the heart on the screen
    screen.blit(heart_img, (x, y))

    # Update the screen
    pygame.display.update()

    # Set the frame rate
    pygame.time.Clock().tick(60)

# Quit the game
pygame.quit()
