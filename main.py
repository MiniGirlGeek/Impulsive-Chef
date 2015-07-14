from random import randint

pot = Actor('cooking-pot')
bin = Actor('closed-bin')
clock_img = Actor('clock')
apple = Actor('apple-good')
badApple = Actor('apple-rotten')
scoreBase = Actor('score-base')
potTop = Actor('pot-top')
binTop = Actor('bin-top')
binInside = Actor('bin-inside')

clock_img.pos = 110, 110
pot.pos = 500, 500
bin.pos = 98.5, 490.398
apple.pos = 500, 0
badApple.pos = 508.889, 0
potTop.pos = 500, 511.5
binInside.pos = 98.5, 440.705
binTop.pos = 143.487, 453.034

WIDTH = 652
HEIGHT = 600
MAX_SPEED = 20

speed = 5
appleCount = 0

appleType = apple

def open_bin():
    bin.image = 'open-bin'
    bin.pos = 143.487, 453.034

def close_bin():
    bin.image = 'closed-bin'
    bin.pos = 98.5, 490.398
    apple.pos = 500, 0
    badApple.pos = 508.889, 0


def choose_apple():
    number = randint(1, 10)
    if number <= 9:
        appleType = badApple
    else:
        appleType = apple
    return appleType

def draw():
    screen.fill((237, 174, 0))
    appleName = ' apple' if appleCount == 1 else ' apples'
    screen.draw.text('You have\n' + str(appleCount) + appleName + '!', midtop=(326.067, 80.169), fontname="intuitive", fontsize=50)
    clock_img.draw()
    pot.draw()
    #bin.draw()
    binInside.draw()
    appleType.draw()
    potTop.draw()
    binTop.draw()

def on_mouse_down(pos):
    open_bin()
    def drop_in_bin():
        animate(appleType, duration=0.2,on_finished=close_bin, pos=(97.059, 575))
    animate(appleType, duration=0.2,on_finished=drop_in_bin, pos=(97.059, 326.068))


def update():
    global appleCount
    global appleType
    global speed
    appleType.bottom += speed
    if appleType.bottom >= 575:
        if appleType.pos[0] == 499.5:
            appleCount += 1
        elif appleType.pos[0] == 508.0:
            appleCount -= 1
        appleType.bottom = -100
        appleType = choose_apple()
        if speed < MAX_SPEED:
            speed = speed * 1.08
