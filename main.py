import pygame  

#added () to the text
pygame.init()

#setting up the width and height to set it up for the screen or display size
width = 1400
height = 800

#uses the width and height variables for the screen size 
screen = pygame.display.set_mode((width, height))

#adding needed colors for the objects
white = (255,255,255)
black = (0,0,0)
gray = (200,200,200)
red = (255,0,0)
green = (0,255,0)
menucolor = (9,36,96)

# creating a small and large fonts for the game

small_font = pygame.font.Font(None, 50)
large_font = pygame.font.Font(None, 100)

#loading the images and connecting them to variables
logo = pygame.image.load('logo.png')
bg = pygame.image.load('background.jpg')
# Scale the background image to match the screen size
bg = pygame.transform.scale(bg, (width, height))

#nameing the title of the game and adding the logo of the game
pygame.display.set_caption("Srh Project - Head Soccer")
pygame.display.set_icon(logo)

def main_menu():
    
    while True:
        screen.fill(menucolor)

        screen.blit(logo,(425, 50))

        Play_text = large_font.render("Play", True, white)
        Play_rect = Play_text.get_rect(center=(700,400))
        screen.blit(Play_text,Play_rect)

        Instructions_text=small_font.render("Press space to Play", True, white)
        Instructions_rect=Instructions_text.get_rect(center=(700,700))
        screen.blit(Instructions_text,Instructions_rect)

        pygame.display.flip()


def main():
    
    game_mode = None
    is_paused = False
    
    #event loop , when variable running is true which tells us the screen will run while it is true 
    running = True
    while running:
        if game_mode is None:
            main_menu()
            for event in pygame.event.get():
                # if you want to break the loop, we will change the variable of runnning into false 
                if event.type == pygame.QUIT:
                    running = False

    screen.blit(bg,(0,0))
    pygame.display.update()

if __name__ == "__main__":
    main()