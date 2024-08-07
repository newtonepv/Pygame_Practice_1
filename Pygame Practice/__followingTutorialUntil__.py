import pygame
from sys import exit

# Frequently changed variables
maxFPSRate = 60

screen_display_size = [800,400]

sky_display_starting_size = [screen_display_size[0], screen_display_size[1]*3/4] #so it occupies 3/4 of the y axis of the screen
sky_display_starting_position = [0,0]  
sky_display_starting_image = pygame.image.load('Graphics/Backgrounds/skyBackground.jpg')

ground_display_starting_size = [screen_display_size[0], screen_display_size[1]*1/4] #so it occupies 1/4 of the y axis of the screen (the rest will be occupied by the sky)
ground_display_starting_position = [0,screen_display_size[1]*3/4] #so it starts at the end of the sky
ground_display_starting_image = pygame.image.load('Graphics/Backgrounds/groundImage.png')
#

pygame.init()
pygame.display.set_caption('Runner')# window name

clock = pygame.time.Clock() ##initializing a clock instance from pygame.time
delta = 0 # initializing the delta variable, it is the float value of the time since the last frame

screen_display = pygame.display.set_mode(screen_display_size)# screen size

##setting the displays
    #setting the sky_display
sky_display = pygame.transform.scale(sky_display_starting_image,sky_display_starting_size)
sky_display_position = sky_display_starting_position
    #
    #now the background_display
ground_display = pygame.transform.scale(ground_display_starting_image,ground_display_starting_size)
ground_display_position = ground_display_starting_position
    #
#

##setting the ground_display

#

##Game Loop
while True:
    # listen to the player input in every frame
    for event in pygame.event.get():
        # check if player wants to quit
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
            #quit the app and exit the code using the sys package
            break
    
    # Get delta time in seconds without limiting the frame rate
    #make time envolved changes in here
    
    #

    #drawing:
    screen_display.blit(sky_display, sky_display_position)##drawing the sky
    screen_display.blit(ground_display, ground_display_position)
    #
    pygame.display.update()
    delta = clock.tick()
