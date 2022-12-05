import pygame as pg


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

        self.default_color = (255, 255, 255)
        self.click_color = (200, 200, 200)
        self.hover_color = (150, 150, 150)
        self.color = self.default_color

        self.text = text

    def set_color(self, color: tuple[int, int, int]) -> None:
        self.color = color

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, self.color, self.rect)
        pg.draw.rect(screen, (0, 0, 0), self.rect, 2)

        btn_font = pg.font.SysFont("Arial", 20)
        btn_text = btn_font.render(self.text, True, (0, 0, 0))
        text_rect = btn_text.get_rect()
        text_rect.center = self.rect.center
        screen.blit(btn_text, text_rect)
