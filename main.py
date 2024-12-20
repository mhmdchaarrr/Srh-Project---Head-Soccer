import pygame  

pygame.init

#setting up the width and height to set it up for the screen or display size
width = 1400
height = 800

#uses the width and height variables for the screen size 
screen = pygame.display.set_mode((width, height))

#loading the images and connecting them to variables

logo = pygame.image.load('logo.png')
bg = pygame.image.load('background.jpg')

#nameing the the title of the game and adding the logo of the game
pygame.display.set_caption("Srh Project - Head Soccer")
pygame.display.set_icon(logo)

#event loop , when variable running is true which tells us the screen will run while it is true 
running = True
while running:
    for event in pygame.event.get():
        # if you want to break the loop, we will change the variable of runnning into false 
        if event.type == pygame.QUIT:
            running = False