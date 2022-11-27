import pygame as pg
import models.computer as computer
from models.ui import ui


COMPUTER_CLK = pg.USEREVENT


def main():
    pg.init()
    screen = pg.display.set_mode((1000, 800))
    pg.display.set_caption("Computer")
    clock = pg.time.Clock()
    pg.time.set_timer(COMPUTER_CLK, 1000)

    comp = computer.Computer()
    user_interface = ui.UI(screen)

    running = True
    while running:
        pygame_events = pg.event.get()
        pressed_keys = pg.key.get_pressed()
        mouse_x, mouse_y = pg.mouse.get_pos()
        mouse_pressed = pg.mouse.get_pressed()

        for event in pygame_events:
            if event.type == pg.QUIT:
                running = False

            if event.type == COMPUTER_CLK:
                comp.update()

        screen.fill((0, 0, 0))

        comp.draw(screen)
        user_interface.draw(
            pygame_events, pressed_keys, mouse_x, mouse_y, mouse_pressed
        )

        pg.display.flip()
        clock.tick(60)

    pg.quit()


if __name__ == "__main__":
    main()
