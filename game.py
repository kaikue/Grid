import pygame
from pygame.locals import DOUBLEBUF
import sys
import result
import grid
import sound

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

FRAMES_PER_SEC = 60

TILE_SIZE = 30 #pixels

BACKGROUND = (0, 0, 0)
BORDER = (60, 60, 60)
GRID = (30, 30, 30)
TEXT = (255, 255, 255)

BORDER_SIZE = 5

"""
TODO:
Buttons
Doors
Splitters
Harm

Level text
1: Arrow keys to move
2: Press R to restart

Music
Open world level?
Weird narration
Weird effects

Restructure sound (only load once)
"""

def start():
    pygame.init()
    
    pygame.display.set_caption("GRID")
    
    #Use double buffering for better performance
    flags = DOUBLEBUF
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags)
    
    global clock
    clock = pygame.time.Clock()
    
    global font
    font = pygame.font.Font("font/kenpixel_mini.ttf", 32)
    
    load_level(1)
    
    run()

def run():
    while True:
        clock.tick_busy_loop(FRAMES_PER_SEC)
        
        update()
        
        render()

def update():
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_ESCAPE]:
        sys.exit(0)
    
    if pressed[pygame.K_LEFT]:
        pass #player_pos[0] -= SPEED
    if pressed[pygame.K_RIGHT]:
        pass #player_pos[0] += SPEED
    if pressed[pygame.K_UP]:
        pass #player_pos[1] -= SPEED
    if pressed[pygame.K_DOWN]:
        pass #player_pos[1] += SPEED
    
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            sys.exit(0)
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.K_UP:
                move((0, -1))
            elif event.key == pygame.K_DOWN:
                move((0, 1))
            elif event.key == pygame.K_LEFT:
                move((-1, 0))
            elif event.key == pygame.K_RIGHT:
                move((1, 0))
            elif event.key == pygame.K_r:
                restart_level()

def render():
    screen.fill(BACKGROUND)
    
    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2
    start_x = center_x - (game_grid.width / 2) * TILE_SIZE
    start_y = center_y - (game_grid.height / 2) * TILE_SIZE
    
    border_rect = pygame.rect.Rect((start_x - BORDER_SIZE, start_y - BORDER_SIZE),
                                    (game_grid.width * TILE_SIZE + 2 * BORDER_SIZE, game_grid.height * TILE_SIZE + 2 * BORDER_SIZE))
    pygame.draw.rect(screen, BORDER, border_rect)
    
    grid_rect = pygame.rect.Rect((start_x, start_y), (game_grid.width * TILE_SIZE, game_grid.height * TILE_SIZE))
    pygame.draw.rect(screen, GRID, grid_rect)
    
    for tile in game_grid.tiles:
        screen_pos = (start_x + tile.pos[0] * TILE_SIZE, start_y + tile.pos[1] * TILE_SIZE)
        tile_rect = pygame.rect.Rect(screen_pos, (TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(screen, tile.get_color(), tile_rect)
    
    if game_grid.text != "":
        text_image = font.render(game_grid.text, False, TEXT)
        screen.blit(text_image, (0, 0))
    
    pygame.display.update()

def load_level(l):
    global level
    level = l
    
    global game_grid
    game_grid = grid.Grid(l)

def next_level():
    load_level(level + 1)

def restart_level():
    sound.play_sound("sound/die.wav")
    load_level(level)

def move(vel):
    for tile in game_grid.tiles:
        r = tile.move(vel)
        if r == result.WON:
            next_level()
            return

if __name__ == "__main__":
    start()