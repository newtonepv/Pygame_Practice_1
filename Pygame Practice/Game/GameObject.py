from typing import List

class GameObject:
    def __init__(self,starting_size : List[float],starting_position : List[float]):
        if(len(starting_size)!=2):
            raise ValueError("starting_size must be a list of exactly 2 floats.")
        self.__size : List[float] = starting_size
        if(len(starting_position)!=2):
            raise ValueError("starting_position should be a list of exactily 2 floats.")
        self.__position: List[float] = starting_position

    def set_size(self, size : List[float]):
        self.__size : List[float] = size

    def get_size(self):
        return self.__size

    def set_position(self, position : List[float]):
        self.__position: List[float] = position

    def get_position(self):
        return self.__position
        

