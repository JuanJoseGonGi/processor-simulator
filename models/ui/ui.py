import pygame as pg

from models.ui import instructions_text_input as iti, control_bar

from typing import List, Sequence, Tuple


class UI:
    def __init__(self, screen) -> None:
        self.editor = iti.InstructionsTextInput(screen)
        self.show_editor = False

        self.control_bar = control_bar.ControlBar()

    def draw(
        self,
        pygame_events: List[pg.event.Event],
        pressed_keys: Sequence[bool],
        mouse_x: int,
        mouse_y: int,
        mouse_pressed: Tuple[bool, bool, bool] | Tuple[bool, bool, bool, bool, bool],
    ) -> None:
        if self.show_editor:
            self.editor.draw(
                pygame_events, pressed_keys, mouse_x, mouse_y, mouse_pressed
            )
