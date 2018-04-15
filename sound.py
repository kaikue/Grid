import pygame
import result

def load_sounds():
    global move
    move = load_sound("move")
    global hit
    hit = load_sound("hit")
    global won
    won = load_sound("won")
    global die
    die = load_sound("die")

def load_sound(name):
    return pygame.mixer.Sound("sound/" + name + ".wav")

def play_move(r):
    if r == result.CLEAR:
        move.play()
    elif r == result.HIT:
        hit.play()
    elif r == result.WON:
        won.play()

def play_die():
    die.play()