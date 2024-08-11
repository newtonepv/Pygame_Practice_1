from typing import List
from GameObject import GameObject
from pygame import Surface, image, transform, Rect

class ImageGameObject(GameObject):
    def __init__(self,starting_size : List[float],starting_position : List[float]
                 ,image_path : str, alwaysInCamera:bool = False, isClone:bool = False):
        
        super().__init__(starting_size,starting_position)
        self.__image_path : str = image_path
        self.__alwaysInCamera : bool = alwaysInCamera
        self.__isClone:bool = isClone
        self.__clone:ImageGameObject=None
        self.__update_surface_and_rect()
    

    def __update_surface_and_rect(self):
        #updates every thing in the image surface to the setted values
        #(noramlly called on set functions)
        self.__set_loaded_image(image.load(self.__image_path).convert_alpha())
        self.__image_surface : Surface = transform.scale(
                                                self.__loaded_image
                                                ,super().get_size())
        
        self.__rectangle :Rect = self.__image_surface.get_rect(
                                    topleft = super().get_position())


    def get_rectangle(self):
        return self.__rectangle

    def get_surface(self):
        return self.__image_surface

    def set_size(self, size : List[float]):
        super().set_size(size)
        self.__update_surface_and_rect()

    def set_position(self, position : List[float]):
        super().set_position(position)
        self.__update_surface_and_rect()


    def set_image_path(self,path : str):
        self.__image_path : str = path
        self.__update_surface_and_rect()

    def get_image_path(self):
        return self.__image_path
    
    def __set_loaded_image(self,loaded_image:Surface):
        self.__loaded_image = loaded_image

    def __get_loaded_image(self):
        return self.__loaded_image

    def set_always_in_camera(self, alwaysInCamera):
        self.__alwaysInCamera = alwaysInCamera
    
    def update(self,screen_display:Surface, screen_display_size: List[int], holdingS:bool, holdingW:bool,delta_time,bunny_speed):
        if self.__clone:
                self.__clone.update(screen_display,screen_display_size, holdingS, holdingW,delta_time,bunny_speed)#recursive, until there are no more clones
          
        
        #events
        if(holdingW):
            self.set_position([self.get_position()[0]+delta_time*bunny_speed
                            ,self.get_position()[1]])
        if(holdingS):
            self.set_position([self.get_position()[0]-delta_time*bunny_speed
                            ,self.get_position()[1]])
        #
              
        if(self.__alwaysInCamera):
            
            #check if went out of bounds
            if self.get_position()[0] < -self.get_size()[0] or self.get_position()[0] > screen_display_size[0]:
                if self.__isClone:
                    # Code to destroy itself
                    return 1
                else:
                    # Turn the original into the clone
                    self.__transform_to_clone()
                    return 0
            
            #check if needs to make clones
            if self.__isClone==False:
                pos = self.get_position()[0]
                if(pos<0):
                    self.__clone = ImageGameObject(super().get_size(),
                                                   [screen_display_size[0]+pos,super().get_position()[1]],
                                                   self.get_image_path(),
                                                   alwaysInCamera=True,
                                                   isClone=True)

                elif(pos+self.get_size()[0]>screen_display_size[0]):
                    self.__clone = ImageGameObject(super().get_size(),
                                                    [-(screen_display_size[0]-pos),super().get_position()[1]],
                                                    self.get_image_path(),
                                                   alwaysInCamera=True,
                                                   isClone=True)
        screen_display.blit(self.get_surface(),self.get_rectangle())
        

    def __transform_to_clone(self):
        if self.__clone:
            # The clone's attributes become the main object's attributes
            self.__image_path = self.__clone.__image_path
            self.set_position(self.__clone.get_position())
            self.set_size(self.__clone.get_size())
            self.set_image_path(self.__clone.get_image_path())
            self.set_always_in_camera(self.__clone.__alwaysInCamera)

            # The clone is no longer needed
            self.__clone = None