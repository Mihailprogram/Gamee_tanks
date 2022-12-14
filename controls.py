import pygame,sys
from bul import Bullet
from ino import Ino
import time
def events(screen,gun,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                gun.mright=True
            elif event.key==pygame.K_a:
                gun.mleft=True
            elif event.key==pygame.K_SPACE:
                new_bullet=Bullet(screen,gun)
                bullets.add(new_bullet)
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_d:
                gun.mright=False
            elif event.key==pygame.K_a:
                gun.mleft=False
def update(bg_color,screen,stuts,scc,gun,inos,bullets):
    screen.fill(bg_color)
    scc.show()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()
def update_bullets(screen,inos,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    collis=pygame.sprite.groupcollide(bullets,inos,True,True)
    if len(inos)==0:
        bullets.empty()
        create_army(screen,inos)


def gun_kill(stuts,screen,gun,inos,bullets):
    if stuts.guns_left>0:
        stuts.guns_left-=1
        inos.empty()
        bullets.empty()
        create_army(screen,inos)
        gun.creat_gun()
        time.sleep(1)
    else:
        stuts.run_game=False
        sys.exit()
def inos_check(stuts,screen,gun,inos,bullets):
    screen_rect=screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom>=screen_rect.bottom:
            gun_kill(stuts,screen,gun,inos,bullets)
            break



def up_dad(stuts,screen,gun,inos,bullets):
    inos.update()
    if pygame.sprite.spritecollideany(gun,inos):
        gun_kill(stuts,screen,gun,inos,bullets)
    inos_check(stuts, screen, gun, inos, bullets)


def create_army(screen,inos):
    ino=Ino(screen)
    ino_width=ino.rect.width
    number_ino_x=int((600-2*ino_width)/ino_width)
    ino_h=ino.rect.height
    number_ino_y=int((600-100-2*ino_h)/ino_h)
    for row_n in range(number_ino_y):
        for ino_number in range(number_ino_x):
            ino=Ino(screen)
            ino.x=ino_width+(ino_width*ino_number)
            ino.y=ino_h+(ino_h*row_n)
            ino.rect.y=ino.rect.height+(ino.rect.height*row_n)
            ino.rect.x=ino.x
            inos.add(ino)