import pygame
import sys
import random
import sqlite3
import time

conn = sqlite3.connect("snake_game.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user (
    username TEXT PRIMARY KEY
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS user_score (
    username TEXT,
    score INTEGER,
    level INTEGER,
    snake TEXT,
    FOREIGN KEY(username) REFERENCES user(username)
)''')
conn.commit()

def get_user_data():
    username = input("Enter your username: ").strip()
    cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO user (username) VALUES (?)", (username,))
        cursor.execute("INSERT INTO user_score (username, score, level, snake) VALUES (?, ?, ?, ?)", 
                       (username, 0, 1, str([(WIDTH // 2, HEIGHT // 2)])))
        conn.commit()
        print("New user created. Starting fresh!")
        time.sleep(3)
        return username, 0, 1, [(WIDTH // 2, HEIGHT // 2)]
    else:
        cursor.execute("SELECT score, level, snake FROM user_score WHERE username = ?", (username,))
        row = cursor.fetchone()
        print(f"Welcome back, {username}! Resuming from level {row[1]}, score {row[0]}")
        time.sleep(3)
        return username, row[0], row[1], eval(row[2])

pygame.init()
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

username, score, level_score, snake = get_user_data()
dx, dy = GRID_SIZE, 0
level_score_treshold = 4 * level_score
cl_speed = 10 + (level_score - 1) * 2
food = None

def get_random_position():
    return (
        random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
        random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
    )

def draw_score():
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, BLUE)
    screen.blit(text, (10, 10))

def draw_level():
    font = pygame.font.Font(None, 36)
    text = font.render(f'Level: {level_score}', True, BLUE)
    screen.blit(text, (10, 40))

def save_state():
    cursor.execute("REPLACE INTO user_score (username, score, level, snake) VALUES (?, ?, ?, ?)",
                   (username, score, level_score, str(snake)))
    conn.commit()
    print("Game state saved!")

food = get_random_position()
running = True
paused = False

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_state()
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
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    print("Game paused. Press 'P' to resume.")
                    save_state()
    
    if paused:
        pygame.display.flip()
        clock.tick(5)
        continue

    x, y = snake[0]
    x += dx
    y += dy

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or (x, y) in snake:
        print("Game over!")
        save_state()
        break

    snake.insert(0, (x, y))

    if snake[0] == food:
        food = get_random_position()
        score += 1
        if score >= level_score_treshold:
            level_score += 1
            level_score_treshold += 4
            cl_speed += 2
            print(f"Level up! New level: {level_score}")
    else:
        snake.pop()

    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    draw_score()
    draw_level()
    pygame.display.flip()
    clock.tick(cl_speed)

pygame.quit()
conn.close()
sys.exit()