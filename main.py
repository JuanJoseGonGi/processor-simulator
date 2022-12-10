import pygame as pg
import constants

import models.computer as computer
from models.ui.ui import UI


def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Computer")
    clock = pg.time.Clock()
    pg.time.set_timer(constants.COMPUTER_CLK, 1000)

    comp = computer.Computer()
    user_interface = UI(screen)

    running = True
    while running:
        pygame_events = pg.event.get()
        pressed_keys = pg.key.get_pressed()
        mouse_x, mouse_y = pg.mouse.get_pos()
        mouse_pressed = pg.mouse.get_pressed()

        for event in pygame_events:
            if event.type == pg.QUIT:
                running = False

            if event.type == constants.COMPUTER_CLK:
                comp.update()

            user_interface.onevent(event, mouse_x, mouse_y, mouse_pressed)

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
