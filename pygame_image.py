import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    #screen2 = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tori_img = pg.image.load("fig/3.png")
    tori_img = pg.transform.flip(tori_img,True,False)#２番
    rotate_img = pg.transform.rotozoom(tori_img,10,1.0)
    img_lst=[tori_img,rotate_img]
    tmr = 0
    x = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600 - x, 0])
        screen.blit(img_lst[tmr%2],[300,200])
        pg.display.update()
        tmr += 1 
        x = tmr % 1600
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()