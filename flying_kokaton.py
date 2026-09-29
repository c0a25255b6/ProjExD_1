import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)#練習８：左右反転した背景画像Suface
    kk_img = pg.image.load("fig/3.png")#練習３：こうかとん画像Sufaceの作成
    kk_img = pg.transform.flip(kk_img,True,False)#練習３：こうかとん左右反転
    kk_rct = kk_img.get_rect()#練習１０－１：こうかとんRectの取得
    kk_rct.center = 300,200#練習１０－２：こうかとん初期座標
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        a = -1
        b = 0
        key_lst = pg.key.get_pressed()#練習１０－３：キーの押下状態取得
        if key_lst[pg.K_UP]:
            b -= 1
        if key_lst[pg.K_DOWN]:
            b += 1
        if key_lst[pg.K_LEFT]:
            a -= 1
        if key_lst[pg.K_RIGHT]:
            a += 2
        kk_rct.move_ip(a,b)

        x = tmr%3200#練習９：ループさせる
        screen.blit(bg_img, [-x, 0])#練習５：背景画像を右から左に
        screen.blit(bg_img2,[-x+1600,0])#練習７：2枚目の背景画像
        screen.blit(bg_img,[-x+3200,0])#練習９：３枚目の背景画像
        screen.blit(kk_img,kk_rct)#練習４：こうかとん画像Sufaceを貼り付け
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習６：FPS変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()