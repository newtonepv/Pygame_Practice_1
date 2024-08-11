from typing import List
from GameObject import GameObject
import pygame

class ImageGameObject(GameObject):
    def __init__(self,starting_size : List[float],starting_position : List[float]
                 ,image_path : str):
        
        super().__init__(starting_size,starting_position)
        self.__image_path : str = image_path
        
        self.__update_entire_image_surface()
    

    def __update_entire_image_surface(self):
        #updates every thing in the image surface to the setted values
        #(noramlly called on set functions)
        self.__set_loaded_image(pygame.image.load(self.__image_path))
        self.__image_surface : pygame.Surface = pygame.transform.scale(
                                                self.__loaded_image
                                                ,super().get_size())
        print(super().get_size())
        print(self.__image_path)

    def getSurface(self):
        return self.__image_surface

    def set_size(self, size : List[float]):
        super().set_size(size)
        self.__update_entire_image_surface()


    def set_image_path(self,path : str):
        self.__image_path : str = path
        self.__update_entire_image_surface()

    def get_image_path(self):
        return self.__image_path
    
    def __set_loaded_image(self,loaded_image:pygame.Surface):
        self.__loaded_image = loaded_image

    def get_loaded_image(self):
        return self.__loaded_image

