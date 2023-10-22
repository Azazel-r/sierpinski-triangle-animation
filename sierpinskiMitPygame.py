# Autor: René Richter
# Datum: 08.07.2022
# Zweck: Sierpinski mit pygame mal schauen lolllololol

import pygame
import math
import time
from random import randint

pygame.init()

FPS_COUNTER = True # ggf. ändern!! falls bock

win = pygame.display.set_mode((600,400))
# win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
farbL = [randint(0,255) for i in range(3)]
faktorL = [1,1,1]
clock = pygame.time.Clock()


def dreieck(sp, l):
    #breaktime = 0
    pos = [[0,0],[l,0],[l//2, - math.sqrt(l**2 - (l//2)**2)]]
    for i in range(len(pos)):
        pos[i][0] += sp[0]
        pos[i][1] += sp[1]
    #for i in range(-1,2):
        #pygame.draw.line(win, (0,0,255), pos[i], pos[i+1])
    #for e in pos:
        #if not 0 <= e[0] <= 1920 or not 0 <= e[1] <= 1080:
            #breaktime += 1
    #if not breaktime >= 3:   
    pygame.draw.polygon(win, (farbL[0], farbL[1], farbL[2]), pos, width=2)

def dreieck2(sp, l):
    #breaktime = 0
    höhe = math.sqrt(l**2 - (l//2)**2)
    pos = [[-3*l/4, höhe/2],
           [-l/4, - höhe/2],
           [l/4, höhe/2]]
    for i in range(len(pos)):
        pos[i][0] += sp[0]
        pos[i][1] += sp[1]
    #for e in pos:
        #if not 0 <= e[0] <= 1920 or not 0 <= e[1] <= 1080:
            #breaktime += 1
    #if not breaktime >= 3:   
    pygame.draw.polygon(win, (farbL[0], farbL[1], farbL[2]), pos, width=2)
        
def sierpinski(sp0, l):
    
    if l <= 20:
        return

    dreieck(sp0, l)

    sierpinski(sp0, l//2)
    sp1 = [sp0[0]+l//4, sp0[1]-math.sqrt((l//2)**2-(l//4)**2)]
    sierpinski(sp1, l//2)
    sp2 = [sp0[0]+l//2, sp0[1]]
    sierpinski(sp2, l//2)

def ändereFarben():
    for j in range(len(farbL)):
        if randint(0,60) == 22:
            faktorL[j] *= -1
        farbL[j] += faktorL[j] * randint(1,3)
        if farbL[j] > 205:
            farbL[j] = 205
            faktorL[j] = -1
        elif farbL[j] < 0:
            farbL[j] = 0
            faktorL[j] = 1
            



#------------------------------

aktiv = True
länge = 100
i = 0
#schriftart = pygame.font.Font("C:\\Users\\lolsc\\Desktop\\tetris\\assets\\PetMe64.ttf", 20)
schriftart = pygame.font.SysFont("impact", 20)
while aktiv:

    if i == 0:
        startzeit = time.perf_counter()
    
    events = pygame.event.get()

    ändereFarben()
    win.fill((farbL[0]+50, farbL[1]+50, farbL[2]+50))

    sierpinski((50,300), länge)
    
    länge += 10
    if länge > 1200:
        länge = 600
    
    for event in events:
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            aktiv = False
    i += 1
    if i >= 60:
        i = 0

    if FPS_COUNTER:
        endzeit = time.perf_counter() - startzeit
        schrift = schriftart.render(f"{int(i//endzeit)}", False, (0,0,0))
        win.blit(schrift, (50,50))
    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
pygame.quit()
