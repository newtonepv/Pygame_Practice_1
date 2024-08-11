from typing import List
import pygame
pygame.init()
pygame.font.init()
pygame.display.set_caption('Runner')# window name

from ImageGameObject import ImageGameObject
from TextUI import TextUI
from sys import exit

#paths
characters_sprites_folder_path = "../Graphics/Sunny Land Collection Files/Sunny Land Collection Files/Assets/Characters"
#

# Function returns the bunny game object
def create_bunny(bunny_position_x:float):
    bunny_size = [screen_display_size[0]/30,screen_display_size[1]/8]

                            # this will make the feet of the bunny touch the ground
    bunny_image_path = characters_sprites_folder_path+'/sunny-bunny/Sprites/idle/_0000_Layer-1.png'
    bunny_position = [bunny_position_x,ground_game_object.get_position()[1]-bunny_size[1]]
    return  ImageGameObject(bunny_size,bunny_position,bunny_image_path)
    
# Function returns the sky game object
def create_sky():
    sky_size = [screen_display_size[0], screen_display_size[1]*3/4] #so it occupies 3/4 of the y axis of the screen
    sky_position = [0,0]  
    sky_image_path = '../Graphics/Backgrounds/skyBackground.jpg'
    return ImageGameObject(sky_size,sky_position,sky_image_path)

#Function returns the ground game object
def create_ground():
    ground_size = [screen_display_size[0], screen_display_size[1]*1/4] #so it occupies 1/4 of the y axis of the screen (the rest will be occupied by the sky)
    ground_position = [0,screen_display_size[1]*3/4] #so it starts at the end of the sky
    ground_image_path = '../Graphics/Backgrounds/groundImage.png'
    return ImageGameObject(ground_size, ground_position, ground_image_path)

#Function returns the text
def create_H1_Text():
    position = [screen_display_size[0]/3,screen_display_size[1]/10]
    font = pygame.font.Font(None, 50)
    color = 'Green'
    antiAlising = False
    content = 'game text'
    return TextUI(None, 50, position, color, content, antiAlising)


maxFPSRate = 60
screen_display_size = [800,400]

##setting the displays
    #creating the sky go
sky_game_object = create_sky()
    #
    #creating the ground go
ground_game_object = create_ground()
    #
    #creating the bunny go
bunny_game_object = create_bunny(10)
bunny_speed = 0.1
    #
#
#text
h1Text_textUI = create_H1_Text()
#


clock = pygame.time.Clock() ##initializing a clock instance from pygame.time
delta_time = 0 # initializing the delta variable, it is the float value of the time since the last frame

screen_display = pygame.display.set_mode(screen_display_size)# screen size


#game loop variables
holdingW = False
holdingS = False
deltaPos = 0.0
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

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_w):
                holdingW=True
            if(event.key == pygame.K_s):
                holdingS=True

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_w):
                holdingW=False
            if(event.key == pygame.K_s):
                holdingS=False
    #end of event listening
    
    #make time envolved changes in here
    
    if(holdingW):
        bunny_game_object.set_position([bunny_game_object.get_position()[0]+delta_time*bunny_speed
                                        ,bunny_game_object.get_position()[1]])
    if(holdingS):
        bunny_game_object.set_position([bunny_game_object.get_position()[0]-delta_time*bunny_speed
                                        ,bunny_game_object.get_position()[1]])
       
    #

    #drawing:

    screen_display.blit(sky_game_object.get_surface(), sky_game_object.get_position())##drawing the sky
    screen_display.blit(ground_game_object.get_surface(), ground_game_object.get_position())##ground
    screen_display.blit(h1Text_textUI.get_text_surface(), h1Text_textUI.get_position())##text
    screen_display.blit(bunny_game_object.get_surface(),bunny_game_object.get_position())##bunny
    #
    pygame.display.update()
    # Get delta time in seconds without limiting the frame rate
    delta_time = clock.tick()
