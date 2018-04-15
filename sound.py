import pygame
import result

def play_move(r):
    if r == result.CLEAR:
        play_sound("sound/move.wav")
    elif r == result.HIT:
        play_sound("sound/hit.wav")
    elif r == result.WON:
        play_sound("sound/won.wav")

def play_sound(path):
    soundObj = pygame.mixer.Sound(path)
    soundObj.play()