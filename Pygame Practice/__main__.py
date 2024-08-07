import pygame
from sys import exit

# Frequently changed variables
maxFPSRate = 60

screen_display_size = [800,400]

sky_display_starting_size = [screen_display_size[0], screen_display_size[1]*3/4]
sky_display_starting_position = [0,0]
sky_display_starting_fill_aRGB =  [255, 0, 0, 0]
sky_display_fill_aRGB_change_speed = 0.2
#

pygame.init()
pygame.display.set_caption('Runner')

clock = pygame.time.Clock() ##initializing a clock instance from pygame.time
delta = 0 # initializing the delta variable, it is the float value of the time since the last frame

screen_display = pygame.display.set_mode(screen_display_size)


sky_display_position = sky_display_starting_position
sky_display = pygame.Surface(sky_display_starting_size)
sky_display_fill_aRGB = sky_display_starting_fill_aRGB
sky_display.fill(sky_display_fill_aRGB)


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
    delta = clock.tick()
    #make time envolved changes in here
    
    for i in range(2, 4):
        sky_display_fill_aRGB[i] += delta*sky_display_fill_aRGB_change_speed
        if sky_display_fill_aRGB[i] > 255:
            sky_display_fill_aRGB[i] = 255
            sky_display_fill_aRGB_change_speed*=-1
        elif sky_display_fill_aRGB[i] < 0:
            sky_display_fill_aRGB[i] = 0
            sky_display_fill_aRGB_change_speed*=-1
    #
    #drawing:
    screen_display.blit(sky_display, sky_display_position)

    sky_display.fill(sky_display_fill_aRGB)
    #
    pygame.display.update()
