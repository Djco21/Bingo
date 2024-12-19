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
        
    def change_status(self, status):
        self.ischosen = status
        if status:
            img = source.green_ball_img
            self.image = img
        else:
            img = source.gray_ball_img
            self.image = img
            return
    
    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))
        screen.blit(self.textsurface,(self.textsurface_center))

class Curr_ball(object):
    def __init__(self, number, posx, posy):
        self.number = number
        self.x = posx
        self.y = posy
        self.image = source.red_ball_img
        self.image = pygame.transform.scale(source.red_ball_img,(300,300))
        self.textsurface = source.big_font.render(str(number),1,(255,255,255))
        self.textsurface_center = self.textsurface.get_rect(centerx=self.x+(105),centery=self.y+(150))

    def get_number(self):
        c_number = self.number
        return c_number
    
    def change_number(self, number):
        self.number = number
        self.textsurface = source.big_font.render(str(number),1,(255,255,255))
        return
    
    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))
        screen.blit(self.textsurface,(self.textsurface_center))

class Last_balls(object):
    def __init__(self, number, posx, posy):
        self.number = number
        self.x = posx
        self.y = posy
        self.image = source.green_ball_img
        self.textsurface = source.font.render(str(number),1,(255,255,255))
        self.textsurface_center = self.textsurface.get_rect(centerx=self.x+(30),centery=self.y+(42))

    def get_number(self):
        c_number = self.number
        return c_number
    
    def change_number(self, number):
        self.number = number
        self.textsurface = source.font.render(str(number),1,(255,255,255))
        return
    
    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))
        screen.blit(self.textsurface,(self.textsurface_center))

class Button(object):
    def __init__(self, text, posx, posy):
        self.x = posx
        self.y = posy
        self.image = source.button
        self.rect = self.image.get_rect(centerx=self.x+200,centery=self.y+50)
        self.textsurface = source.font.render(str(text),1,(255,255,255))
        self.textsurface_center = self.textsurface.get_rect(centerx=self.x+200,centery=self.y+50)

    def press_button(self):
        result = False

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            print('colidiu')
            if pygame.mouse.get_pressed()[0]:
                print('clicou')
                result = True
            if not pygame.mouse.get_pressed()[0] and result:
                result = False
                return True

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.textsurface, (self.textsurface_center))