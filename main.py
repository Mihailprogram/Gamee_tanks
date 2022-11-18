import pygame,controls

from gun import Gun
from pygame.sprite import Group
from stuts import Sats
from sc import Scores
def run():
    pygame.init()
    screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption("Программа")
    bg_color=(0,0,0)
    gun=Gun(screen)
    bullets=Group()
    inos=Group()
    controls.create_army(screen,inos)
    stuts=Sats()
    scc=Scores(screen,stuts)
    while True:
        controls.events(screen,gun,bullets)
        if stuts.run_game:

            gun.update_gun()
            controls.update(bg_color,screen,stuts,scc,gun,inos,bullets)
            controls.update_bullets(screen,inos,bullets)
            controls.up_dad(stuts,screen,gun,inos,bullets)
run()