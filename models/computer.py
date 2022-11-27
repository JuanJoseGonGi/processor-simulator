import pygame as pg


class Computer:
    def __init__(self) -> None:
        pass

    def update(self):
        print("Executing")

    def draw(self, screen: pg.Surface):
        # Draw a box to represent the computer
        pg.draw.rect(screen, (255, 255, 255), (100, 100, 300, 300))
