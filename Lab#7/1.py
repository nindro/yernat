#1. Create a simple clock application (only with minutes and seconds) which is synchronized with system clock. Use Mickey's right hand as minutes arrow and left - as seconds. For moving Mickey's hands you can use: pygame.transform.rotate
import pygame
import time
from datetime import datetime

pygame.init()

width, height = 640, 480
center = (width // 2, height //2)

mickey = pygame.image.load("clock.png")
sec_hand = pygame.image.load("sec_hand.png")
min_hand = pygame.image.load("min_hand.png")

mickey = pygame.transform.scale(mickey, (width, height))

screen = pygame.display.set_mode((width, height))

def draw_hand(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, -angle)
    new_rect = rotated_image.get_rect(center=pivot)
    screen.blit(rotated_image, new_rect.topleft)

done = False
while not done:
    screen.fill((255, 255, 255))
    screen.blit(mickey, (0, 0))
    now = datetime.now()
    seconds = now.second
    minutes = now.minute

    sec_angle = (seconds/60) * 360
    min_angle = (minutes/60) * 360

    draw_hand(sec_hand, sec_angle, center)
    draw_hand(min_hand, min_angle, center)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    time.sleep(1)
pygame.quit()