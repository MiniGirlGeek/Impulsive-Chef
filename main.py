from random import randint
import csv, time

NAME = input('Tell me your name, or else!: ')
pot = Actor('cooking-pot')
bin = Actor('closed-bin')
clock_img = Actor('clock')
apple = Actor('apple-good')
badApple = Actor('apple-rotten')
scoreBase = Actor('score-base')
potTop = Actor('pot-top')
binTop = Actor('bin-top')
binInside = Actor('bin-inside')
pie = Actor('pie')

clock_img.pos = 110, 110
pot.pos = 500, 500
bin.pos = 98.5, 490.398
apple.pos = 500, 0
badApple.pos = 508.889, 0
potTop.pos = 500, 511.5
binInside.pos = 98.5, 440.705
binTop.pos = 143.487, 453.034
pie.pos = 326.067, 363

LENGTH = 60
WIDTH = 652
HEIGHT = 600
MAX_SPEED = 18

speed = 5
appleCount = 0


csvfile = open('data/' + NAME + '\'s_data_from_' + time.strftime("%d:%m:%Y") + '.csv', 'w')

fieldnames = ['Time Apple Generated', 'Time Of Click', 'Apple Type', 'Location', 'Apple\'s Speed', 'Reaction Time', 'Error Type']
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()
row = {'Time Apple Generated':'', 'Time Of Click':'', 'Apple Type':'', 'Location':'', 'Apple\'s Speed':'', 'Reaction Time':'', 'Error Type':''}
appleType = apple
row['Time Apple Generated'] = time.time()
row['Apple Type'] = 'good'

startTime = time.time()

def open_bin():
    bin.image = 'open-bin'
    bin.pos = 143.487, 453.034

def close_bin():
    bin.image = 'closed-bin'
    bin.pos = 98.5, 490.398
    apple.pos = 500, 0
    badApple.pos = 508.889, 0


def choose_apple():
    if time.time() - startTime <= LENGTH:
        number = randint(1, 10)
        if number <= 8:
            appleType = badApple
            row['Time Apple Generated'] = time.time()
            row['Apple Type'] = 'bad'
        else:
            appleType = apple
            row['Time Apple Generated'] = time.time()
            row['Apple Type'] = 'good'
        return appleType

def draw():
    if time.time() - startTime >= LENGTH:
        screen.fill((237, 174, 0))
        screen.draw.text('Well done ' + NAME + '!\n Your score was: ' + str(appleCount),  midtop=(326.067, 80.169), fontname="intuitive", fontsize=50)
        pie.draw()
        csvfile.close()
    else:
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
    global row
    if time.time() - startTime <= LENGTH:
        open_bin()
        def drop_in_bin():
            animate(appleType, duration=0.2,on_finished=close_bin, pos=(97.059, 575))
        animate(appleType, duration=0.2,on_finished=drop_in_bin, pos=(97.059, 326.068))
        row['Time Of Click'] = time.time()
        row['Location'] = 'Bin'
        if appleType == apple:
            row['Error Type'] = 'clicked'
        try:
            row['Reaction Time'] = row['Time Of Click'] - row['Time Apple Generated']
        except:
            pass

        writer.writerow(row)
        row = {'Time Apple Generated':'', 'Time Of Click':'', 'Apple Type':'', 'Location':'', 'Apple\'s Speed':'', 'Reaction Time':'', 'Error Type':''}


def update():
    global row
    global appleCount
    global appleType
    global speed
    if time.time() - startTime <= LENGTH:
        appleType.bottom += speed
        if appleType.bottom >= 560:
            if appleType.pos[0] == 499.5:
                appleCount += 1
                row['Apple\'s Speed'] = speed
                row['Location'] = 'Pot'
                sounds.splash.play()
                writer.writerow(row)
                row = {'Time Apple Generated':'', 'Time Of Click':'', 'Apple Type':'', 'Location':'', 'Apple\'s Speed':'', 'Reaction Time':'', 'Error Type':''}
            elif appleType.pos[0] == 508.0:
                appleCount -= 1
                row['Error Type'] = 'didn\'t click'
                sounds.splash.play()
                writer.writerow(row)
                row = {'Time Apple Generated':'', 'Time Of Click':'', 'Apple Type':'', 'Location':'', 'Apple\'s Speed':'', 'Reaction Time':'', 'Error Type':''}
            else:
                sounds.clang.play()
            appleType.bottom = -100
            appleType = choose_apple()
            if speed < MAX_SPEED:
                speed = speed * 1.3

