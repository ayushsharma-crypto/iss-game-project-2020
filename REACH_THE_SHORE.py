#!/usr/bin/python
# -- coding: utf-8 --
import pygame
import sys
import random
import math
from pygame import mixer
import configparser
import os

pygame.init()


configParser = configparser.RawConfigParser()                                   #values from config file
configFilePath = os.path.join("./", "config.cfg")
configParser.read(configFilePath)

light_pink = configParser.get("info", "light_pink")
light_pink = eval(light_pink)
violet = configParser.get("info", "violet")
violet = eval(violet)
orange = configParser.get("info", "orange")
orange = eval(orange)
green = configParser.get("info", "green")
green = eval(green)
kindblue = configParser.get("info", "kindblue")
kindblue = eval(kindblue)
black = configParser.get("info", "black")
black = eval(black)
gb = configParser.get("info", "gb")
gb = eval(gb)
blue = configParser.get("info", "blue")
blue = eval(blue)
redi = configParser.get("info", "redi")
redi = eval(redi)
brown = configParser.get("info", "brown")
brown = eval(brown)
winc = configParser.get("info", "winc")
winc= eval(winc)
white = configParser.get("info", "white")
white = eval(white)
rg = configParser.get("info", "rg")
rg = eval(rg)



startingfont1 = configParser.get("info","startingfont1")
startingfont1 = eval(startingfont1)
startingfont2 = configParser.get("info","startingfont2")
startingfont2 = eval(startingfont2)
fonti = configParser.get("info","fonti")
fonti = eval(fonti)
p1font = configParser.get("info","p1font")
p1font = eval(p1font)
score_font = configParser.get("info","score_font")
score_font = eval(score_font)


p2message = configParser.get("info","p2message")
p2message = eval(p2message)

win1 = configParser.get("info","win1")
win1 = eval(win1)

win2 = configParser.get("info","win2")
win2 = eval(win2)

win3 = configParser.get("info","win3")
win3 = eval(win3)

win4 = configParser.get("info","win4")
win4 = eval(win4)

win5 = configParser.get("info","win5")
win5 = eval(win5)

win6 = configParser.get("info","win6")
win6 = eval(win6)                                                               # values from config file


pygame.display.set_caption('!! Reach The Shore !!')
screen = pygame.display.set_mode((1000, 1010))                                     # my pygame screen window will be of 1000 px by 1010 px


# class for fixed obstacle

class fixedobstacle:

    def __init__(
        self,
        qwerty,
        rx1,
        rx2,
        ry1,
        ry2,
        cx,
        cy,
        ):
        self.obstacle1 = pygame.image.load(qwerty)
        self.obstacle1x = random.randint(rx1, rx2)
        self.obstacle1y = random.randint(ry1, ry2)
        self.obstacle1x_change = cx
        self.obstacle1y_change = cy
        self.flago1 = False
        self.flago2 = False

    def showobstacle(self):
        screen.blit(self.obstacle1, (self.obstacle1x, self.obstacle1y))


list_of_obstacles = []

# creating fixed obstacles various instances

obstacle1 = fixedobstacle(
    's1.png',
    0,
    500,
    170,
    180,
    0,
    0,
    )
obstacle2 = fixedobstacle(
    's1.png',
    300,
    800,
    306,
    316,
    0,
    0,
    )
obstacle3 = fixedobstacle(
    's1.png',
    500,
    900,
    452,
    462,
    0,
    0,
    )
obstacle4 = fixedobstacle(
    's1.png',
    0,
    200,
    598,
    608,
    0,
    0,
    )
obstacle5 = fixedobstacle(
    's1.png',
    0,
    800,
    744,
    754,
    0,
    0,
    )
#appending each fixed object in list

list_of_obstacles.append(obstacle1)
list_of_obstacles.append(obstacle2)
list_of_obstacles.append(obstacle3)
list_of_obstacles.append(obstacle4)
list_of_obstacles.append(obstacle5)


# class for moving obstacles

class movingobstacle:

    def __init__(
        self,
        qwerty,
        x,
        y,
        cx,
        ):
        self.obstacle1 = pygame.image.load(qwerty)
        self.obstacle1x = x
        self.obstacle1y = y
        self.obstacle1x_change = cx
        self.flagm1 = False
        self.flagm2 = False

    def show_f_obstacle(self):
        screen.blit(self.obstacle1, (self.obstacle1x, self.obstacle1y))

    def newpath(self, level):
        self.obstacle1x = random.choice([0, 920])
        if self.obstacle1x == 0:
            self.obstacle1 = pygame.image.load('bird2.png')
            self.obstacle1x_change = random.randint(12, 18) / 10 + level
        else:
            self.obstacle1 = pygame.image.load('ship.png')
            self.obstacle1x_change = -(random.randint(12, 18) / 10
                    + level)


list_of_movers = []
# creating various instances of moving obstacles

f_ob1 = movingobstacle('ship.png', 920, 105, -1.5)
f_ob2 = movingobstacle('bird2.png', 0, 253, 1)
f_ob3 = movingobstacle('ship.png', 920, 402, -1)
f_ob4 = movingobstacle('bird2.png', 0, 550, 1.7)
f_ob5 = movingobstacle('ship.png', 920, 694, -1)
f_ob6 = movingobstacle('ship.png', 920, 840, -1.8)

# appending all moving obs. instances in a list of movers

list_of_movers.append(f_ob1)
list_of_movers.append(f_ob2)
list_of_movers.append(f_ob3)
list_of_movers.append(f_ob4)
list_of_movers.append(f_ob5)
list_of_movers.append(f_ob6)


# class for player

class player:

    def __init__(
        self,
        qwerty,
        x,
        y,
        ):
        self.img = pygame.image.load(qwerty)
        self.x = x
        self.y = y
        self.cx = 0
        self.cy = 0
        self.level = 0
        self.reached = False
        self.turn = True
        self.score = 0
        self.s_increment = False
        self.time = pygame.time.get_ticks()
        self.net_time = 0

    def show_player(self):
        screen.blit(self.img, (self.x, self.y))


player1 = player('redbut.png', 500, 940)                 # player 1
player2 = player('but1.png', 500, 0)                      # player 2
player2.turn = False

player2.img = pygame.transform.flip(player2.img, False, True)
player1.img = pygame.transform.scale(player1.img, (55, 50))
player2.img = pygame.transform.scale(player2.img, (55, 50))


# collision function

def is_collision(
    px,
    py,
    ox,
    oy,
    ):
    dist = math.sqrt(math.pow(px - ox, 2) + math.pow(py - oy, 2))
    if dist <= 60:
        return True
    return False


# paused game function

def nothing():
    pause = True
    pausebutton = button(
        (153, 204, 0),
        850,
        5,
        100,
        70,
        'RESUME',
        )
    pausebutton.draw(screen, (0, 0, 0))
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                In_game = False
                pause = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pausebutton.isover(pos):
                    pause = False

            if event.type == pygame.MOUSEMOTION:
                if pausebutton.isover(pos):
                    pausebutton.color = (255, 255, 0)
                else:
                    pausebutton.color = (255, 204, 0)

        pygame.display.update()
    return


# class of buttons

class button:

    def __init__(
        self,
        color,
        x,
        y,
        width,
        height,
        text='',
        ):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=False):
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2,
                             self.width + 4, self.height + 4), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y,
                         self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsansms', 30)
            text = font.render(self.text, True, (0, 0, 0))
            screen.blit(text, (self.x + self.width / 2
                        - text.get_width() / 2, self.y + self.height
                        / 2 - text.get_height() / 2))

    def isover(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

#creating instances of various buttons

greenbutton = button(
    (0, 255, 0),
    370,
    400,
    250,
    100,
    'START GAME',
    )
quitbutton = button(
    (153, 204, 0),
    370,
    700,
    250,
    100,
    'QUIT GAME',
    )
pausebutton = button(
    (153, 204, 0),
    850,
    5,
    100,
    70,
    'PAUSE',
    )
continuebutton = button(
    (0, 255, 0),
    370,
    300,
    250,
    100,
    'NEXT ROUND',
    )
homebutton = button(
    (153, 204, 0),
    370,
    600,
    250,
    100,
    'GO HOME',
    )
instruction = button(
    (0, 0, 255),
    370,
    550,
    250,
    100,
    'INSTRUCTION',
    )

running = False
round_number = 1

# Game loop
# This while loop will create intro page.
In_game = True
while In_game:

    screen.fill(light_pink)

    # startingfont1 = pygame.font.SysFont('comicsansms', 90)
    # startingfont2 = pygame.font.SysFont('comicsansms', 50)

# writtings on intro page:

    write1 = startingfont1.render('!!  REACH THE SHORE  !!', True,
                                  violet)
    write2 = startingfont1.render('If U CAN :)', True,violet)
    credit = startingfont2.render('* Game Made By Ayush Sharma', True,
                                  orange)
    project = startingfont2.render('* For ISS Project', True, orange)
    screen.blit(write1, (140, 100))
    screen.blit(write2, (340, 240))

# Drawing start game box and quit game box

    greenbutton.draw(screen, green)
    quitbutton.draw(screen, rg)
    instruction.draw(screen, kindblue)    # instruction box
    screen.blit(credit, (450, 910))
    screen.blit(project, (450, 950))
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            In_game = False
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenbutton.isover(pos):
                running = True
            if quitbutton.isover(pos):
                running = False
                In_game = False
                pygame.quit()
                exit()
            if instruction.isover(pos):            # will show instruction to play the game

                flagg = True
                while flagg:

                    screen.fill(black)
                    # fonti = pygame.font.SysFont('comicsansms', 30)
                    writ1 = \
                        fonti.render('*The Game challenges you to reach the opposite '
                            , True, gb)
                    writ2 = \
                        fonti.render(' shore from which end player had started.'
                            , True, gb)
                    writ3 = \
                        fonti.render('*Do not collide with snakes and '
                            , True, gb)
                    writ4 = \
                        fonti.render(' other moving obstacles in path.'
                            , True, gb)
                    writ5 = fonti.render('* Player 1 control :-', True,
                            gb)
                    writ6 = fonti.render(' left : A', True, gb)
                    writ7 = fonti.render(' right : D', True, gb)
                    writ8 = fonti.render(' up : W', True, gb)
                    writ9 = fonti.render(' Down : S', True, gb)
                    writ10 = fonti.render('* Player 2 control :-',
                            True, gb)
                    writ11 = fonti.render(' left : LEFT-ARROW', True,
                            gb)
                    writ12 = fonti.render(' right : RIGHT-ARROW', True,
                            gb)
                    writ13 = fonti.render(' up : UP-ARROW', True, gb)
                    writ14 = fonti.render(' Down : DOWN-ARROW', True,
                            gb)

                    screen.blit(writ1, (300, 100))
                    screen.blit(writ2, (300, 135))
                    screen.blit(writ3, (300, 180))
                    screen.blit(writ4, (300, 215))
                    screen.blit(writ5, (300, 260))
                    screen.blit(writ6, (350, 300))
                    screen.blit(writ7, (350, 340))
                    screen.blit(writ8, (350, 380))
                    screen.blit(writ9, (350, 420))
                    screen.blit(writ10, (300, 460))
                    screen.blit(writ11, (350, 500))
                    screen.blit(writ12, (350, 540))
                    screen.blit(writ13, (350, 580))
                    screen.blit(writ14, (350, 620))

                    back = button(                      # on clicking back button will bring you to home page.
                        blue,
                        340,
                        670,
                        250,
                        100,
                        'GO BACK',
                        )
                    back.draw(screen, rg)

                    for event in pygame.event.get():

                        pos = pygame.mouse.get_pos()

                        if event.type == pygame.QUIT:                 # On clicking 'x' button game window gets close.
                            In_game = False
                            running = False
                            flagg = False
                            pygame.quit()
                            exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if back.isover(pos):
                                flagg = False

                    pygame.display.update()

        if event.type == pygame.MOUSEMOTION:

            if greenbutton.isover(pos):
                greenbutton.color = green
            else:
                greenbutton.color = (153, 204, 0)
            if quitbutton.isover(pos):
                quitbutton.color = (255, 255, 0)
            else:
                quitbutton.color = (255, 204, 0)
            if instruction.isover(pos):
                instruction.color = (0, 0, 255)
            else:
                instruction.color = (0, 102, 255)

# Actual game part starts in thi while loop.

    while running:                

# setting the game screen.

        screen.fill(blue)
        pygame.draw.rect(screen, brown, (0, 0, 1000, 80))
        pygame.draw.rect(screen, redi, (0, 80, 1000, 5))

        pygame.draw.rect(screen, brown, (0, 185, 1000, 40))
        pygame.draw.rect(screen, brown, (0, 341, 1000, 40))
        pygame.draw.rect(screen, brown, (0, 487, 1000, 40))
        pygame.draw.rect(screen, brown, (0, 633, 1000, 40))
        pygame.draw.rect(screen, brown, (0, 779, 1000, 40))

        pygame.draw.rect(screen, redi, (0, 925, 1000, 5))
        pygame.draw.rect(screen, brown, (0, 930, 1000, 80))

        pausebutton.draw(screen, black)

        #  introducing obstacles

        for i in list_of_obstacles:
            i.showobstacle()

        for i in list_of_movers:
            i.show_f_obstacle()

        for i in list_of_movers:
            i.obstacle1x = i.obstacle1x + i.obstacle1x_change

        for i in list_of_movers:
            if i.obstacle1x <= 0 or i.obstacle1x >= 940:
                if player1.turn:
                    i.newpath(player1.level)
                elif player2.turn:
                    i.newpath(player2.level)

# code to run if this turn of player 1 to play.

        if player1.turn == True:

            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pausebutton.isover(pos):
                        nothing()
                        pygame.display.update()

                if event.type == pygame.MOUSEMOTION:
                    if pausebutton.isover(pos):
                        pausebutton.color = green
                    else:
                        pausebutton.color = (153, 204, 0)

# control part of player 1 movement.

                if event.type == pygame.KEYDOWN:

                    if event.key == ord('a'):
                        player1.cx = -1.5

                    if event.key == ord('d'):
                        player1.cx = 1.5

                    if event.key == ord('w'):
                        player1.cy = -1.5

                    if event.key == ord('s'):
                        player1.cy = 1.5

                if event.type == pygame.KEYUP:

                    if event.key == ord('a') or event.key == ord('d'):
                        player1.cx = 0

                    if event.key == ord('w') or event.key == ord('s'):
                        player1.cy = 0

# making container for player 1.

            if player1.x <= 0:
                player1.x = 0
            elif player1.x >= 930:
                player1.x = 930

            if player1.y <= 0:
                player1.y = 0
            elif player1.y > 940:
                player1.y = 940

            flag_for_collision = False

# checking for collision by player 1 with other obstacles.

            for i in list_of_obstacles:
                if is_collision(player1.x, player1.y, i.obstacle1x,
                                i.obstacle1y) == True:
                    flag_for_collision = True
                if player1.y + 64 < i.obstacle1y and i.flago1 == False:
                    player1.score += 5
                    i.flago1 = True

            for i in list_of_movers:
                if is_collision(player1.x, player1.y, i.obstacle1x,
                                i.obstacle1y) == True:
                    flag_for_collision = True
                if player1.y + 64 < i.obstacle1y and i.flagm1 == False:
                    player1.score += 10
                    i.flagm1 = True

            if player1.y <= 20:
                player1.reached = True
                player1.score += 50
                player1.s_increment = True
            else:
                player1.reached = False
                player1.s_increment = False

            if player1.y <= 20:
                player1.level += 2

# conditions for player 1 turn to stop.

            if flag_for_collision or player1.reached == True:
                player1.x = 500
                player1.y = 940
                player1.cx = 0
                player1.cy = 0
                player1.turn = False
                player2.turn = True
                player2.time = pygame.time.get_ticks()
                screen.fill(black)
                # startingfont1 = pygame.font.SysFont('comicsansms', 90)
                # p2message =  startingfont1.render("Player 2's turn", True, winc)

                screen.blit(p2message, (290, 415))
                pygame.display.update()

                pygame.time.wait(2500)

            player1.x += player1.cx
            player1.y += player1.cy

# if this player 2 turn then the game loop will enter this if condition. 

        if player2.turn == True:

            for event in pygame.event.get():

                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pausebutton.isover(pos):
                        nothing()

                if event.type == pygame.MOUSEMOTION:
                    if pausebutton.isover(pos):
                        pausebutton.color = (0, 255, 0)
                    else:
                        pausebutton.color = (153, 204, 0)

# controls for player 2 to move within in game window.

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        player2.cx = -1.5

                    if event.key == pygame.K_RIGHT:
                        player2.cx = 1.5

                    if event.key == pygame.K_UP:
                        player2.cy = -1.5

                    if event.key == pygame.K_DOWN:
                        player2.cy = 1.5

                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT or event.key \
                        == pygame.K_RIGHT:
                        player2.cx = 0

                    if event.key == pygame.K_UP or event.key \
                        == pygame.K_DOWN:
                        player2.cy = 0

# setting container for player 2 to remain inside the game window.

            if player2.x <= 0:
                player2.x = 0
            elif player2.x >= 930:
                player2.x = 930

            if player2.y <= 0:
                player2.y = 0
            elif player2.y > 940:
                player2.y = 940

            flag1_for_collision = False

# checkinig collision player2 with other obstacles.

            for i in list_of_obstacles:
                if is_collision(player2.x, player2.y, i.obstacle1x,
                                i.obstacle1y) == True:
                    flag1_for_collision = True
                if player2.y > i.obstacle1y + 64 and i.flago2 == False:
                    player2.score += 5
                    i.flago2 = True

            for i in list_of_movers:
                if is_collision(player2.x, player2.y, i.obstacle1x,
                                i.obstacle1y) == True:
                    flag1_for_collision = True
                if player2.y > i.obstacle1y + 64 and i.flagm2 == False:
                    player2.score += 10
                    i.flagm2 = True

            if player2.y >= 930:
                player2.reached = True
                player2.score += 50
                player2.s_increment = True
            else:
                player2.reached = False
                player2.s_increment = False

            if player2.y >= 930:
                player2.level += 2

# checking condition for a round to get over i.e player2 turn gets over.

            if flag1_for_collision or player2.reached == True:
                round_number += 1
                player2.x = 500
                player2.y = 0
                player2.cx = 0
                player2.cy = 0
                player2.turn = False
                player1.turn = True
                player1.time = pygame.time.get_ticks()

                screen.fill(black)
                # startingfont1 = pygame.font.SysFont('comicsansms', 90)
                wx = 290
                if player1.s_increment and not player2.s_increment:
                    # win1 =  startingfont1.render('Player 1 WINS', True,
                            # winc)
                    screen.blit(win1, (wx, 415))

                elif player2.s_increment and not player1.s_increment:

                    # win2 =  startingfont1.render('PLAYER 2 WINS', True,
                            # winc)
                    screen.blit(win2, (wx, 415))

                elif not player1.s_increment \
                    and not player2.s_increment:

                    # win3 =  startingfont1.render('BOTH PLAYER CRASHED',
                            # True, winc)
                    wx = 150
                    screen.blit(win3, (wx, 415))

                elif player1.s_increment and player2.s_increment:

                    if player1.time > player2.time:
                        # win4 =  startingfont1.render('PLAYER 1 WINS THROUGH TIME', True,
                                # winc)
                        screen.blit(win4, (wx, 415))

                    elif player1.time < player2.time:
                        # win5 =  startingfont1.render('PLAYER 2 WINS THROUGH TIME', True,
                                # winc)
                        screen.blit(win5, (wx, 415))

                    elif player1.time == player2.time:
                        # win6 =  startingfont1.render('BOTH PLAYER WINS',
                                # True, winc)
                        wx = 170
                        screen.blit(win6, (wx, 415))


                # startingfont1 = pygame.font.SysFont('comicsansms', 90)
                player1_scr =  startingfont1.render('Player 1 score: '
                        + str(player1.score), True, winc)
                player2_scr =  startingfont1.render('Player 2 score: '
                        + str(player2.score), True, winc)
                screen.blit(player1_scr, (250, 505))
                screen.blit(player2_scr, (250, 600))

                pygame.display.update()
                pygame.time.wait(3000)
                screen.fill((0, 0, 0))
                # p1font = pygame.font.SysFont('comicsansms', 80)
                yup = p1font.render('Continue To', True, winc)
                round_num = p1font.render('Round ' + str(round_number),
                        True, winc)
                hm = p1font.render('Or Go Home', True, winc)

                # p1message = p1font.render("Player 1's turn",True,(18,97,8))

                screen.blit(yup, (330, 105))
                screen.blit(round_num, (380, 185))

                continuebutton.draw(screen, green)
                screen.blit(hm, (320, 495))
                homebutton.draw(screen, rg)

                pygame.display.update()

                pos = pygame.mouse.get_pos()

# next while loop encompases the condition to continue to next round or go to the home page.

                FLAGGG = True
                while FLAGGG:
                    if event.type == pygame.MOUSEBUTTONDOWN \
                        and (not continuebutton.isover(pos)
                             and homebutton.isover(pos)
                             or continuebutton.isover(pos)
                             and not homebutton.isover(pos)):
                        FLAGGG = False
                    screen.fill((0, 0, 0))
                    screen.blit(yup, (330, 105))
                    screen.blit(round_num, (380, 185))

                    continuebutton.draw(screen, green)
                    screen.blit(hm, (320, 495))
                    homebutton.draw(screen, rg)
                    pygame.display.update()

                    for event in pygame.event.get():

                        pos = pygame.mouse.get_pos()

                        if event.type == pygame.QUIT:
                            In_game = False
                            running = False
                            pygame.quit()
                            exit()

                        if event.type == pygame.MOUSEMOTION:
                            if continuebutton.isover(pos):
                                continuebutton.color = green
                            else:
                                continuebutton.color = (153, 204, 0)
                            if homebutton.isover(pos):
                                homebutton.color = rg
                            else:
                                homebutton.color = (255, 204, 0)

                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if continuebutton.isover(pos):
                        running = True
                    if homebutton.isover(pos):
                        running = False

                player1.score = 0
                player2.score = 0
                for i in list_of_obstacles:
                    i.flago1 = False
                    i.flago2 = False
                for i in list_of_movers:
                    i.flagm1 = False
                    i.flagm2 = False

                pygame.display.update()
                pygame.time.wait(1000)

            player2.x += player2.cx
            player2.y += player2.cy

        if player1.turn:
            player1.net_time = (pygame.time.get_ticks() - player1.time) \
                / 1000

        if player2.turn:
            player2.net_time = (pygame.time.get_ticks() - player2.time) \
                / 1000

# these codes will print the score of each player on he screen.

        # score_font = pygame.font.SysFont('comicsansms', 30)
        player1_score = score_font.render('Player1 score:'
                + str(player1.score), True, white)

        player2_score = score_font.render('Player2 score:'
                + str(player2.score), True,white)

        player1_Time = score_font.render('Player1 Time:'
                + str(player1.net_time), True, white)

        player2_Time = score_font.render('Player2 Time:'
                + str(player2.net_time), True, white)

        screen.blit(player1_score, (10, 945))
        screen.blit(player2_score, (10, 10))
        screen.blit(player1_Time, (10, 975))
        screen.blit(player2_Time, (10, 40))

        player1.show_player()
        player2.show_player()
        pygame.display.update()