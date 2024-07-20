import pygame
import time 
import random 
pygame.init()
#so first I am going to set the color i will need for the code 
white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0 , 155, 0)
snakelength = 1
direction = "right" #i defined this for later in the codew 
#now I am going to set the height and width of the display 
display_width = 800
display_height = 600
snakelist = [] #used later in code
#creating the display surface 
gameDisplay = pygame.display.set_mode((display_width, display_height))
#naming the window 
pygame.display.set_caption ("Snake Game By Neev")
#for this code I wanted to try to add pictures so I got some off the internet here is the link to the apple picture https://www.google.com/search?q=snake+game+apple+no+background+&&tbm=isch&ved=2ahUKEwj67KWQlNX_AhXhUjUKHUsmDD8Q2-cCegQIABAA&oq=snake+game+apple+no+background+&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BggAEAcQHjoGCAAQCBAeOgQIABAeOgYIABAFEB5QigdY2SFggSJoAHAAeACAAWKIAZIJkgECMTWYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=gleTZPqjGOGl1QHLzLD4Aw&bih=951&biw=1920&rlz=1C1VDKB_enCA1041CA1041#imgrc=p_4_o1uJnM1eGM
#here is the link to the snake picture https://www.google.com/search?q=snake+game+apple+no+background+&&tbm=isch&ved=2ahUKEwj67KWQlNX_AhXhUjUKHUsmDD8Q2-cCegQIABAA&oq=snake+game+apple+no+background+&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BggAEAcQHjoGCAAQCBAeOgQIABAeOgYIABAFEB5QigdY2SFggSJoAHAAeACAAWKIAZIJkgECMTWYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=gleTZPqjGOGl1QHLzLD4Aw&bih=951&biw=1920&rlz=1C1VDKB_enCA1041CA1041#imgrc=p_4_o1uJnM1eGM
apple_img = pygame.image.load('C:\Python\fwdpythonfiles\Snake Game\apple.jpg')
snake_img = pygame.image.load('C:\Python\fwdpythonfiles\Snake Game\snake.jpg')

clock = pygame.time.Clock()

blocksize = 15 
FPS = 15

lead_x_change = 10
lead_y_change = 0
def snake(snakelist): #this function will be used in order to rotate the snake head image everytime it turns 
  if direction == "right":
    head = pygame.transform.rotate(snake_img,180)
  if direction == "left":
    head = pygame.transform.rotate(snake_img)
  if direction == "up":
    head = pygame.transform.rotate(snake_img,90)
  if direction == "down":
    head = pygame.transform.rotate(snake_img,270)
  gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1])) 

for x in snakelist[:-1]:
  pygame.draw.rect(gameDisplay, green, [x[0],x[1], blocksize, blocksize])

def gameLoop(): 
 
  lead_x = display_width / 2
  lead_y = display_height / 2

  AppleX = round(random.randrange(0,display_width - blocksize)) # this part is to put the apple in random places 
  AppleY = round(random.randrange(0,display_height - blocksize))
  while not False:
    while False:
      gameDisplay.fill(white)
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit
          quit()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        quit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
          direction = "left"
          lead_x_change = -blocksize
          lead_y_change = 0 
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
          direction = "right"
          lead_x_change = blocksize
          lead_y_change = 0        
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
          direction = "up"
          lead_x_change = -blocksize
          lead_y_change = 0        
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
          direction = "down"
          lead_x_change = blocksize
          lead_y_change = 0           
  if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
    quit()
  else: 
    lead_x += lead_x_change
    lead_y += lead_y_change
  gameDisplay.fill(white)
  gameDisplay.blit(apple_img,(AppleX,AppleY))
  snakehead = []
  snakehead.append(lead_x)
  snakehead.append(lead_y)
  snakelist.append(snakehead)
  if len(snakelist) > snakelength:
    del snakelist[0]
  for eachSegment in snakelist[:-1]:
    if eachSegment == snakehead:
      quit()
  snake(blocksize, snakelist)
  pygame.display.update()
  if lead_x > AppleX and lead_x < AppleX + 30 or lead_x + blocksize > AppleX and lead_x + blocksize < AppleX + 30:
    if lead_y > AppleY and lead_y < AppleY + 30:
      randAppleX = round(random.randrange(0, display_width - blocksize))
      randAppleY = round(random.randrange(0, display_height - blocksize))
      snakelength + 1 
    elif lead_y + blocksize > AppleY and lead_y + blocksize < AppleY + 30:
      randAppleX = round(random.randrange(0, display_width - block_size))
      randAppleY = round(random.randrange(0, display_height - block_size))
      snakelength +=1
  clock.tick(FPS)
quit()
gameLoop()
      
      

  
  
    
  
  
  

  





