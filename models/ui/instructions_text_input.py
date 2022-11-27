import pygame as pg
from pygame_texteditor import TextEditor

from typing import List, Sequence, Tuple

OFFSET_X = 50
OFFSET_Y = 50
TEXT_AREA_HEIGHT = 300
TEXT_AREA_WIDTH = 800


class InstructionsTextInput:
    def __init__(self, screen: pg.Surface) -> None:
        self.text_editor = TextEditor(
            OFFSET_X,
            OFFSET_Y,
            TEXT_AREA_WIDTH,
            TEXT_AREA_HEIGHT,
            screen,
            line_numbers_flag=True,
        )

    def draw(
        self,
        pygame_events: List[pg.event.Event],
        pressed_keys: Sequence[bool],
        mouse_x: int,
        mouse_y: int,
        mouse_pressed: Tuple[bool, bool, bool] | Tuple[bool, bool, bool, bool, bool],
    ) -> None:
        self.text_editor.display_editor(
            pygame_events, pressed_keys, mouse_x, mouse_y, mouse_pressed
        )

    def get_instructions(self) -> List[str]:
        return self.text_editor.get_text_as_list()
