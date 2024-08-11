import pygame
pygame.init()
pygame.font.init()

from ImageGameObject import ImageGameObject
from sys import exit

#paths
path_to_characters_sprites_folder = "../Graphics/Sunny Land Collection Files/Sunny Land Collection Files/Assets/Characters"
#
# Frequently changed variables
maxFPSRate = 60
screen_display_size = [800,400]

##setting the displays
    #setting the sky_display
sky_display_starting_size = [screen_display_size[0], screen_display_size[1]*3/4] #so it occupies 3/4 of the y axis of the screen
sky_display_starting_position = [0,0]  
sky_display_starting_image = pygame.image.load('../Graphics/Backgrounds/skyBackground.jpg')
sky_display = pygame.transform.scale(sky_display_starting_image,sky_display_starting_size)
sky_display_position = sky_display_starting_position
    #
    #now the ground_display
ground_display_starting_size = [screen_display_size[0], screen_display_size[1]*1/4] #so it occupies 1/4 of the y axis of the screen (the rest will be occupied by the sky)
ground_display_starting_position = [0,screen_display_size[1]*3/4] #so it starts at the end of the sky
ground_display_starting_image = pygame.image.load('../Graphics/Backgrounds/groundImage.png')
ground_display = pygame.transform.scale(ground_display_starting_image,ground_display_starting_size)
ground_display_position = ground_display_starting_position
    #
    #player display
bunny_png_height_px = 50
bunny_display_starting_size = [screen_display_size[0]/30,screen_display_size[1]/8]
bunny_display_position = [screen_display_size[0]/20,
                                screen_display_size[1]-(screen_display_size[1]-
                                ground_display_position[1])-bunny_png_height_px]
                                #this will make the feet of the bunny touch the ground
bunny_display_starting_image = pygame.image.load(path_to_characters_sprites_folder+'/sunny-bunny/Sprites/idle/_0000_Layer-1.png')
bunny_display_position = bunny_display_position
bunny_display = pygame.transform.scale(bunny_display_starting_image,bunny_display_starting_size)

    #
#
#text
text_display_position = [screen_display_size[0]/3,screen_display_size[1]/10]
text_display_font = pygame.font.Font(None, 50)
text_display_color = 'Green'
text_display_AA = False
text_display_Content = 'game text'
text_display = text_display_font.render(text_display_Content, text_display_AA, text_display_color)
#

pygame.display.set_caption('Runner')# window name

clock = pygame.time.Clock() ##initializing a clock instance from pygame.time
deltaTime = 0 # initializing the delta variable, it is the float value of the time since the last frame

screen_display = pygame.display.set_mode(screen_display_size)# screen size



holdingW = False
holdingS = False
deltaPos = 0.0

gameObject = ImageGameObject([50,100], [0,0], "../Graphics/Sunny Land Collection Files/Sunny Land Collection Files/Assets/Characters/sunny-bunny/Sprites/idle/_0000_Layer-1.png")

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
    
    
    #make time envolved changes in here
    
    if(holdingW):
        gameObject.set_image_path("../Graphics/Sunny Land Collection Files/Sunny Land Collection Files/Assets/Characters/sunny-bunny/Sprites/jump/_0000_Layer-1.png")
    if(holdingS):
        gameObject.set_image_path("../Graphics/Sunny Land Collection Files/Sunny Land Collection Files/Assets/Characters/sunny-bunny/Sprites/idle/_0000_Layer-1.png")
        
    #

    #drawing:

    screen_display.blit(sky_display, sky_display_position)##drawing the sky
    screen_display.blit(ground_display, ground_display_position)##ground
    screen_display.blit(text_display, text_display_position)##text
    screen_display.blit(bunny_display,bunny_display_position)##bunny
    screen_display.blit(gameObject.getSurface(),gameObject.get_position())
    #
    pygame.display.update()
    # Get delta time in seconds without limiting the frame rate
    deltaTime = clock.tick()
