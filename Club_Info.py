import pygame
import sys

# Initialize Pygame
pygame.init()

# Get the screen dimensions
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Scrolling Text")

# Text settings
font_size = 100
font = pygame.font.Font(None, font_size)
text = "Hi! I'm at another club right now but feel free to sign up!"

# Calculate the initial text position
text_surface = font.render(text, True, (255, 255, 255))
text_width, text_height = text_surface.get_size()
x = screen_width

# Color settings
bg_color = (0, 0, 0)
text_color = (255, 255, 255)
bg_increment = 1
text_increment = 1

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Change background color from black to white and vice versa
    bg_color = (bg_color[0] + bg_increment, bg_color[1] + bg_increment, bg_color[2] + bg_increment)
    if bg_color[0] >= 255:
        bg_increment = -1
    elif bg_color[0] <= 0:
        bg_increment = 1

    # Change text color from white to black and vice versa
    text_color = (text_color[0] - text_increment, text_color[1] - text_increment, text_color[2] - text_increment)
    if text_color[0] <= 0:
        text_increment = -1
    elif text_color[0] >= 255:
        text_increment = 1

    screen.fill(bg_color)

    # Draw the text in the center of the screen
    y = (screen_height - text_height) // 2
    text_surface = font.render(text, True, text_color)
    screen.blit(text_surface, (x, y))

    x -= 2  # Adjust the scrolling speed here for smoother movement

    if x + text_width <= 0:
        x = screen_width

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
