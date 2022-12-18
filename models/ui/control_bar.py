import pygame as pg
import constants

from models.ui.button import Button
from typing import Tuple, Callable


class ControlBar:
    def __init__(self, screen) -> None:
        self.height = constants.CONTROL_BAR_HEIGHT
        self.width = screen.get_width()
        self.x = constants.CONTROL_BAR_X
        self.y = screen.get_height() - self.height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

        self.screen = screen

        self.show_editor_button = Button(
            self.x + 20,
            constants.CONTROL_BAR_BUTTON_Y + self.y,
            60,
            constants.CONTROL_BAR_BUTTON_HEIGHT,
            "Code",
        )

        self.toggle_show_editor = lambda: None

    def click(
        self,
        mouse_x: int,
        mouse_y: int,
        mouse_pressed: Tuple[bool, bool, bool] | Tuple[bool, bool, bool, bool, bool],
    ) -> None:
        if not mouse_pressed[0]:
            return

        if self.show_editor_button.rect.collidepoint(mouse_x, mouse_y):
            self.show_editor_button.click()

    def reset(self):
        self.show_editor_button.reset()

    def set_toggle_show_editor(self, toggle_show_editor: Callable[[], None]):
        self.toggle_show_editor = toggle_show_editor
        self.show_editor_button.set_onclick(self.toggle_show_editor)

    def draw(self) -> None:
        self.screen.fill(constants.BLUE, self.rect)
        self.show_editor_button.draw(self.screen)
