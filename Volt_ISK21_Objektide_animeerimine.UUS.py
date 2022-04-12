import pygame                                                    #mooduli pygame importimine

pygame.init()                                                    #pygame käivitamine

screenX = 640                                                    #akna pikkus
screenY = 480                                                    #akna kõrgus
screen=pygame.display.set_mode([screenX,screenY])                #soovitud suurusega akna tekitamine, mis lisatakse muutujasse.
pygame.display.set_caption("Ülesanne 4")                         #aknale nimetuse andmine

bg = pygame.image.load("bg_rally.jpg")                           #pildi avamine ,muutuja omistab pildi.

punane = pygame.image.load("f1_red.png")                         #pildi avamine ,muutuja omistab pildi.
punane = pygame.transform.scale(punane, [50, 100])               #punase auto suuruse xy koordinaadid


fps = pygame.time.Clock()                                        #mängu ajaga (liikumine) sidumine

skoor = 0                                                        #muutuja väärtus 0

sinine = pygame.image.load("f1_blue.png")                         #pildi avamine ,muutuja omistab pildi.
sinine = pygame.transform.scale(sinine, [50, 100])                #transform abil pildi mõõtmed xy koordinaadtidega

sinine1 = pygame.transform.scale(sinine, [50, 100])               #muutuja sinine 1 väärtus pilt koos suurus xy koordinaatidega
sinine2 = pygame.transform.scale(sinine, [50, 100])               #muutuja sinine 2 väärtus pilt koos suurus xy koordinaatidega
sinine3 = pygame.transform.scale(sinine, [50, 100])               #muutuja sinine 3 väärtus pilt koos suurus xy koordinaatidega

font = pygame.font.Font(pygame.font.match_font('Daytona'), 35)    #fondi stiil, joone paksus väärtus muutujasse
text = font.render("Skoor: " + str(skoor), True, [255,180,0])     #muutuja mille väärtus tekst Skoor, värvus oranz

posX1, posY1 = 150, 100                                           #positsioon mille väärtus xy koordinaatidega
posX2, posY2 = 400, 200                                           #positsioon mille väärtus xy koordinaatidega
posX3, posY3 = 210, 100                                           #positsioon mille väärtus xy koordinaatidega


running = True                                #muutuja väärtus õige
while (running):                              #korduslause kui tõsi
    screen.blit(bg, [0, 0])                   #tausta joonistamine
    posY1 += 5                                #Y koordinaadi suurendamine auto 1 Y koordinaadi 5 võrra
    posY2 += 4                                #Y koordinaadi suurendamine auto 2 Y koordinaadi 4 võrra
    posY3 += 4                                #Y koordinaadi suurendamine auto 3 Y koordinaadi 4 võrra

    screen.blit(punane, [295, 380])           #tausta uuesti joonistamine
    screen.blit(sinine1, [posX1, posY1])      #tausta uuesti joonistamine vastavalt asetusele
    screen.blit(sinine2, [posX2, posY2])      #tausta uuesti joonistamine vastavalt asetusele
    screen.blit(sinine3, [posX3, posY3])      #tausta uuesti joonistamine vastavalt asetusele
    screen.blit(text, [5, 20])
    text = font.render("Skoor: " + str(skoor), True, [255, 180, 0]) #muutuja mille väärtus tekst Skoor, värvus oranz
    if posY1 == 480:    #tingimusel kui Y koordinaat võrdne 480
        posY1 = 0       #muutuja väärtus 0
        skoor += 1      #skoori suurendamine iseenda väärtusele +1
    if posY2 == 480:    #tingimusel kui Y koordinaat võrdne 480
        posY2 = 0       #muutuja väärtus 0
        skoor += 1      #skoori suurendamine iseenda väärtusele +1
    if posY3 == 480:    #tingimusel kui Y koordinaat võrdne 480
        posY3 = 0       #muutuja väärtus 0
        skoor += 1      #skoori suurendamine iseenda väärtusele +1

    #Programmi sulgemine ristist
    for event in pygame.event.get():  #tsükli kasutamine event omistab väärtuse pygame meetodit kasutades
        if event.type == pygame.QUIT: #kui event tüübi väärtuseks sulgumine(pygame.QUIT)
            running = False           #väärtus vale, aken sulgub.

    pygame.display.flip()   #ekraani värskendamine
    fps.tick(40)            #40 kaadrit sekundis