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

info_font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 50)
large_font = pygame.font.Font(None, 100)

#loading the images and connecting them to variables
logo = pygame.image.load('logo.png')
playbutton = pygame.image.load('play_button_updated-removebg-preview.png')
infobutton = pygame.image.load('options_for_info_-removebg-preview.png')
bg = pygame.image.load('background.jpg')
# Scale the background image to match the screen size
bg = pygame.transform.scale(bg, (width, height))

#nameing the title of the game and adding the logo of the game
pygame.display.set_caption("Srh Project - Head Soccer")
pygame.display.set_icon(logo)

def main_menu():
    menurunning = True
    while menurunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    options()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

        #add the fill of the screen to the desired color
        screen.fill(menucolor)
        #adds the logo in the x and y axis
        screen.blit(logo,(425, 50))
        
        
        # play text is the text, and rect creates a rectangle is a x and y coordinates, blit combines the two
        Play_text = large_font.render("Play", True, white)
        Play_rect = Play_text.get_rect(center=(700,400))
        screen.blit(Play_text, Play_rect)

        #place the button above the play text and rect but still act the same, if the code is above the player text and rect line, the white text would overlay the image
        screen.blit(playbutton,(590,353))

        screen.blit(infobutton,(590,480))

        # same as the play but for the instructions
        Instructions_text = info_font.render("Press space to Play", True, white)
        Instructions_rect = Instructions_text.get_rect(center=(700,700))
        screen.blit(Instructions_text, Instructions_rect)

        Instructions_text = info_font.render("Press Tab for How To Play", True, white)
        Instructions_rect = Instructions_text.get_rect(center=(700,750))
        screen.blit(Instructions_text, Instructions_rect)

        pygame.display.flip() 

def options():
    while True:
        screen.fill(menucolor)

        # Corrected syntax: Replace ':' with '=' for text and rect
        options_text = small_font.render("Use W,A,D to control player one and use UP,LEFT,RIGHT to control player two", True, white)
        options_rect = options_text.get_rect(center=(700, 400))
        screen.blit(options_text, options_rect)

        Instructions_text = small_font.render("Press Backspace to Return", True, white)
        Instructions_rect = Instructions_text.get_rect(center=(700,700))
        screen.blit(Instructions_text, Instructions_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return  # Exit options to main menu
                
        pygame.display.flip()

def main():
    mainrunning = True
    game_mode = None
    is_paused = False
    
    while mainrunning:
        if game_mode is None:
            # true means space is presses, False if screen shuts down
            if main_menu():
                game_mode = "game"
            else:
                mainrunning = False
        else:
            for event in pygame.event.get():
                # if you want to break the loop, we will change the variable of runnning into false 
                if event.type == pygame.QUIT:
                    mainrunning = False

            screen.blit(bg,(0,0))
            pygame.display.flip()

if __name__ == "__main__":
    main()
