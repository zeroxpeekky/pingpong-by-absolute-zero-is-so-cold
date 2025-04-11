from pygame import *
back = (0,255,255)
window = display.set_mode((700,500))
display.set_caption('pingpong')
zadniyfon = transform.scale(image.load("background.jpg"),(700,500))
clock = time.Clock()

x1 = 50
y1 = 100
x2 = 50
y2 = 100
x3 = 25
y3 = 25
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys [K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys [K_s] and self.rect.y > 10:
            self.rect.y -= self.speed
class Ball(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 650:
            if self.rect.y < 0:
                self.rect.y += 3
        if self.rect.x > 200:
            if self.rect.x < 0:
                self.rect.x +=3





playerone = Player1('rocket.png', 0 , 50, 60,65,10)
playertwo = Player2('rocket.png', 650 , 50, 60,65,10)
ball = Ball('ball.png',25,25,50,50,5)


finish = False
game = True
while game:
    
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(zadniyfon,(0,0))
        playerone.update()
        playertwo.update()
        ball.update()
        playerone.reset()
        playertwo.reset()
        ball.reset()


    clock.tick(40)
    display.update()
        
