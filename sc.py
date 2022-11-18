import pygame.font

class Scores():
    def __init__(self,screen,stuts):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.stuts=stuts
        self.text_color=(144,133,131)
        self.font=pygame.font.SysFont(None,33)
        self.image_score()
    def image_score(self):
        self.score_img=self.font.render(str(self.stuts.score),True,self.text_color,(0,0,0))
        self.screen_rect=self.score_img.get_rect()
        self.screen_rect.right=self.screen_rect.right-40
        self.screen_rect.top=20

    def show(self):
        self.screen.blit(self.score_img,self.screen_rect)