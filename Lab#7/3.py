#3. Draw circle - a red ball of size 50 x 50 (radius = 25) on white background. When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the direction of pressed key. The ball should not leave the screen, i.e. user input that leads the ball to leave of the screen should be ignored
import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
done = False
clock = pygame.time.Clock()
radius = 25
red = (255, 0, 0)
x, y = 400, 300
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and x - radius - 20 >= 0: x -= 20
    if pressed[pygame.K_RIGHT] and x + radius + 20 <= 800: x += 20
    if pressed[pygame.K_UP] and y - radius - 20 >= 0: y -= 20
    if pressed[pygame.K_DOWN] and y + radius + 20 <= 600: y += 20
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, red, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()