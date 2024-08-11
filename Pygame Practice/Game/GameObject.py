from typing import List

class GameObject:
    def __init__(self,starting_size : List[float],starting_position : List[float]):
        if(len(starting_size)!=2):
            raise ValueError("size value should only have the x axis [0] and the y axis [1]")
        self.__size : List[float] = starting_size
        if(len(starting_position)!=2):
            raise ValueError("position value should only have the x axis [0] and the y axis [1]")
        self.__position: List[float] = starting_position

    def set_size(self, size : List[float]):
        self.__size : List[float] = size

    def get_size(self):
        return self.__size

    def set_position(self, position : List[float]):
        self.__position: List[float] = position

    def get_position(self):
        return self.__position
        

