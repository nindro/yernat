#2. Create music player with keyboard controller. You have to be able to press keyboard: play, stop, next and previous as some keys. Player has to react to the given command appropriately.
import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((640, 480))

playlist = ["yay.mp3", "aww.mp3", "door.wav"]
current_track = 0
playing = False
def play_music():
    global playing
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()
    playing = True
def stop_music():
    global playing
    pygame.mixer.music.stop()
    playing = False
def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()
def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()
done = False
while not done:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                stop_music()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                prev_track()
pygame.quit()

#RESULTS
#Controls:
#S - stop the music
#N - next track
#P - previous track