
while 1:
        import pygame , sys ,random 
        from pygame.locals import *
        pygame.init()

        #ctes
        a=0
        inc=dec=20
        red_inc=10
        ballsize=(65,65)
        redsize=(70,70)
        x,y=335,530
        screensize = (800,600)
        y1=-50
        y2=-random.randint(50,500)
        x2=random.randint(0,750)
        x1=random.randint(0,750)
        x3=random.randint(0,750)
        x4=random.randint(0,750)
        y3=-random.randint(50,500)
        y4=-random.randint(50,500)
        x5=random.randint(0,750)
        x6=random.randint(0,750)
        y5=-random.randint(50,500)
        y6=-random.randint(50,500)
        s=0
        xs=ys=0
        screen = pygame.display.set_mode(screensize)

        #colors
        black = (0,0,0)
        white = (255,255,255)


        gameclock=pygame.time.Clock()

        #the ball
        ball = pygame.image.load('ball.png')
        ball=pygame.transform.scale(ball,ballsize)

        #red
        red = pygame.image.load('red.png')
        red= pygame.transform.scale(red,redsize)



        gameover = pygame.image.load('./game over.jpg')
        begining=1
        while begining :
                        gameclock.tick(30)
                        for event in pygame.event.get():
                                        if event.type == QUIT :
                                                        pygame.quit()
                                                        sys.exit()
                                        if event.type == KEYDOWN  :
                                                         if event.key == K_RETURN:
                                                                                 begining = 0
                                                         if event.key == K_ESCAPE:
                                                                                 pygame.quit()
                                                                                 sys.exit()
                        pygame.display.flip()
                        screen.fill(black)
                        font=pygame.font.SysFont('font',50)
                        begin=font.render("Hit ENTER To Begin" ,True,white)
                        exite=font.render("Hit ESCAPE To Exit" , True , white)
                        screen.blit(begin,(60,60))                        
                        screen.blit(exite,(300,300))                        
                        



        #main loop
        s = 0
        l = 0
        playing=1
        while playing:
                        gameclock.tick(30)
                        for event in pygame.event.get():
                                        if event.type == QUIT:
                                                        pygame.quit()
                                                        sys.exit()
                                        if event.type == KEYDOWN or event.type == KEYUP:
                                                        if event.key == K_RIGHT:
                                                                        x += inc
                                                        if event.key == K_LEFT:
                                                                        x -= dec
                        font = pygame.font.SysFont('font', 50)
                        score = font.render("SCORE  : " + str(s), True, white)
                        level = font.render("LEVEL  : " + str(l) , True , white)
                        screen.blit(score, (xs, ys))
                        screen.blit(level,(600,0))
                        screen.blit(red, (x2, y2))
                        screen.blit(red, (x1, y1))
                        screen.blit(red, (x3, y3))
                        screen.blit(red, (x4, y4))
                        screen.blit(red, (x5, y5))
                        screen.blit(red, (x6, y6))
                        y1 += red_inc
                        y2 += red_inc
                        y3 += red_inc
                        y4 += red_inc
                        y5 += red_inc
                        y6 += red_inc

                        
                        if y1 > 625:
                                        y1 = -random.randint(50, 2000)
                                        x1 = random.randint(0, 750)
                                        s += 1
                        if y2 > 625:
                                        y2 = -random.randint(50, 2000)
                                        x2 = random.randint(0, 750)
                                        s += 1
                        if y3 > 625:
                                        y3 = -random.randint(50, 2000)
                                        x3 = random.randint(0, 750)
                                        s += 1
                        if y4 > 625:
                                        y4 = -random.randint(50, 2000)
                                        x4 = random.randint(x - 100, x + 170)
                                        s += 1
                        if y5 > 625:
                                        y5 = -random.randint(50, 2000)
                                        x5 = random.randint(x - 100, x + 170)
                                        s += 1
                        if y6 > 625:
                                        y6 = -random.randint(50, 2000)
                                        x6 = random.randint(x - 100, x + 170)
                                        s += 1
                        
                        if s>10 :
                                red_inc =15
                                l=1
                        if s>50 :
                                red_inc =20
                                inc=dec=25
                                l=2
                        if s>100 :
                                red_inc =22
                                inc=dec=30
                                l=3
                        
                        if s>300 :
                                red_inc =25
                                inc=dec=35
                                l=4

                        if s>500 :
                                red_inc = 30
                                inc=dec=40
                                l=5
                        
                        if (x1 <= x + 60 and x1 >= x - 60 and y1 >= y - 60) or (x2 <= x + 60 and x2 >= x - 60 and y2 >= y - 60) or (
                                                                        x3 <= x + 60 and x3 >= x - 60 and y3 >= y - 60) or (
                                                                        x4 <= x + 60 and x4 >= x - 60 and y4 >= y - 60) or (
                                                                        x5 <= x + 60 and x5 >= x - 60 and y5 >= y - 60) or (
                                                                        x6 <= x + 60 and x6 >= x - 60 and y6 >= y - 60):

                                        red_inc = inc = dec = 0
                                        a+=5
                                        


                        if a>200 : playing = 0
                        pygame.display.flip()
                        screen.fill(black)
                        screen.blit(ball, (x, y))

                        if x < 0:
                                        x = 0
                        if x > 800 - ballsize[0]:
                                        x = 800 - ballsize[0]
        ending = 1
        while ending :
                        gameclock.tick(30)
                        for event in pygame.event.get():
                                        if event.type == QUIT :
                                                        pygame.quit()
                                                        sys.exit()
                                        if event.type == KEYDOWN  :
                                                         if event.key == K_RETURN:
                                                                                 ending = 0
                                                         if event.key == K_ESCAPE:
                                                                                 pygame.quit()
                                                                                 sys.exit()
                        pygame.display.flip()
                        screen.fill(black)
                        font=pygame.font.SysFont('font',50)

                        begin=font.render("Hit ENTER To replay" ,True,white)
                        exite=font.render("Hit ESCAPE To Exit" , True , white)
                        screen.blit(begin,(60,60))                        
                        screen.blit(exite,(350,450)) 
                        screen.blit(gameover, (264, 220))

                        xs = 280
                        ys = 180
                        screen.blit(score, (xs, ys))



