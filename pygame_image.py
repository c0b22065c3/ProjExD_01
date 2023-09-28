import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")

    width = 800
    height = 600
    screen = pg.display.set_mode((width, height))
    clock  = pg.time.Clock()

    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    rotated_bg_img = pg.transform.flip(bg_img, True, False)

    kokaton_img = pg.image.load("ex01/fig/3.png")
    flipped_kokaton_img = pg.transform.flip(kokaton_img, True, False)
    
    angle = 10
    angle_len = angle + 1
    kokatons_list = list(pg.transform.rotozoom(flipped_kokaton_img, i, 1.0) \
                         for i in range(angle_len))

    bg_width = 1600
    clock_tick = 100

    tmr = 0
    bg_x = 0
    bg_x_2 = bg_width
    ret = False
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        if bg_x <= -bg_width:
            bg_x = bg_width
        if bg_x_2 <= -bg_width:
            bg_x_2 = bg_width

        screen.blit(bg_img, [bg_x, 0])
        screen.blit(rotated_bg_img, [bg_x_2, 0])

        if ret:
            flap = -(tmr % angle_len + 1)
        else:
            flap = (tmr % angle_len)

        screen.blit(kokatons_list[flap], [300, 200])

        if flap == angle_len - 1:
            ret = True
        elif flap == -angle_len:
            ret = False

        pg.display.update()
        tmr += 1
        bg_x -= 1
        bg_x_2 -= 1
        clock.tick(clock_tick)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()