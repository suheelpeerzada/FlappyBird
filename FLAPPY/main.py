import pygame as p
from random import randint
from time import sleep

p.init()

w = 420
h = 650

sc = 0

screen = p.display.set_mode((w, h))
p.display.set_caption('Flappy Bird by 51, 46, 24')

back = p.image.load('FLAPPY\\assets\\flback.jpg').convert_alpha()
bird = p.image.load('FLAPPY\\assets\\flb1.png').convert_alpha()
bird1 = p.transform.rotate(bird, 25).convert_alpha()

score = p.font.Font('FLAPPY\\assets\\flappy-bird-font.ttf', 20)
jump_sound = p.mixer.Sound('FLAPPY\\assets\\sfx_wing.wav')
point = p.mixer.Sound('FLAPPY\\assets\\sfx_point.wav')
hit = p.mixer.Sound('FLAPPY\\assets\\sfx_hit.wav')


tunnel = p.image.load('FLAPPY\\assets\\tunnelbtm1.png').convert_alpha()
tunnelu = p.image.load('FLAPPY\\assets\\tunneltop1.png').convert_alpha()
name = p.image.load('FLAPPY\\assets\\flappybird.png').convert_alpha()
play = p.image.load('FLAPPY\\assets\\play.png').convert_alpha()

u_tunnel = randint(600, 700)
l_tunnel = randint(100, 200)

backrect = back.get_rect(bottomleft=(w+8,h))
bird_rect = bird.get_rect(center = (200,325))
tunnel_rect = tunnel.get_rect(midbottom = (randint(400, 600),680))
tunnelu_rect = tunnelu.get_rect(midbottom = (randint(750, 1000),130))

playrect = play.get_rect(center = (150, 250))
name_rect = name.get_rect(bottomleft = (60,0))
gravity = 0
gameover = True
speed = 4
tspeed = 2

m=n=sin=0

while True:
        score_dis = score.render(f'{(sc)}', False, 'white')
        score_rect = score_dis.get_rect(center = (20, 30))
        for event in p.event.get():
            if event.type == p.QUIT:
                exit()
            if not gameover:
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_SPACE:
                            gravity= -15
                            jump_sound.play()
            else:
                 if event.type == p.MOUSEBUTTONDOWN:
                        bird_rect.y = 200
                        gravity = 0
                        sc = 0
                        speed = 4
                        gameover = False
                        tunnel_rect.x = randint(400, 600)
                        tunnelu_rect.x = randint(750, 1000)
                        jump_sound.play()
                 if event.type == p.KEYDOWN:
                      if event.key == p.K_SPACE:
                        bird_rect.y = 200
                        gravity = 0
                        sc = 0
                        speed = 4
                        gameover = False
                        tunnel_rect.x = randint(400, 600)
                        tunnelu_rect.x = randint(750, 1000)
                        jump_sound.play()
        if not gameover:
            screen.blit(back, (0,0))
            screen.blit(bird1,bird_rect) 
            screen.blit(tunnel, tunnel_rect)
            screen.blit(tunnelu, tunnelu_rect)
            screen.blit(score_dis, (w/2, 20)) 
            tunnel_rect.x -= speed
            tunnelu_rect.x -= speed
            if sc >= 2:
                 match sin:
                      case 0:
                        tunnel_rect.y += tspeed
                        tunnelu_rect.y += tspeed
                        if tunnel_rect.y >= 500:
                             sin = 1
                      case 1:
                            tunnel_rect.y -= tspeed
                            tunnelu_rect.y -= tspeed
                            if tunnel_rect.y <= 320:
                              sin = 0
            if bird_rect.y<470:
                gravity+=1
                bird_rect.y+=gravity
            if bird_rect.y >= 470 :
                 bird_rect.y -= 1
                 hit.play()
                 sleep(.5)
                 gameover = True
            if tunnel_rect.x <= -110:
                tunnel_rect.x = randint(750, 1000)
            if tunnelu_rect.x <= -110:
                tunnelu_rect.x = randint(400, 600)
            if tunnel_rect.collidepoint(bird_rect.center) or tunnelu_rect.collidepoint(bird_rect.center):
                hit.play()
                sleep(.5)
                gameover = True
            if 147 < tunnel_rect.x < 154 or 147 < tunnelu_rect.x < 154: 
                sc += 1
                point.play()
                speed+= 0.3
                if sc >= 20:
                    tspeed+=0.3
        else:
            screen.blit(back, (0,0))
            screen.blit(name, name_rect)
            screen.blit(bird1, bird_rect)
            screen.blit(play, (150, 410))

            match m:
                 case 0:
                      bird_rect.y-= 3
                      if bird_rect.y <= 200:
                        m = 1
                 case 1:
                      bird_rect.y+= 3
                      if bird_rect.y >= 250:
                           m=0

            match n:
                 case 0:
                      name_rect.y-= 1
                      if name_rect.y <= 40:
                        n = 1
                 case 1:
                      name_rect.y+= 1
                      if name_rect.y >= 80:
                           n=0
        p.display.update()
        p.time.Clock().tick(60)