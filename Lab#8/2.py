import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE =(0, 0, 255)

# Snake initial position and movement
snake = [(WIDTH // 2, HEIGHT // 2)]
dx, dy = GRID_SIZE, 0  # Initial movement direction
# New variables
score = 0
level_score = 1
cl_speed = 10
level_score_treshold = 4
# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def get_random_position():
    """Generate a random position within the grid."""
    x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
    return x, y
def draw_score():
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, BLUE)
    screen.blit(text, (10, 10))
def draw_level():
    font = pygame.font.Font(None, 36)
    text = font.render(f'Level: {level_score}', True, BLUE)
    screen.blit(text, (10, 40))

food = get_random_position()

running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -GRID_SIZE
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, GRID_SIZE
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -GRID_SIZE, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = GRID_SIZE, 0

    # Move snake
    x, y = snake[0]
    x += dx
    y += dy

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        running = False
    else:
        snake.insert(0, (x, y))
        snake.pop()
    if snake[0] == food:
        food = get_random_position()
        snake.append(snake[-1])
        score += 1
    if score >= level_score_treshold:
        level_score += 1
        level_score_treshold += 4

    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))  # Draw food
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    draw_score()
    draw_level()
    pygame.display.flip()
    clock.tick(10 + (level_score - 1) * 2)  # Control speed

pygame.quit()
sys.exit()
#1.Check for border: 69-70
#2.Generate for food: 74-76
#3.Level up: 78-81
#4.Increasing speed: 91
#5.Score: 74-77