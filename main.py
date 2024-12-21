import pygame
import random  

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
htpbutton = pygame.image.load('htpbutton.png')
htpbuttonsize = pygame.transform.scale(htpbutton,(700,600))
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

        #kept the text empty due to the text not showing behind the button
        options_text = small_font.render("", True, white)
        options_rect = options_text.get_rect(center=(700, 400))
        screen.blit(options_text, options_rect)

        screen.blit(htpbuttonsize,(345,90))

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


    player = pygame.Rect(100,700,100,100)
    opponent = pygame.Rect(1200,700,100,100)
    ball = pygame.Rect(width // 2,height // 2,50,50)
    
    player_velocity_y = 0
    opponent_velocity_y = 0
    gravity = 0.4
    jump_strength=-12
    move_speed= 5
    ground_level = 800
    #this is split into two, one for the x axis and one for the y axis 
    #the x axis is a random choice between two, -5 or 5, and the y axis is the same for -3 and 3
    #this uses the random feature which picks randomly
    ball_velocity = [random.choice([-5, 5]), random.choice([-3, 3])]
    #this controls how much the ball keeps after it bounces
    #if this was -1, it would have to difference in the bounce and keep bouncing without loosing energy
    ball_bounce = -0.8

    clock = pygame.time.Clock()

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

                #keydown allows the use of the keyboard in oygame
                if event.type == pygame.KEYDOWN:
                    # first we check on the event the button w is pressed and the player rect is on the ground
                    # if both are true, we will see the player jump from 0 to the designed jump strength
                    # since jump strength is a variable we can control, we can control how high the player jumps
                    if event.key == pygame.K_w and player.bottom >= ground_level:
                        player_velocity_y = jump_strength
                    # same with the player's jump
                    if event.key == pygame.K_UP and opponent.bottom >= ground_level:
                        opponent_velocity_y = jump_strength

            # Get the state of all keyboard key
            keys = pygame.key.get_pressed()
            
            # if the player is not at the 0 axis / the far left and the button a is pressed, it moves at the movespeed variable in the negative which glides it to the left 
            if keys[pygame.K_a] and player.left > 0:
                player.x -= move_speed
            # same thing but is not at the width, which is the far right, and button d is pressed, its moves the player in the positive which glides it to the right 
            if keys[pygame.K_d] and player.right < width:
                player.x += move_speed
                
            # same thing as the player but with different buttons 
            if keys[pygame.K_LEFT] and opponent.left > 0:
                opponent.x -= move_speed
            if keys[pygame.K_RIGHT] and opponent.right < width:
                opponent.x += move_speed

            # putting it as >0 and <width act as a border for the player and opponent
            

            # Apply gravity and update positions for player 1
            player_velocity_y += gravity
            player.y += player_velocity_y
            
            # Apply gravity and update positions for opponent
            opponent_velocity_y += gravity
            opponent.y += opponent_velocity_y
            
            # Ground collision for player 1
            if player.bottom > ground_level:
                player.bottom = ground_level
                player_velocity_y = 0
                
            # Ground collision for opponent
            if opponent.bottom > ground_level:
                opponent.bottom = ground_level
                opponent_velocity_y = 0

            #this increases the vertical velocity by adding gravity
            ball_velocity[1] += gravity
            #updates the ball's position
            ball.x += ball_velocity[0]
            ball.y += ball_velocity[1]
            
            # since in the y axis, 0 is the highest point and height (800) is the lowest
            #so when ball hits the bottom, at the ground level/ height, it bounces back depending on the bounce
            if  ball.bottom >= height:
                ball.bottom = height
                ball_velocity[1] *= ball_bounce
            #same but not with bottom, the highest point which is 0
            if  ball.top <= 0:
                ball.top = 0
                ball_velocity[1] *= ball_bounce

            #same with the top and bottom, we do the same with the left and right
            # in the x axis, 0 is the far left and width (1400) is the far right
            if ball.left <= 0 or ball.right >= width:
                ball_velocity[0] = -ball_velocity[0]

            # first, it checks if there is a collision between the ball and the player
            # lets say the player is cut in half, if the ball hits the right side of the player, it goes to the right and vis versa
            # the vertical velocity is constant at -8
            if  ball.colliderect(player):
                ball_velocity[0] = 5 if ball.centerx > player.centerx else -5
                ball_velocity[1] = -8

            # same thing but for the opponent
            if ball.colliderect(opponent):
               ball_velocity[0] = 5 if ball.centerx > opponent.centerx else -5
               ball_velocity[1] = -8 


            screen.blit(bg,(0,0))

            # adding these would allow the objects to show up of the screen
            pygame.draw.rect(screen,red,player)
            pygame.draw.rect(screen,green,opponent)
            pygame.draw.ellipse(screen,black,ball)
            pygame.display.flip()

            clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
