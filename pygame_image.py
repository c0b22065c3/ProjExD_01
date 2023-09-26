import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    rotated_bg_img = pg.transform.flip(bg_img, True, False)

    kokaton_img = pg.image.load("ex01/fig/3.png")
    flipped_kokaton_img = pg.transform.flip(kokaton_img, True, False)
    # rotated_kokaton_img = pg.transform.rotozoom(flipped_kokaton_img, 10, 1.0)
    angle = 11 # 指定したい角度 + 1°
    kokatons_list = list(pg.transform.rotozoom(flipped_kokaton_img, i, 1.0) \
                         for i in range(angle))

    tmr = 0
    bg_x = 0
    bg_x_2 = 1600
    ret = False
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        if bg_x <= -1600:
            bg_x = 1600
        if bg_x_2 <= -1600:
            bg_x_2 = 1600

        screen.blit(bg_img, [bg_x, 0])
        screen.blit(rotated_bg_img, [bg_x_2, 0])

        if ret:
            flap = -1 * (tmr % angle + 1)
        else:
            flap = (tmr % angle)

        screen.blit(kokatons_list[flap], [300, 200])

        if flap == angle - 1:
            ret = True
        elif flap == -angle:
            ret = False

        pg.display.update()
        tmr += 1        
        bg_x -= 1
        bg_x_2 -= 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()