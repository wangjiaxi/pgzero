import pgzrun, random, time

WIDTH = 384
HEIGHT = 700
SPEED = 5
rubbish = ['oil', 'rock1', 'rock2', 'rock3']
car = Actor('car_blue_small_5', (192, 600))
barrier1 = Actor(rubbish[random.randint(0, 3)], (random.randint(0, 600), 0))
G = 0.4
barrier1.vy = 0
car.dead = False


def draw():
    screen.clear()
    for i in range(700 // 128 + 1):
        screen.blit('road_asphalt21', (0, 128 * i))
        screen.blit('road_asphalt88', (128, 128 * i))
        screen.blit('road_asphalt23', (256, 128 * i))
    car.draw()
    barrier1.draw()


def reset_barrier_1():
    barrier1.image = rubbish[random.randint(0, 3)]
    barrier1.center = random.randint(0, 384), 0


def reset_car():
    car.x = 192
    car.image = 'car_blue_small_5'
    car.dead = False


def reset():
    reset_car()
    reset_barrier_1()


def set_car_dead():
    car.image = 'car_red_small_5'
    car.dead = True
    clock.schedule_unique(reset_car, 1.0)


def update_barrier_1():
    barrier1.vy += G
    barrier1.y += barrier1.vy
    # barrier1.y += SPEED
    if barrier1.y < 0 or barrier1.y > 700:
        barrier1.vy = 0
        reset_barrier_1()


def update_car():
    if car.x < 384 or car.x > 0:
        if keyboard.right:
            car.x += 10
        elif keyboard.left:
            car.x -= 10
    if car.colliderect(barrier1):
        reset_barrier_1()
        set_car_dead()
    if not 0 < car.x < 384:
        reset()


def update():
    update_barrier_1()
    update_car()


pgzrun.go()
