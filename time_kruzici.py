import pygame as pg
import time as timer
import random
import math as m

pg.font.init()

vbirdx=1
vbird=1
t=0.01
g=0.5
birdw=302
birdy=100
birdx=600

r=15
comic=pg.font.SysFont("Comic Sans MS",30)
running1=True
running2=False
running3=False
running_easter=False
score=0
boja=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
WIDTH=1366
HEIGHT=768
zelena=(0,255,0)
zelenikrugc=[random.randint(0,WIDTH),random.randint(100+r,HEIGHT-r)]
pg.display.set_caption("aim teszt")
screen=pg.display.set_mode((WIDTH,HEIGHT))
satic=pg.time.Clock()
screen.fill(boja)
krugcentar=(random.randint(0,WIDTH),random.randint(100+r,HEIGHT-r))
mis=pg.mouse.get_pressed()
posx=mis[0]
posy=mis[1]
c=0
pos=0
time=5
povrs_score=comic.render("score:"+" "+str(score),True,(255,255,255))
povrs_vreme=comic.render("time"+" "+str(time),True,(255,255,255))
brojkrugova=5
frame=0
interval1=-2
interval2=2

lista2=list()



def draw():
    screen.fill((0,0,0))

def beli_krugovi(broj_krugova,r):
    for i in range(broj_krugova):
        boja=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        centar=(random.randint(100+r,WIDTH-r),random.randint(100+r,HEIGHT-r))
        pg.draw.circle(screen,(boja),centar,r)
def hipotenuza(x1,y1,x2,y2):
    x=abs(x1-x2)
    y=abs(y1-y2)
    c=m.sqrt(x*x+y*y)
    return c
def pomeraj(centarx,centary,interval1,interval2):
    centarx=random.randint(interval1,interval2)
    centary=random.randint(interval1,interval2)
    return centarx,centary

bezanjex=random.randint(-1,1)
bezanjey=random.randint(-1,1)

draw()
beli_krugovi(brojkrugova,r)
screen.blit(povrs_vreme,(WIDTH-WIDTH/8,50))
pg.draw.circle(screen,((255,255,255)),zelenikrugc,r)

while running1:
    boja=(random.randint(0,170),random.randint(0,170),random.randint(0,170))
    pg.draw.circle(screen,((255,255,255)),zelenikrugc,r)    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running1=False
            running2=False
            running3=False
        elif event.type==pg.MOUSEBUTTONUP:
            if event.button==1:
                pos=pg.mouse.get_pos()
                c=hipotenuza(pos[0],pos[1],zelenikrugc[0],zelenikrugc[1])
                if c<=r:
                    brojkrugova+=1
                    zelenikrugc=[random.randint(r,WIDTH-r),random.randint(100+r,HEIGHT-r)]
                    draw()
                    beli_krugovi(brojkrugova,r,)
                    pg.draw.circle(screen,((255,255,255)),zelenikrugc,r)
                    score+=1
                    time=5
    povrs_score=comic.render("score:"+" "+str(score),True,(255,255,255))
    povrs_vreme=comic.render("time"+" "+str(time),True,(255,255,255))
    screen.fill(pg.Color("black"), (100,0,WIDTH,100))
    screen.blit(povrs_score,(WIDTH/8,50))
    screen.blit(povrs_vreme,(WIDTH-WIDTH/8,50))
    satic.tick(60)
    frame+=1
    if frame==60:
        chance=random.randint(1,1000)
        if chance==745:
            running1=False
            running2=False
            running3=False
            running_easter=True
        screen.fill(pg.Color((0,0,0)), (100,0,WIDTH,100))
        time-=1
        frame=0
        screen.blit(povrs_vreme,(WIDTH-WIDTH/8,50))
    if time==0:
        draw()
        screen.blit(povrs_score,(WIDTH/2-50,HEIGHT/2-30))
        pg.display.update()
        timer.sleep(2)
        running1=False
        running2=False
        Running3=False
    if score==50:
        running1=False
        running2=True
    pg.display.update()
while running2:
        if score>=70:
            r=25
        time=30
        draw()
        pg.draw.circle(screen,((255,255,255)),zelenikrugc,r)
        pomeraja,pomerajb=pomeraj(zelenikrugc[0],zelenikrugc[1],interval1,interval2)    
        for event in pg.event.get():
            if event.type==pg.QUIT:
                running1=False
                running2=False
                running3=False
            elif event.type==pg.MOUSEBUTTONUP:
                if event.button==1:
                    pos=pg.mouse.get_pos()
                    c=hipotenuza(pos[0],pos[1],zelenikrugc[0],zelenikrugc[1])
                    if c<=r:
                        interval1-=1
                        interval2+=1
                        zelenikrugc=[random.randint(r,WIDTH-r),random.randint(100+r,HEIGHT-r)]
                        draw()
                        pg.draw.circle(screen,((255,255,255)),((zelenikrugc[0]+pomeraja)%WIDTH,(zelenikrugc[1]+pomerajb)%HEIGHT),r)
                        score+=1
                        time=30
        povrs_score=comic.render("score:"+" "+str(score),True,(255,255,255))
        povrs_vreme=comic.render("time"+" infinite",True,(255,255,255))
        screen.fill(pg.Color("black"), (100,0,WIDTH,100))
        screen.blit(povrs_score,(WIDTH/8,50))
        screen.blit(povrs_vreme,(WIDTH-WIDTH/8,50))
        satic.tick(60)
        frame+=1
        if frame==60:
            chance=random.randint(1,100000)
            if chance==7519:
                running1=False
                running2=False
                running3=False
                running_easter=True
        if frame%10==0 and frame!=60:
            if zelenikrugc[0]-r<=0:
                pomeraja=2
            elif zelenikrugc[0]+r>=WIDTH:
                pomeraja=-2
            if zelenikrugc[1]-r<=100:
                pomerajb=2
            elif zelenikrugc[1]+r>=HEIGHT:
                pomerajb=-2
            else:  
                zelenikrugc[0]+=pomeraja
                zelenikrugc[1]+=pomerajb
        pg.display.update()
        if score==100:
            running3=True
            running2=False

while running_easter:
    bezanjex=random.randint(-1,1)
    bezanjey=random.randint(-1,1)
    time=30
    draw()
    pg.draw.circle(screen,((255,255,255)),zelenikrugc,r)
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running1=False
            running2=False
            running3=False
            running_easter=False
    pos=pg.mouse.get_pos()
    c=hipotenuza(pos[0],pos[1],zelenikrugc[0],zelenikrugc[1])
    if c<=r:
        if zelenikrugc[0]-r<=0:
            bezanjex=1
        elif zelenikrugc[0]+r>=WIDTH:
            bezanjex=-1
        if zelenikrugc[1]-r<=100:
            bezanjex=1
        elif zelenikrugc[1]+r>=HEIGHT:
            bezanjex=-1
        zelenikrugc[0]+=bezanjex*2*r
        zelenikrugc[1]+=bezanjey*2*r
    povrs_score=comic.render(". .- ... - . .-.",True,(255,255,255))
    povrs_vreme=comic.render(". --. --.",True,(255,255,255))
    screen.fill(pg.Color("black"), (100,0,WIDTH,100))
    screen.blit(povrs_score,(WIDTH/8,50))
    screen.blit(povrs_vreme,(WIDTH-WIDTH/8,50))
    satic.tick(60)
    frame+=1
    pg.display.update()
    
while running3:
    randomboja=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running1=False
            running2=False
            running3=False

    if birdy+birdw>=HEIGHT:
        birdv=5
        for i in range(7):
            birdy+=vbird+g
            vbird-=g
    if birdx<=0:
        vbird=3
        vbirdx=3
        for i in range(7):
            birdx+=vbirdx
            vbird-=g
            vbirdx-=g
    if birdx+birdw>=WIDTH:
        birdx=0
    if birdy<=0:
        vbird=3
        for i in range(7):
            birdy+=vbird
            vbird-=g
    else:
        birdy+=g+vbird
        birdx+=vbirdx
        vbird+=0.001
    
    pg.draw.rect(screen,(randomboja),(birdx,birdy,birdw,birdw))
    pg.display.update()



pg.quit