from typing import Union, List
from pygame import font, Surface

class TextUI:
    def __init__(self, font: font.Font | None, font_size: float, position: List[float], color: Union[List[int], str], content: str, anti_alising: bool):
        self.__font: font.Font | None = font
        if font_size <= 0:
            raise ValueError("font_size should be higher than 0")
        if len(position) != 2:
            raise ValueError("position value should only have the x axis [0] and the y axis [1]")
        self.__font_size: float = font_size
        self.__position: List[float] = position
        self.__color: Union[List[int], str] = color
        self.__content: str = content
        self.__anti_alising: bool = anti_alising

        self.__text_surface: Surface | None = None
        self.__update_text_surface()

    def __update_text_surface(self):
        text_font = font.Font(self.__font, int(self.__font_size))
        self.__text_surface = text_font.render(self.__content, self.__anti_alising, self.__color)

    def get_font(self) -> font.Font | None:
        return self.__font

    def set_font(self, new_font: font.Font | None):
        self.__font = new_font
        self.__update_text_surface()

    def get_font_size(self) -> float:
        return self.__font_size

    def set_font_size(self, new_font_size: float):
        if new_font_size <= 0:
            raise ValueError("font_size should be higher than 0")
        self.__font_size = new_font_size
        self.__update_text_surface()

    def get_position(self) -> List[float]:
        return self.__position

    def set_position(self, new_position: List[float]):
        if len(new_position) != 2:
            raise ValueError("position value should only have the x axis [0] and the y axis [1]")
        self.__position = new_position

    def get_color(self) -> Union[List[int], str]:
        return self.__color

    def set_color(self, new_color: Union[List[int], str]):
        self.__color = new_color
        self.__update_text_surface()

    def get_content(self) -> str:
        return self.__content

    def set_content(self, new_content: str):
        self.__content = new_content
        self.__update_text_surface()

    def get_anti_alising(self) -> bool:
        return self.__anti_alising

    def set_anti_alising(self, new_anti_alising: bool):
        self.__anti_alising = new_anti_alising
        self.__update_text_surface()

    def get_text_surface(self) -> Surface | None:
        return self.__text_surface
