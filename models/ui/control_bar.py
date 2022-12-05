from models.ui.button import Button

CONTROL_BAR_HEIGHT = 20
CONTROL_BAR_X = 0


class ControlBar:
    def __init__(self, screen) -> None:
        self.height = CONTROL_BAR_HEIGHT
        self.width = screen.get_width()
        self.x = CONTROL_BAR_X
        self.y = screen.get_height() - self.height

        self.screen = screen

        self.show_editor_button = Button(self.x + 2, self.y - 2, 10, 10, "👀 editor")

    def draw(self) -> None:
        self.screen.fill((0, 0, 0), (self.x, self.y, self.width, self.height))

        self.show_editor_button.draw(self.screen)
