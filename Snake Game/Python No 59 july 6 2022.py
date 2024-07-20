import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 170, 0)
img = pygame.image.load("snake.png")
img = pygame.transform.scale(img,(30,30))

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('')

clock = pygame.time.Clock()

block_size = 20
FPS = 30

fontsmall = pygame.font.SysFont("comicsansms", 20)
fontnormal = pygame.font.SysFont("comicsansms", 50)
fontbig = pygame.font.SysFont("comicsansms", 80)

direction = "left"
def snake(block_size, snakelist):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = pygame.transform.rotate(img,0)

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def text1(size,text,color):
    if size== "small":
        textsurface = fontsmall.render(text,True,color)
    if size== "normal":
        textsurface = fontnormal.render(text,True,color)
    if size== "big":
        textsurface = fontbig.render(text,True,color)
    return textsurface, textsurface.get_rect()

def message_to_screen(msg, color,size):
    text2,textrect = text1(size,msg,color)
    textrect.centre = (display_width/2), (display_height/2)
    gameDisplay.blit(text2,textrect)
def introduction():
    intro = True
    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        intro = False



def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    appleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
    appleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
    EX = round(random.randrange(0,display_width - block_size))
    EY = round(random.randrange(0,display_height - block_size))

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -4
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 4
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -4
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 4
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        
        AppleThickness = 20
        pygame.draw.rect(gameDisplay, red, [appleX, appleY, AppleThickness, AppleThickness])
        pygame.draw.rect(gameDisplay,black,[EX, EY,20,20] )
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        pygame.display.update()

        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0, display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height-block_size))#/10.0)*10.0
                snakeLength += 1

        if lead_x > appleX and lead_x < appleX + AppleThickness or lead_x + block_size > appleX and lead_x + block_size < appleX + AppleThickness:
        
            if lead_y > appleY and lead_y < appleY + AppleThickness:

                appleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                appleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                snakeLength += 3

            elif lead_y + block_size > appleY and lead_y + block_size < appleY + AppleThickness:

                appleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                appleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                snakeLength += 3
        if lead_x > EX and lead_x < EX + AppleThickness or lead_x + block_size > EX and lead_x + block_size < EX + AppleThickness:
        
            if lead_y > EY and lead_y < EY + AppleThickness:

                EX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                EY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                del snakeList [0]
                snakeLength -= 3

            elif lead_y + block_size > appleY and lead_y + block_size < appleY + AppleThickness:

                EX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                EY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                del snakeList [0]
                snakeLength -= 3
        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()















