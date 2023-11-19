import turtle
import pygame

def play_bgm():
    pygame.mixer.music.load('./sounds/bgm.mp3')
    pygame.mixer.music.play(-1)

def volume_down():
    v = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(v-0.1)
def volume_up():
    v = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(v+0.1)

def load_sound():
    global boom, coin, next_level, win
    pygame.mixer.init()
    boom = pygame.mixer.Sound('./sounds/lose.mp3')
    coin = pygame.mixer.Sound('./sounds/coin.ogg')
    next_level = pygame.mixer.Sound('./sounds/one_up.ogg')
    win = pygame.mixer.Sound('./sounds/win.mp3')

def play_sound():
    boom.play()

def play_get_coin():
    coin.play()

def play_next_level():
    next_level.play()

def play_win():
    win.play()

def draw_rect(edge, bgcolor, bdcolor='#FFFFFF'):
    turtle.color(bdcolor, bgcolor)
    turtle.down()
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(edge)
        turtle.rt(90)
    turtle.end_fill()
    turtle.up()
