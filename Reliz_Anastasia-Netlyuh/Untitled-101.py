from pygame import *
from random import randint
#звук
mixer.init()
mixer.music.load("IMG_1928 (audio-extractor.net).mp3")
mixer.music.play()



#зображення
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, width, hight ):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def recet(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > win_width/2:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < win_width - 80:
              self.rect.x += self.speed  



class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x < win_width - 450:
            self.rect.x += self.speed    
 


class Friend(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global score1 
        global score2

        if self.rect.y > win_height-180:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

        
     

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global score1 

        if self.rect.y > win_height-180:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0

        


  

score1 = 0

score2 = 0

#ігрова сцена         
window = display.set_mode((800, 500))
win_width = 800
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Wolf Game")
background = transform.scale(image.load("photo_5222434216665537562_x.jpg"),(win_width, win_height))

font.init()
#font1 = font.Font(None, 80)
font2 = font.Font(None, 36)

#пишемо текст на екрані

    #спрайти
wolf1 = "wolf_2001.png"
wolf2= "wolf_2002.png"
game_fon = "photo_5222434216665537562_x.jpg"
egg = "egg.norm(1).png"
egg_bad = "bad_egg.png" 

eggs_good= sprite.Group()
for i in range(1, 6):
    egg = Friend("egg.norm(1).png", randint(1, 7),randint(20, win_width - 400), -35, 50, 60)
    eggs_good.add(egg)
    egg = Friend("egg.norm(1).png", randint(1, 7),randint(win_width - 400, win_width - 20), -35, 50, 60)
    eggs_good.add(egg)

eggs_bad= sprite.Group()
for i in range(1, 4):
    egg_bad = Enemy("bad_egg.png", randint(5, 7),randint(win_width - 400, win_width - 20), -35, 50, 60)
    eggs_bad.add(egg_bad)    
    egg_bad = Enemy("bad_egg.png", randint(5, 7),randint(20, win_width - 400), -35, 50, 60)
    eggs_bad.add(egg_bad)  



font.init()
font1 = font.SysFont('Calibri',36)
font2 = font.SysFont('Calibri',45)
font3 = font.SysFont('Calibri',80)
txt_lose_game = font2.render('You lose',True,(255,15,51))
txt_win_game = font2.render('You win',True,(50,205,50))




wolf1 = Player1("wolf_2001.png", 13, win_height - -40, 350, 140, 180)
wolf2 = Player2("wolf_2002.png", 13, win_height - 325, 350, 140, 180)

run = True
finish = False
while run:
    
    for e in event.get():
        if e.type == QUIT:
            run = False
    if e.type == KEYDOWN:
            if e.key == K_UP and finish == True:
                eggs_good= sprite.Group()
                for i in range(1, 6):
                    egg = Friend("egg.norm(1).png", randint(1, 7),randint(20, win_width - 400), -35, 50, 60)
                    eggs_good.add(egg)
                    egg = Friend("egg.norm(1).png", randint(1, 7),randint(win_width - 400, win_width - 20), -35, 50, 60)
                    eggs_good.add(egg)

                eggs_bad= sprite.Group()
                for i in range(1, 4):
                    egg_bad = Enemy("bad_egg.png", randint(5, 7),randint(win_width - 400, win_width - 20), -35, 50, 60)
                    eggs_bad.add(egg_bad)    
                    egg_bad = Enemy("bad_egg.png", randint(5, 7),randint(20, win_width - 400), -35, 50, 60)
                    eggs_bad.add(egg_bad)  

                finish = False
            elif e.key == K_DOWN and finish == False:
                finish= True
            elif e.key == K_DOWN and finish == True:
                finish= False


    if not finish:       
        text = font1.render("Рахунок:"+ str(score1), 1, (36, 36, 143)) 
        text1 = font1.render("Рахунок:"+ str(score2), 1, (36, 36, 143)) 
        window.blit(background, (0, 0))  
        window.blit(text1, (10, 15))
        window.blit(text, (645, 15))
        if sprite.spritecollide(wolf1, eggs_good,True):
            egg = Friend("egg.norm(1).png", randint(1, 7),randint(win_width - 400, win_width - 20), -35, 50, 60)
            eggs_good.add(egg)
            score1 += 1
            
        if sprite.spritecollide(wolf2, eggs_good, True):
            egg = Friend("egg.norm(1).png", randint(1, 7),randint(20, win_width - 400), -35, 50, 60)
            eggs_good.add(egg)
            score2 += 1
            
        if sprite.spritecollide(wolf1, eggs_bad, True):
            egg_bad = Enemy("bad_egg.png", randint(3, 7),randint(win_width - 400, win_width - 20), -35, 50, 60)
            eggs_bad.add(egg_bad)
            score1 -= 1
            
        if sprite.spritecollide(wolf2, eggs_bad, True):
            egg_bad = Enemy("bad_egg.png", randint(3, 7),randint( 20, win_width - 400), -35, 50, 60)
            eggs_bad.add(egg_bad)
            score2 -= 1    
            
        for egg in  eggs_good.sprites():
            if egg.rect.y > win_height:
                egg.rect.y = -35
        for egg_b in  eggs_bad.sprites():
            if egg_b.rect.y > win_height:
                egg_b.rect.y = -35
                
        if score2 == 4:
            window.blit(txt_win_game,(150,200))
            window.blit(txt_lose_game,(550,200))
            for egg_b in  eggs_bad.sprites():
                egg_b.kill()
            for egg_b in  eggs_good.sprites():
                egg_b.kill()
            score1 = 0
            score2 = 0

            finish=True
            
        if score1 == 4:
            window.blit(txt_lose_game,(150,200))
            window.blit(txt_win_game,(550,200))
            for egg_b in  eggs_bad.sprites():
                egg_b.kill()
            for egg_b in  eggs_good.sprites():
                egg_b.kill()
            score1 = 0
            score2 = 0
            finish=True
            
                


        wolf1.update()
        wolf1.update()
        wolf1.recet()

        wolf2.update()
        wolf2.update()
        wolf2.recet()
        eggs_bad.update()
        eggs_bad.draw(window)
        eggs_good.update()
        eggs_good.draw(window)


    display.update()
        
    time.delay(50)
