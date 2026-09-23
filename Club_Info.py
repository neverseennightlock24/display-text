import pygame

# Display settings
MESSAGE = "Hi! I'm at another club right now but feel free to sign up!"
FONT_SIZE = 100
SCROLL_SPEED = 120  # pixels per second
FADE_SPEED = 60  # brightness steps per second (0-255 range)
FRAME_RATE = 60


def shouldQuit():
    # Only a window-close request ends the program; no key exits it on purpose
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
    return False


def advanceBrightness(brightness, fadeDirection, elapsedSeconds):
    # Bounce the background brightness between black (0) and white (255)
    brightness += fadeDirection * FADE_SPEED * elapsedSeconds
    if brightness >= 255:
        brightness = 255
        fadeDirection = -1
    elif brightness <= 0:
        brightness = 0
        fadeDirection = 1
    return brightness, fadeDirection


def drawFrame(screen, font, textX, brightness):
    # Text is always the inverse shade of the background
    backgroundShade = int(brightness)
    textShade = 255 - backgroundShade
    backgroundColor = (backgroundShade, backgroundShade, backgroundShade)
    textColor = (textShade, textShade, textShade)

    textSurface = font.render(MESSAGE, True, textColor)
    textY = (screen.get_height() - textSurface.get_height()) // 2

    screen.fill(backgroundColor)
    screen.blit(textSurface, (int(textX), textY))
    pygame.display.flip()


def main():
    pygame.init()

    # (0, 0) makes pygame use the current desktop resolution
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Scrolling Text")
    pygame.mouse.set_visible(False)

    font = pygame.font.Font(None, FONT_SIZE)
    textWidth = font.size(MESSAGE)[0]
    screenWidth = screen.get_width()

    # Text starts just off the right edge and scrolls left
    textX = screenWidth
    brightness = 0
    fadeDirection = 1
    clock = pygame.time.Clock()

    while not shouldQuit():
        # Frame-rate independent timing keeps speed consistent on slow machines
        elapsedSeconds = clock.tick(FRAME_RATE) / 1000

        brightness, fadeDirection = advanceBrightness(brightness, fadeDirection, elapsedSeconds)

        textX -= SCROLL_SPEED * elapsedSeconds
        if textX + textWidth <= 0:
            textX = screenWidth

        drawFrame(screen, font, textX, brightness)

    pygame.quit()


if __name__ == "__main__":
    main()
