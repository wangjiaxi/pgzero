import random
import pgzrun

bird = Actor('bird2', (75, 200))
pipe_top = Actor('top', anchor=('left', 'bottom'))
pipe_bottom = Actor('bottom', anchor=('left', 'top'))

WIDTH = 400
HEIGHT = 708
GAP = 500
SPEED = 3


def reset_pipes():
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP // 2)
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP // 2)


def update_pipes():
    pipe_top.left -= SPEED
    pipe_bottom.left -= SPEED
    if pipe_top.right < 0:
        reset_pipes()


GRAVITY = 0.3

bird.dead = False
bird.vy = 0


def update_bird():
    bird.image = 'bird2'
    bird.vy += GRAVITY
    bird.y += bird.vy
    bird.x = 75

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        bird.dead = True
        bird.image = 'dead'

    if not 0 < bird.y < 720:
        bird.y = 200
        bird.dead = False
        bird.vy = 0
        reset_pipes()


def draw():
    screen.blit('background', (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()


def update():
    update_pipes()
    update_bird()




FLAP_VELOCITY = -6.5


def on_key_down():
    if not bird.dead:
        bird.vy = FLAP_VELOCITY


def on_mouse_down():
    if not bird.dead:
        bird.vy = FLAP_VELOCITY


pgzrun.go()
