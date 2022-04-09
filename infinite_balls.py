while 1:
    import pygame, sys
    from pygame.locals import *
    from random import randint
    from math import sqrt
    from math import *
    pygame.init()
# =================colors================
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
# =================cstes=================
    s = 0
    a = 0
    l = 0
    r = 5
    ball_speed = 20
    red_ball_speed = 12
    w = 700
    h = 766
    playing = 1
    scene1 = 1
    gameover = 1
# =================variables==============
    screen_size = (w, h)
    ball_size = (w // 12, w // 12)
    red_ball_X = [randint(0, w), randint(0, w), randint(0, w), randint(0, w), randint(0, w), randint(0, w),
                  randint(0, w), randint(0, w), randint(0, w), randint(0, w), randint(0, w), randint(0, w),
                  randint(0, w), randint(0, w), randint(0, w), randint(0, w), randint(0, w), randint(0, w),
                  randint(0, w), randint(0, w), randint(0, w)]
    red_ball_Y = [-randint(0, 2000), -randint(0, 2000), -randint(0, 2000), -randint(0, 2000), -randint(0, 2000),
                  -randint(0, 2000), -randint(0, 2000), -randint(0, 2000), -randint(0, 2000), -randint(0, 2000),
                  -randint(0, 2000), -randint(0, 2000), -randint(0, 2000), -randint(0, 2000), -randint(0, 2000),
                  -randint(0, 2000), -randint(0, 2000), -randint(0, 2000), -randint(0, 2000), -randint(0, 2000),
                  -randint(0, 2000)]
    x = (w / 2) - (ball_size[0] / 2)
    y = h - ball_size[0]
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("INFINITE BALLS")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('font', w // 20)
    font1 = pygame.font.SysFont('font1', w // 10)
    start = pygame.image.load("start.png")
    start = pygame.transform.scale(start, screen_size)
    end = pygame.image.load("end.png")
    end = pygame.transform.scale(end, screen_size)
    ball = pygame.image.load("ball.png")
    ball = pygame.transform.scale(ball, ball_size)
    red_ball = pygame.image.load("red.png")
    red_ball = pygame.transform.scale(red_ball, ball_size)
# ====//////////////////=====start loop=======\\\\\\\\\\\\\\\\\========
    while scene1:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    scene1 = 0
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.flip()
        screen.fill(black)
        screen.blit(start, (0, 0))
# ====////////////////====playling loop=======\\\\\\\\\\\\\\\========
    while playing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN or event.type == KEYUP:
                if event.key == K_RIGHT:
                    x += ball_speed
                if event.key == K_LEFT:
                    x -= ball_speed
        score = font.render('SCORE : ' + str(s), 1, white)
        level = font.render('LEVEL : ' + str(l), 1, white)
        screen.blit(score, (0, 0))
        pygame.display.flip()
        screen.fill(black)
        screen.blit(ball, (x, y))
        levelsize = level.get_size()
        screen.blit(level, (w - levelsize[0] - 10, 0))
#============= red ball for loop============
        for i in range(r):
            screen.blit(red_ball, (red_ball_X[i], red_ball_Y[i]))
            red_ball_Y[i] += red_ball_speed
#============ creations condition============
            if red_ball_Y[i] > h:
                s += 1
                red_ball_Y[i] = -randint(0, 2000)
                if x - 150 >= 0:
                    a = x - 150
                else:
                    a = 0
                red_ball_X[i] = randint(a, x + 150 + ball_size[0])
#============ death condition ===========
            if (sqrt(((red_ball_X[i] - x) ** 2) + ((red_ball_Y[i] - y) ** 2))) <= ball_size[0]:
                red_ball_speed = 0
                ball_speed = 0
                pygame.time.wait(400)
                playing=0
# ====white ball limit : stoping condition=====
        if x >= w - ball_size[0]:
            x = w - ball_size[0]
        if x <= 0:
            x = 0
# ====Level conditions ! =====
        if s == 10:
            l = 1
            r = 7
            red_ball_speed = 14
        if s == 50:
            l = 2
            r = 10
            red_ball_speed = 16
            ball_speed = 22
        if s == 200:
            l = 3
            r = 13
            red_ball_speed = 18
            ball_speed = 24
        if s == 500:
            l = 4
            r = 15
            red_ball_speed = 20
            ball_speed = 28
        if s == 1000:
            l = 5
            r = 20
            red_ball_speed = 25
            ball_speed = 35
#=====/////////////////======ending loop======\\\\\\\\\\\\\\\\\=======
    while gameover:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    gameover = 0
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        yourscore=font1.render(str(s),1,red)
        pygame.display.flip()
        screen.fill(black)
        screen.blit(end, (0, 0))
        screen.blit(yourscore,((w//2)-(h//12),h//3))
