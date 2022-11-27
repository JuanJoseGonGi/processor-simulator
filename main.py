import pygame as pg


def main():
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Computer")
    pgClock = pg.time.Clock()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((0, 0, 0))
        # if Computer.clock.timer <= 0 launch computer.update()
        # Computer draw

        pg.display.flip()
        pgClock.tick(60)

    pg.quit()


if __name__ == "__main__":
    main()
