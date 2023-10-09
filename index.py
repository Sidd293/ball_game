import pygame
import random
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRICK_COLORS = [(0,0,0),(255,0,0)]
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BALL_SIZE = 10
BRICK_WIDTH  = 20
BRICK_HEIGHT  = 20
RED = (255,0,0)
BAR_WIDTH = 100
BAR_HEIGHT = 30

brick_map = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 1],
[1, 2, 2, 2, 2, 0, 2, 2, 0, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 1],
[1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
[3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]
print(len(brick_map),len(brick_map[0]))
class Bar:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def  update(self,x):
        self.x  = x
        # self.y = y
    
    def collide(self,ball):
        ball_pos_x = ball.x+ball.vec.x
        ball_pos_y = ball.y+ball.vec.y

        # if (self.x < ball.x + BALL_SIZE and self.x + BRICK_WIDTH > ball.x and self.y < ball.y + BALL_SIZE and self.y + BRICK_HEIGHT > ball.y):
        if (self.x < ball_pos_x + BALL_SIZE and self.x + BAR_WIDTH > ball_pos_x and self.y < ball_pos_y + BALL_SIZE and self.y + BAR_HEIGHT > ball_pos_y):
            return True
        return False
    

class Brick:
    def __init__(self,x,y,typ):
        self.typ = typ
        self.x = x
        self.y = y
    
    def collide(self,ball):
        ball_pos_x = ball.x+ball.vec.x
        ball_pos_y = ball.y+ball.vec.y

        # if (self.x < ball.x + BALL_SIZE and self.x + BRICK_WIDTH > ball.x and self.y < ball.y + BALL_SIZE and self.y + BRICK_HEIGHT > ball.y):
        if (self.x < ball_pos_x + BALL_SIZE and self.x + BRICK_WIDTH > ball_pos_x and self.y < ball_pos_y + BALL_SIZE and self.y + BRICK_HEIGHT > ball_pos_y):
            return True
        return False
        
lis = [[0]*20]*30
# for row in lis:
#     print(row,end = ",")
#     print("")
 
class Ball:
    # vec = pygame.Vector2(1.0,1.0)
    vel = 10 
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 10
        self.vec = pygame.Vector2(5.0,5.0).rotate(39)
    def update(self):
        self.x = self.x+self.vec.x
        self.y = self.y+self.vec.y

    def checks(self):
        ball_pos_x = self.x+self.vec.x
        ball_pos_y = self.y+self.vec.y
        if ball_pos_x - BALL_SIZE < 0 or ball_pos_x + BALL_SIZE > SCREEN_WIDTH:
            self.vec = self.vec.rotate(80+random.randint(0,10))
        if ball_pos_y - BALL_SIZE < 0 or ball_pos_y + BALL_SIZE > SCREEN_HEIGHT:
            self.vec = self.vec.rotate(80+random.randint(0,10))
            
pad = 2
def main():
    bar = Bar(0,SCREEN_HEIGHT-BAR_HEIGHT)
    """
    This is our main program.
    """
    pygame.init()
    # ball = Ball(100,SCREEN_HEIGHT-100.0)
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    balls = [Ball(100,SCREEN_HEIGHT-100.0)]
 
    pygame.display.set_caption("Ballz BRICKS BREACKER")
    
    mouseX = 0
    mouseY = 0
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    bricks = [[]]





    print(len(brick_map),len(brick_map[0]))
    for ci ,i in enumerate(brick_map):
        brickskRow = []
        for cj,  j in enumerate(i):
            brickskRow.append(Brick(cj*BRICK_WIDTH,ci*BRICK_HEIGHT , j))
        bricks.append(brickskRow)
  
    # -------- Main Program Loop -----------
    while not done:
       
        clock.tick(50)
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEMOTION:
                pos=pygame.mouse.get_pos()
                btn=pygame.mouse
                mouseX = pos[0]
                mouseY = pos[1]
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                balls.append(Ball(balls[0].x,balls[0].y))
                print ('mouse button down')
        background.fill((255,255,255))
        screen.blit(background, (0, 0))

        for brickRow in bricks:
            for brick in brickRow:
                bcolor = (255,255,255)
                if brick.typ == 1 : 
                    bcolor = (100,100,100)
                elif brick.typ ==2 :
                    bcolor = (100,255,100)
                elif brick.typ == 0:
                    bcolor = (128,0,128)
                

                
                # print((brick.y))
                pygame.draw.rect(screen, (255,0,0), pygame.Rect(bar.x,bar.y,BAR_WIDTH,BAR_HEIGHT))

                pygame.draw.rect(screen, bcolor, pygame.Rect(brick.x,brick.y,BRICK_WIDTH,BRICK_HEIGHT))
                for ball in balls:
                    if brick.collide(ball):
                        
                        # print(ball.vec,end=" ")
                        # 1 -> breakable , 2 -> unbreakable , 3 - > blank
                        # print(ball.vec)
                        if(brick.typ == 1):
                            ball.vec = ball.vec.rotate(90+random.randint(0, 5))
                        elif(brick.typ == 2):
                            ball.vec = ball.vec.rotate(90+random.randint(0, 5))
                            if brick in brickRow:
                                brickRow.remove(brick)
                        elif(brick.typ == 0):
                            ball.vec = ball.vec.rotate(90+random.randint(0, 5))
                            balls.append(Ball(ball.x,ball.y))
                            if brick in brickRow:
                                brickRow.remove(brick)
        for ball in balls:pygame.draw.circle(screen, (0,0,255), [ball.x,ball.y], BALL_SIZE)
        for ball in balls:
            if(bar.collide(ball)):
                ball.vec = ball.vec.rotate(70+random.randint(1, 20))
            ball.checks()
            
            ball.update()
        bar.update(mouseX)
        pygame.display.flip()

        #  print ("x = {}, y = {}".format(pos[0], pos[1]))
        # pygame.
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()