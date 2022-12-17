import pygame as pg

import constants

from models.record import Record


class ALU:
    def __init__(self, parent_rect: pg.rect.Rect) -> None:
        self.x = constants.ALU_X
        self.y = constants.ALU_Y
        self.width = constants.ALU_WIDTH
        self.height = constants.ALU_HEIGHT
        self.rect = pg.Rect(
            self.x + parent_rect.x, self.y + parent_rect.y, self.width, self.height
        )

        self.input_a = Record(
            0.45 * self.rect.width - constants.ALU_INPUT_WIDTH,
            constants.ALU_INPUT_Y,
            constants.ALU_INPUT_WIDTH,
            constants.ALU_INPUT_HEIGHT,
            self.rect,
        )

        self.input_a.name = "A"

        self.input_b = Record(
            self.rect.width * 0.55,
            constants.ALU_INPUT_Y,
            constants.ALU_INPUT_WIDTH,
            constants.ALU_INPUT_HEIGHT,
            self.rect,
        )

        self.input_b.name = "B"

        self.output = Record(
            self.rect.width / 2 - constants.ALU_INPUT_WIDTH / 2,
            constants.ALU_OUTPUT_Y,
            constants.ALU_INPUT_WIDTH,
            constants.ALU_INPUT_HEIGHT,
            self.rect,
        )

        self.output.name = "OUT"

    def draw(self, screen: pg.Surface) -> None:
        points = [
            (self.rect.x, self.rect.y),
            (self.rect.x + self.rect.width * 0.4, self.rect.y),
            (self.rect.x + self.rect.width * 0.5, self.rect.y + self.rect.height * 0.5),
            (self.rect.x + self.rect.width * 0.6, self.rect.y),
            (self.rect.x + self.rect.width, self.rect.y),
            (self.rect.x + self.rect.width * 0.75, self.rect.y + self.rect.height),
            (self.rect.x + self.rect.width * 0.25, self.rect.y + self.rect.height),
        ]

        pg.draw.polygon(screen, constants.BLUE, points)

        self.input_a.draw(screen)
        self.input_b.draw(screen)
        self.output.draw(screen)
