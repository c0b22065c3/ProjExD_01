import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kokaton_img = pg.image.load("ex01/fig/3.png")
    flipped_kokaton_img = pg.transform.flip(kokaton_img, True, False)
    rotated_kokaton_img = pg.transform.rotozoom(flipped_kokaton_img, 10, 1.0)
    kokatons_list = [flipped_kokaton_img, rotated_kokaton_img]

    tmr = 0
    bg_x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        if bg_x <= -1600:
            bg_x = 0

        screen.blit(bg_img, [bg_x, 0])
        if bg_x <= -800:
            screen.blit(bg_img, [bg_x + 1600, 0])

        flap = tmr % 2
        screen.blit(kokatons_list[flap], [300, 200])
        pg.display.update()
        tmr += 1        
        bg_x -= 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()