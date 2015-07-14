from random import randint

pot = Actor('cooking-pot')
bin = Actor('closed-bin')
clock_img = Actor('clock')
apple = Actor('apple-good')
badApple = Actor('apple-rotten')
scoreBase = Actor('score-base')
potTop = Actor('pot-top')

clock_img.pos = 110, 110
pot.pos = 500, 500
bin.pos = 98.5, 490.398
apple.pos = 500, 0
badApple.pos = 508.889, 0
potTop.pos = 500, 511.5

WIDTH = 800
HEIGHT = 600
MAX_SPEED = 30

speed = 2

appleType = apple

def open_bin():
    bin.image = 'open-bin'
    bin.pos = 143.487, 453.034

def close_bin():
    bin.image = 'closed-bin'
    bin.pos = 98.5, 490.398


def choose_apple():
    number = randint(1, 10)
    if number <= 8:
        appleType = badApple
    else:
        appleType = apple
    return appleType

def draw():
    screen.fill((237, 174, 0))
    clock_img.draw()
    pot.draw()
    bin.draw()
    appleType.draw()
    potTop.draw()

def on_mouse_down(pos):
    open_bin()
    clock.schedule_unique(close_bin, 1.0)
    if appleType.collidepoint(pos):
        animate(appleType, pos=(103.059 , 326.068))
    else:
        print("You missed me!")

def update():
    global appleType
    global speed
    appleType.bottom += speed
    if appleType.bottom >= 575:
        appleType.bottom = -100
        appleType = choose_apple()
        if speed < MAX_SPEED:
            speed = speed * 1.2
        print(speed)


