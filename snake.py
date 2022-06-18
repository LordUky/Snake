import pygame, sys, time, random

pygame.init()
pygame.mixer.music.load('bg.mp3')#import bgm
pygame.mixer.music.set_volume(0.1) #volume
pygame.mixer.music.play(loops=-1)#loop
img, dr, lt, dic1, dic2, = pygame.display.set_mode((1024, 600)), 1, [[512, 300], [492, 300], [472, 300], [452, 300]], {1: 0, 2: 1, 3: 0, 4: 1}, {1: 20, 2: 20, 3: -20, 4: -20} #dr: 右下左上 → 1234
pygame.display.set_caption('image')
img.fill((0, 0, 0))
for i in lt:
    pygame.draw.rect(img, (255, 0, 0), (*i, 20, 20))
pygame.display.update()

def move(n):
    lt.insert(0, lt[0][:])
    del lt[-1]
    lt[0][dic1[n]] += dic2[n]

t = 1
while True:
    u0 = time.time()
    u1 = time.time()
    l = 4
    x, y = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
    while [x, y] in lt:
        x, y = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
    z, w = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
    while [z, w] in lt or (z == x and w == y):
        z, w = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
    r, s = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
    while [r, s] in lt or (r == x and s == y) or (r == z and s == w):
        r, s = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
    p, q = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
    while [p, q] in lt or (p == x and q == y) or (p == z and q == w) and (p == r and q == s):
        p, q = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
    while True:
        if len(lt) > l:
            l = len(lt)
        u2 = time.time()
        if u2 - u1 > 2:
            del lt[-1]
            u1 = time.time()
        t *= 1
        img=pygame.display.set_mode((1024, 600))
        img.fill((0, 0, 0))
        str = pygame.key.get_pressed()#get keyboard pressed info
        if len(lt) != len(set(map(tuple, lt))) or len(lt) == 0:
            time.sleep(0.7)
            font = pygame.font.SysFont('microsoft Yahei', 50)
            text1 = font.render(f'最大长度：{l}', True, (255, 255, 255), (0, 0, 0))
            text2 = font.render(f'存活时间：{int(10*(u2 - u0))/10}秒', True, (255, 255, 255), (0, 0, 0))
            img.blit(text1, (350, 200))
            img.blit(text2, (350, 300))
            pygame.display.update()
            time.sleep(1.3)
            lt = [[512, 300], [492, 300], [472, 300], [452, 300]]
            dr = 1
            t = 1
            u1 = time.time()
            break
        temp = lt[-1][:]
        if str[pygame.K_RIGHT] and dr != 1 and dr != 3:#str[]return 1 if corresponding key is currently pressed
            dr = 1
        elif str[pygame.K_DOWN] and dr != 2 and dr != 4:
            dr = 2
        elif str[pygame.K_LEFT] and dr != 1 and dr != 3:
            dr = 3
        elif str[pygame.K_UP] and dr != 2 and dr != 4:
            dr = 4
        elif str[pygame.K_ESCAPE]:#exit if esc is pressed
            pygame.quit()
        time.sleep(t - 1)
        move(dr)
        if lt[0][0] <= -2:
            lt[0][0] = 1012
        if lt[0][0] >= 1032:
            lt[0][0] = 12
        if lt[0][1] <= -20:
            lt[0][1] = 580
        if lt[0][1] >= 600:
            lt[0][1] = 0
        if [x, y] == lt[0]:
            t = 1
            x, y = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
            while [x, y] in lt:
                x, y = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
            lt.append(temp)
        if [z, w] == lt[0]:
            t = 1
            z, w = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
            while [z, w] in lt or (z == x and w == y):
                z, w = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
            lt.append(temp)
        if [r, s] == lt[0]:
            t = 1
            r, s = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
            while [r, s] in lt or (r == x and s == y) or (r == z and s == w):
                r, s = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
            lt.append(temp)
        if [p, q] == lt[0]:
            t = 1
            p, q = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
            while [p, q] in lt or (p == x and q == y) or (p == z and q == w) and (p == r and q == s):
                p, q = random.randint(0, 48) * 20 + 32, random.randint(0, 27) * 20 + 20
            lt.append(temp)
        for i in lt:
            pygame.draw.rect(img, (255, 0, 0), (*i, 20, 20))
        pygame.draw.rect(img, (255, 255, 255), (x, y, 20, 20))
        pygame.draw.rect(img, (255, 255, 255), (z, w, 20, 20))
        pygame.draw.rect(img, (255, 255, 255), (r, s, 20, 20))
        pygame.draw.rect(img, (255, 255, 255), (p, q, 20, 20))
        pygame.display.update()
        time.sleep(0.03)#refresh
