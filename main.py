import pygame, random, time
from client import Network

fps = 20

c = Network()


clock = pygame.time.Clock()
running = True

x = 720 
y = 720

window = pygame.display.set_mode((x, y))

paddle_1 = pygame.transform.scale(pygame.image.load("Images/paddle.png").convert_alpha(), (200, 100))          
paddle_2 = pygame.transform.scale(pygame.image.load("Images/paddle.png").convert_alpha(), (200, 100)) 

rect_1 = paddle_1.get_rect()
rect_2 = paddle_2.get_rect()


ball = pygame.image.load("Images/ball.png")
gameover_screen = pygame.transform.scale(pygame.image.load("Images/gameover.png").convert_alpha(), (x, y)) 


paddle_1x = 300
paddle_1y = 10

paddle_2x = 300 
paddle_2y = 710

ballx = 300
bally = 350

speedx = 10
speedy = 10

direction1 = 0
direction2 = 0


def moveBall():
    global ballx, bally, speedx, speedy
    ballx += speedx
    bally += speedy

    if ballx >= 660 or ballx <= 10:
        speedx *= -1

def parse_data(data):
    try:
        d = data.split(",")
        return [int(d[0]), int(d[1])]
    except:
        return 0,0

def send_data():
        data =  str(direction1) + "," + str(direction2)
        reply = c.send(data)
        return reply


while running:
    window.fill(pygame.Color(255, 255, 255))

    if paddle_2x <= 80:
        paddle_2x = 80
    
    if paddle_2x >= 600: 
        paddle_2x = 600
    
    if paddle_1x <= 80:
        paddle_1x = 80
    
    if paddle_1x >= 600:
        paddle_1x = 600
    

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False 
        
        if i.type == pygame.KEYDOWN: 
            if i.key == pygame.K_LEFT: 
                direction2 = -16
                

            if i.key == pygame.K_RIGHT: 
                direction2 = 16
            
            if i.key == pygame.K_a:
                direction1 = -16
            
            if i.key == pygame.K_d: 
                direction1 = 16
        
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT: 
                direction2 = 0
            
            elif i.key == pygame.K_a or i.key == pygame.K_d: 
                direction1 = 0

    paddle_2x += direction2
    paddle_1x += direction1

    window.blit(paddle_1, rect_1)
    window.blit(paddle_2, rect_2)

    rect_1.midtop = (paddle_1x, paddle_1y)
    rect_2.midbottom = (paddle_2x, paddle_2y)

    window.blit(ball, (ballx, bally))


    if rect_2.collidepoint((ballx, bally + 25)): 
        speedx *= random.choice([-1, 1])
        speedy *= -1 
    
    if rect_1.collidepoint((ballx, bally + 50)): 
        speedx *= random.choice([-1, 1]) 
        speedy *= -1

    
    if bally >= 720 or bally <= 0: 
        window.fill(pygame.Color(0, 0, 0))
        window.blit(gameover_screen, (0, 0))

        paddle_1y = 10000
        paddle_2y = 10000
    

    direction1, direction2 = parse_data(send_data())

    moveBall()

    # send_data()


    clock.tick(fps)
    pygame.display.update()        