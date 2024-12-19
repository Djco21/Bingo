import pygame
import source
class Ball(object):
    def __init__(self, number, ischosen, posx, posy):
        self.number = (number,)
        self.ischosen = ischosen
        self.x = posx
        self.y = posy
        self.textsurface = source.font.render(str(number),1,(255,255,255))
        self.textsurface_center = self.textsurface.get_rect(centerx=self.x+(45),centery=self.y+(42))
        if self.ischosen:
            self.image = source.green_ball_img
        else:
            self.image = source.gray_ball_img

    def __str__(self):
        return f'A bola de número {self.number} está {self.ischosen}'
    
    def get_number(self):
        c_number = int(''.join(map(str, self.number)))
        return c_number
        
    def change_status(self, status, img):
        self.ischosen = status
        self.image = img
        if status:
            img = source.green_ball_img
            return
    
    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))
        screen.blit(self.textsurface,(self.textsurface_center))

class Button(object):
    def __init__(self, text, posx, posy):
        self.x = posx
        self.y = posy
        self.image = source.button
        self.textsurface = source.font.render(str(text),1,(255,255,255))
        self.textsurface_center = self.textsurface.get_rect(centerx=self.x+200,centery=self.y+50)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.textsurface, (self.textsurface_center))