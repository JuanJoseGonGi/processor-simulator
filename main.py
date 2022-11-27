import pygame as pg
import models.computer as computer

COMPUTER_CLK = pg.USEREVENT


def main():
    pg.init()
    screen = pg.display.set_mode((1000, 800))
    pg.display.set_caption("Computer")
    clock = pg.time.Clock()
    pg.time.set_timer(COMPUTER_CLK, 1000)

    comp = computer.Computer()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == COMPUTER_CLK:
                comp.update()

        screen.fill((0, 0, 0))

        comp.draw(screen)

        pg.display.flip()
        clock.tick(60)

    pg.quit()


if __name__ == "__main__":
    main()
