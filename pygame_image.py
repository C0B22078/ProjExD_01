import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_imgrv = pg.transform.flip(bg_img,True,False) 
    tori_img = pg.image.load("fig/3.png")
    tori_img = pg.transform.flip(tori_img,True,False)#２番
    rotate_img = pg.transform.rotozoom(tori_img,10,1.0)
    rotate2_img = pg.transform.rotozoom(tori_img,15,1.0)
    rotate0_img = pg.transform.rotozoom(tori_img,355,1.0)
    img_lst=[tori_img,rotate_img,rotate2_img,rotate_img,tori_img,rotate0_img]
    tmr = 0
    x = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_imgrv, [1600 - x, 0])
        screen.blit(bg_img, [3200 - x, 0])
        screen.blit(img_lst[tmr%3],[300,200])
        pg.display.update()
        tmr += 4 
        x = tmr % 3200
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()