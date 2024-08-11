from typing import List
from GameObject import GameObject
from pygame import Surface, image, transform

class ImageGameObject(GameObject):
    def __init__(self,starting_size : List[float],starting_position : List[float]
                 ,image_path : str):
        
        super().__init__(starting_size,starting_position)
        self.__image_path : str = image_path
        
        self.__update_entire_image_surface()
    

    def __update_entire_image_surface(self):
        #updates every thing in the image surface to the setted values
        #(noramlly called on set functions)
        self.__set_loaded_image(image.load(self.__image_path))
        self.__image_surface : Surface = transform.scale(
                                                self.__loaded_image
                                                ,super().get_size())

    def get_surface(self):
        return self.__image_surface

    def set_size(self, size : List[float]):
        super().set_size(size)
        self.__update_entire_image_surface()


    def set_image_path(self,path : str):
        self.__image_path : str = path
        self.__update_entire_image_surface()

    def get_image_path(self):
        return self.__image_path
    
    def __set_loaded_image(self,loaded_image:Surface):
        self.__loaded_image = loaded_image

    def __get_loaded_image(self):
        return self.__loaded_image

