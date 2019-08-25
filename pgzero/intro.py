import time
import pgzrun
import random

alien = Actor('alien')
alien.topright = 0, 10

WIDTH = 500
HEIGHT = 500

colors = [0, 0, 0]
def draw():
    screen.fill(tuple(colors))
    alien.draw()

def update():
#    colors[0] = (colors[0] + 1) % 256
    colors[1] = (colors[1] + 1) % 256
    colors[2] = (colors[2] + 1) % 256
    alien.left += 2
    if alien.right > WIDTH:
        alien.left(0)
        time.sleep(0.2)
        alien.image = 'alien'

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = 'alien'

pgzrun.go()