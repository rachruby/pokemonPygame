# Pokemon Game Simulation with Pygame
# Date: Dec.7, 2020
# Author: Rachel Zhang
# Description: This program is a Pokemon game, where user and computer compete using their pre-determined Pokemons.

import pygame, sys, os 
from pygame import *

# Start up pygame
pygame.init()

# Setting up the window where we will draw our shapes and display animations
# The numbers represent the resolution of the screen
WIN = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Pokemon Game Simulation')

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
LIGHTBROWN = (199,167,93)
BLUE = (0,0,255)
DARKGREEN = (23,85,16)
LIGHTGRAY = (249,249,249)
GRAY = (128,128,128)
# Creating font sizes
font = pygame.font.SysFont("Comic Sans MS",25)
menu_font = pygame.font.SysFont("Comic Sans MS",30)
instructions_font = pygame.font.SysFont("Comic Sans MS", 20)
ESC_font = pygame.font.SysFont("Comic Sans MS", 18)
textbox = pygame.font.SysFont("Comic Sans MS",21)
def drawText(text, font, color, surface, x, y):
    graphics = font.render(text,1,color)
    WIN.blit(graphics,(x,y))

click = False
# Menu Page main loop
def menu_page():
    
    # Background Picture for Menu Page
    loc = os.getcwd()
    img = 'background.png'
    path = loc + "\\" + img
    img_background = pygame.image.load(path)
    imgX = 0
    imgY = 0
    # Background music
    loc_music = os.getcwd()
    music = '101 - opening.ogg'
    path_music = loc_music + "\\" + music
    theme = pygame.mixer.music.load('101 - opening.ogg')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops = -1)

    # User Picture
    loc_user = os.getcwd()
    img_user = 'user.png'
    path_user = loc_user + "\\" + img_user
    image_user = pygame.image.load(path_user)
    userX = 300
    userY = 520
    speedX = 2
    speedY = 2

    # Trainer Picture
    loc_trainer = os.getcwd()
    img_trainer = 'trainer.png'
    path_trainer = loc_trainer + "\\" + img_trainer
    image_trainer = pygame.image.load(path_trainer)
    trainerX = 300
    trainerY = 50
    trainerspeed = 250

    # Sound Effect
    loc_bonus = os.getcwd()
    sound_bonus = 'bonus.wav'
    path_bonus = loc_bonus + "\\" + sound_bonus
    bonus = pygame.mixer.Sound('bonus.wav')
    bonus.set_volume(0.7)
    
    while True:
        WIN.fill(BLACK)
        WIN.blit(img_background,(imgX,imgY))
        pokeball = pygame.draw.circle(WIN,RED,(300,255),15)
        WIN.blit(image_user,(userX,userY))
        trainer = WIN.blit(image_trainer,(trainerX,trainerY))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if userX > 0:
                userX = userX - speedX
        if keys[pygame.K_RIGHT]:
            if userX < 547:
                userX = userX + speedX
        if keys[pygame.K_UP]:
            if userY > 0:
                userY = userY - speedY

        if keys[pygame.K_DOWN]:
            if userY < 522:
                userY = userY + speedY

        if 275<userX<310 and 245<userY<260:
            pokeball = pygame.draw.circle(WIN,LIGHTGRAY,(300,255),15)
            pygame.display.update()

            trainerY = trainerY + 2
            if 245<trainerY<260:
                trainerY = userY
            pygame.draw.rect(WIN,LIGHTGRAY,(0,400,600,200))
            drawText("Hey! You have Pokemon! Come on! Press SPACE to play", textbox,(BLACK),WIN,50,400)
            bonus.play()
            
        if keys[pygame.K_SPACE]:
            instructions()
            

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

# Instructions Page loop
def instructions():
    run = True
    # Background Picture for Menu Page
    loc = os.getcwd()
    img = 'background.png'
    path = loc + "\\" + img
    img_background = pygame.image.load(path)
    imgX = 0
    imgY = 0

    while run:
        WIN.fill(BLACK)
        pygame.time.delay(5)
        if imgX == imgX:
            imgX = imgX + 5
            imgY = imgY - 5 
            WIN.blit(img_background,(imgX,imgY))
            if imgX > 600:
                game()
                
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        pygame.display.update()

# Game Page loop                     
def game():
    run = True
    # User Picture
    user_loc = os.getcwd()
    user_img = 'user_game.png'
    user_path = user_loc + "\\" + user_img
    user_image = pygame.image.load(user_path)
    user_X = 0
    user_Y = 320
    # Pikachu Picture
    pika_loc = os.getcwd()
    pika_img = 'pika.png'
    pika_path = pika_loc + "\\" + pika_img
    pika_image = pygame.image.load(pika_path)
    pika_X = 60
    pika_Y = 320
    
    # Trainer Picture
    loc_trainer = os.getcwd()
    img_trainer = 'trainer.png'
    path_trainer = loc_trainer + "\\" + img_trainer
    image_trainer = pygame.image.load(path_trainer)
    trainerX = 400
    trainerY = 50

    # Inkay Picture
    loc_inkay = os.getcwd()
    img_inkay = 'inkay.png'
    path_inkay = loc_inkay + "\\" + img_inkay
    image_inkay = pygame.image.load(path_inkay)
    inkayX = 430
    inkayY = 50


       
    while run:
        WIN.fill(WHITE)  
        WIN.blit(user_image,(user_X,user_Y))
        WIN.blit(pika_image,(pika_X,pika_Y))

        # PIKA's Initial Health Point
        PIKA1 = pygame.draw.circle(WIN,RED,(500,350),15)
        PIKA2 = pygame.draw.circle(WIN,RED,(540,350),15)
        PIKA3 = pygame.draw.circle(WIN,RED,(580,350),15)
        drawText("PIKACHU HEALTH POINTS", ESC_font,(BLACK),WIN,360,370)

        
        WIN.blit(image_trainer,(trainerX,trainerY))
        WIN.blit(image_inkay,(inkayX,inkayY))
        pygame.draw.rect(WIN,GRAY,(0,400,600,200))

        # INKAY's Initial Health Point 
        INKAY1 = pygame.draw.circle(WIN,RED,(20,50),15)
        INKAY2 = pygame.draw.circle(WIN,RED,(60,50),15)
        INKAY3 = pygame.draw.circle(WIN,RED,(100,50),15)
        drawText("INKAY HEALTH POINTS", ESC_font,(BLACK),WIN,2,10)

        drawText("Inkay! What will Pikachu do?", textbox,(BLACK),WIN,50,400)
        drawText("Press SPACE BAR TO ATTACK!", textbox,(BLACK),WIN,50,461)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pika_attack()
   
            

        # User moving keys      
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
 
        
        pygame.display.update()
def pika_attack():
    run = True
    # User Picture
    user_loc = os.getcwd()
    user_img = 'user_game.png'
    user_path = user_loc + "\\" + user_img
    user_image = pygame.image.load(user_path)
    user_X = 0
    user_Y = 320
    # Pikachu Picture
    pika_loc = os.getcwd()
    pika_img = 'pika.png'
    pika_path = pika_loc + "\\" + pika_img
    pika_image = pygame.image.load(pika_path)
    pika_X = 60
    pika_Y = 320
    
    # Trainer Picture
    loc_trainer = os.getcwd()
    img_trainer = 'trainer.png'
    path_trainer = loc_trainer + "\\" + img_trainer
    image_trainer = pygame.image.load(path_trainer)
    trainerX = 400
    trainerY = 50

    # Inkay Picture
    loc_inkay = os.getcwd()
    img_inkay = 'inkay.png'
    path_inkay = loc_inkay + "\\" + img_inkay
    image_inkay = pygame.image.load(path_inkay)
    inkayX = 430
    inkayY = 50


       
    while run:
        WIN.fill(WHITE)
        pygame.time.delay(1500)        
        WIN.blit(user_image,(user_X,user_Y))
        WIN.blit(pika_image,(pika_X,pika_Y))

        # PIKA's Initial Health Point
        PIKA1 = pygame.draw.circle(WIN,RED,(500,350),15)
        PIKA2 = pygame.draw.circle(WIN,RED,(540,350),15)
        PIKA3 = pygame.draw.circle(WIN,RED,(580,350),15)
        drawText("PIKACHU HEALTH POINTS", ESC_font,(BLACK),WIN,360,370)

        
        WIN.blit(image_trainer,(trainerX,trainerY))
        WIN.blit(image_inkay,(inkayX,inkayY))
        pygame.draw.rect(WIN,GRAY,(0,400,600,200))

        # INKAY's Initial Health Point 
        INKAY1 = pygame.draw.circle(WIN,RED,(20,50),15)
        INKAY2 = pygame.draw.circle(WIN,RED,(60,50),15)
        INKAY3 = pygame.draw.circle(WIN,LIGHTBROWN,(100,50),15)
        drawText("INKAY HEALTH POINTS", ESC_font,(BLACK),WIN,2,10)
        drawText("THUNDER!!! INKAY HEALTH POINT -1!", textbox,(BLACK),WIN,50,400)
        drawText("Press SPACE to continue...", textbox,(BLACK),WIN,50,461)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            inkay_attack()
        pygame.display.update() 
            

        # User moving keys      
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
def inkay_attack():
    run = True
    # User Picture
    user_loc = os.getcwd()
    user_img = 'user_game.png'
    user_path = user_loc + "\\" + user_img
    user_image = pygame.image.load(user_path)
    user_X = 0
    user_Y = 320
    # Pikachu Picture
    pika_loc = os.getcwd()
    pika_img = 'pika.png'
    pika_path = pika_loc + "\\" + pika_img
    pika_image = pygame.image.load(pika_path)
    pika_X = 60
    pika_Y = 320
    
    # Trainer Picture
    loc_trainer = os.getcwd()
    img_trainer = 'trainer.png'
    path_trainer = loc_trainer + "\\" + img_trainer
    image_trainer = pygame.image.load(path_trainer)
    trainerX = 400
    trainerY = 50

    # Inkay Picture
    loc_inkay = os.getcwd()
    img_inkay = 'inkay.png'
    path_inkay = loc_inkay + "\\" + img_inkay
    image_inkay = pygame.image.load(path_inkay)
    inkayX = 430
    inkayY = 50

 
       
    while run:
        WIN.fill(WHITE)
        pygame.time.delay(1500)
        WIN.blit(user_image,(user_X,user_Y))
        WIN.blit(pika_image,(pika_X,pika_Y))

        # PIKA's Initial Health Point
        PIKA1 = pygame.draw.circle(WIN,RED,(500,350),15)
        PIKA2 = pygame.draw.circle(WIN,LIGHTBROWN,(540,350),15)
        PIKA3 = pygame.draw.circle(WIN,LIGHTBROWN,(580,350),15)
        drawText("PIKACHU HEALTH POINTS", ESC_font,(BLACK),WIN,360,370)

        
        WIN.blit(image_trainer,(trainerX,trainerY))
        WIN.blit(image_inkay,(inkayX,inkayY))
        pygame.draw.rect(WIN,GRAY,(0,400,600,200))

        # INKAY's Initial Health Point 
        INKAY1 = pygame.draw.circle(WIN,RED,(20,50),15)
        INKAY2 = pygame.draw.circle(WIN,RED,(60,50),15)
        INKAY3 = pygame.draw.circle(WIN,LIGHTBROWN,(100,50),15)
        drawText("INKAY HEALTH POINTS", ESC_font,(BLACK),WIN,2,10)
        # TEXT BOX
        drawText("INKAY'S TURN!!!", textbox,(BLACK),WIN,50,400)
        drawText("SPLASH!!! PIKACHU'S HEALTH POINT -2!", textbox,(BLACK),WIN,50,461)
        drawText("Press SPACE to ATTACK BACK, COME ON!", textbox,(BLACK),WIN,50,490)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pikachu_attack1()
        pygame.display.update() 
            

        # User moving keys      
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


def pikachu_attack1():
    run = True
    # User Picture
    user_loc = os.getcwd()
    user_img = 'user_game.png'
    user_path = user_loc + "\\" + user_img
    user_image = pygame.image.load(user_path)
    user_X = 0
    user_Y = 320
    # Pikachu Picture
    pika_loc = os.getcwd()
    pika_img = 'pika.png'
    pika_path = pika_loc + "\\" + pika_img
    pika_image = pygame.image.load(pika_path)
    pika_X = 60
    pika_Y = 320
    
    # Trainer Picture
    loc_trainer = os.getcwd()
    img_trainer = 'trainer.png'
    path_trainer = loc_trainer + "\\" + img_trainer
    image_trainer = pygame.image.load(path_trainer)
    trainerX = 400
    trainerY = 50

    # Inkay Picture
    loc_inkay = os.getcwd()
    img_inkay = 'inkay.png'
    path_inkay = loc_inkay + "\\" + img_inkay
    image_inkay = pygame.image.load(path_inkay)
    inkayX = 430
    inkayY = 50


       
    while run:
        WIN.fill(WHITE)
        pygame.time.delay(1500)
        WIN.blit(user_image,(user_X,user_Y))
        WIN.blit(pika_image,(pika_X,pika_Y))

        # PIKA's Initial Health Point
        PIKA1 = pygame.draw.circle(WIN,RED,(500,350),15)
        PIKA2 = pygame.draw.circle(WIN,LIGHTBROWN,(540,350),15)
        PIKA3 = pygame.draw.circle(WIN,LIGHTBROWN,(580,350),15)
        drawText("PIKACHU HEALTH POINTS", ESC_font,(BLACK),WIN,360,370)

        
        WIN.blit(image_trainer,(trainerX,trainerY))
        WIN.blit(image_inkay,(inkayX,inkayY))
        pygame.draw.rect(WIN,GRAY,(0,400,600,200))

        # INKAY's Initial Health Point 
        INKAY1 = pygame.draw.circle(WIN,RED,(20,50),15)
        INKAY2 = pygame.draw.circle(WIN,LIGHTBROWN,(60,50),15)
        INKAY3 = pygame.draw.circle(WIN,LIGHTBROWN,(100,50),15)
        drawText("INKAY HEALTH POINTS", ESC_font,(BLACK),WIN,2,10)
        # TEXT BOX
        drawText("THUNDER!!! SUPER EFFECTIVE!", textbox,(BLACK),WIN,50,400)
        drawText("INKAY'S HEALTH POINT -1!", textbox,(BLACK),WIN,50,461)
        drawText("Press SPACE to continue...", textbox,(BLACK),WIN,50,490)
        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            inkay_attack1()
        pygame.display.update() 
            

        # User moving keys      
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

def inkay_attack1():
    run = True
    # User Picture
    user_loc = os.getcwd()
    user_img = 'user_game.png'
    user_path = user_loc + "\\" + user_img
    user_image = pygame.image.load(user_path)
    user_X = 0
    user_Y = 320
    # Pikachu Picture
    pika_loc = os.getcwd()
    pika_img = 'pika.png'
    pika_path = pika_loc + "\\" + pika_img
    pika_image = pygame.image.load(pika_path)
    pika_X = 60
    pika_Y = 320
    
    # Trainer Picture
    loc_trainer = os.getcwd()
    img_trainer = 'trainer.png'
    path_trainer = loc_trainer + "\\" + img_trainer
    image_trainer = pygame.image.load(path_trainer)
    trainerX = 400
    trainerY = 50

    # Inkay Picture
    loc_inkay = os.getcwd()
    img_inkay = 'inkay.png'
    path_inkay = loc_inkay + "\\" + img_inkay
    image_inkay = pygame.image.load(path_inkay)
    inkayX = 430
    inkayY = 50


       
    while run:
        WIN.fill(WHITE)
        pygame.time.delay(1500)
        WIN.blit(user_image,(user_X,user_Y))
        WIN.blit(pika_image,(pika_X,pika_Y))

        # PIKA's Initial Health Point
        PIKA1 = pygame.draw.circle(WIN,RED,(500,350),15)
        PIKA2 = pygame.draw.circle(WIN,LIGHTBROWN,(540,350),15)
        PIKA3 = pygame.draw.circle(WIN,LIGHTBROWN,(580,350),15)
        drawText("PIKACHU HEALTH POINTS", ESC_font,(BLACK),WIN,360,370)

        
        WIN.blit(image_trainer,(trainerX,trainerY))
        WIN.blit(image_inkay,(inkayX,inkayY))
        pygame.draw.rect(WIN,GRAY,(0,400,600,200))

        # INKAY's Initial Health Point 
        INKAY1 = pygame.draw.circle(WIN,RED,(20,50),15)
        INKAY2 = pygame.draw.circle(WIN,LIGHTBROWN,(60,50),15)
        INKAY3 = pygame.draw.circle(WIN,LIGHTBROWN,(100,50),15)
        drawText("INKAY HEALTH POINTS", ESC_font,(BLACK),WIN,2,10)
        # TEXT BOX
        drawText("INKAY'S TURN! SUPER!", textbox,(BLACK),WIN,50,400)
        drawText("SPLASH! PIKACHU'S HEALTH POINT -2!", textbox,(BLACK),WIN,50,461)

        pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            result()
        pygame.display.update() 
            

        # User moving keys      
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


def result():
    run = True
    # Trainer Picture
    loc_trainer = os.getcwd()
    img_trainer = 'james.png'
    path_trainer = loc_trainer + "\\" + img_trainer
    image_trainer = pygame.image.load(path_trainer)
    trainerX = 300
    trainerY = 150
    # Inkay Picture
    loc_inkay = os.getcwd()
    img_inkay = 'pokemon.png'
    path_inkay = loc_inkay + "\\" + img_inkay
    image_inkay = pygame.image.load(path_inkay)
    inkayX = 390
    inkayY = 400

       
    while run:
        WIN.fill(WHITE)        
        WIN.blit(image_trainer,(trainerX,trainerY))
        WIN.blit(image_inkay,(inkayX,inkayY))
        # TEXT BOX
        drawText("YOU LOST!",menu_font, (BLACK), WIN, 20,220)
        drawText("Trainer James and Inkay won!", textbox,(BLACK),WIN,20,400)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        pygame.display.update()
 
menu_page()
