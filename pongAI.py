from re import A
import pygame
import sys
import time

pygame.init()

size = WIDTH, HEIGHT = 900, 500
FPS = 60
screen = pygame.display.set_mode(size)
BLACK = (0,0,0)
WHITE = (255,255,255)

class Bar():
    
    def __init__(self, dx):
        Bar.left_y = HEIGHT/2 - 35
        Bar.right_y = HEIGHT/2 - 35
        self.x = dx
        self.velocity = 12
    
    def leftmove(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w] and Bar.left_y>0:
            Bar.left_y -= self.velocity        
        elif key_pressed[pygame.K_s] and Bar.left_y<HEIGHT-70:
            Bar.left_y += self.velocity

    def rightmove(self):
        if Ball.y > Bar.right_y:
            Bar.right_y += 17
        else:
            Bar.right_y -= 17

    def draw_left(self):
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.x, Bar.left_y, 12, 70))
    
    def draw_right(self):
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.x, Bar.right_y, 12, 70))


class Ball():
    
    def __init__(self):
        Ball.y = HEIGHT/2 - 4
        self.x = WIDTH/2 - 4
        self.velocity = [20,3]
        self.left_count=0
        self.right_count=0
        self.y_movement=False

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x,self.y), 8)

    def move(self):
        if self.y_movement==False:
            self.x += self.velocity[0]
        else:
            self.x += self.velocity[0]
            Ball.y += self.velocity[1]

        if Ball.y > Bar.right_y and Ball.y < Bar.right_y+70 and self.x>WIDTH-12:
            self.velocity[0] = -self.velocity[0]
            self.y_movement=True            

        elif Ball.y > Bar.left_y and Ball.y < Bar.left_y+70 and self.x<12:
            self.velocity[0] = -self.velocity[0]
            self.y_movement=True

        elif Ball.y > HEIGHT or Ball.y < 0:
            self.velocity[1] = -self.velocity[1]
            
        elif self.x<-15:
            self.left_count+=1
            self.velocity[0] = -self.velocity[0]
            self.x = WIDTH/2 - 4
            Ball.y = HEIGHT/2 - 4
            time.sleep(1.2)
            self.y_movement=False

        elif self.x>WIDTH+15:
            self.right_count+=1
            self.velocity[0] = -self.velocity[0]
            self.x = WIDTH/2 - 4
            Ball.y = HEIGHT/2 - 4
            time.sleep(1.2)
            self.y_movement=False
                    
    def left_score(self):
        font = pygame.font.SysFont('calibri', 60, bold=True)
        scoretext = font.render(str(self.left_count), True, WHITE,)
        screen.blit(scoretext, (WIDTH/2 + 280, 20))

    def right_score(self):
        font = pygame.font.SysFont('calibri', 60, bold=True)
        scoretext = font.render(str(self.right_count), True, WHITE)
        screen.blit(scoretext, (WIDTH/2 - 300, 20))
        
# -Draw left and right bars-
left_bar = Bar(0)
right_bar = Bar(WIDTH - 12)


ball = Ball()


clock = pygame.time.Clock()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    # -mobility-
    ball.move()
    left_bar.leftmove()
    right_bar.rightmove()

    # -background-
    screen.fill(BLACK)
    
    # -draw-
    ball.draw()
    ball.left_score()
    ball.right_score()
    left_bar.draw_left()
    right_bar.draw_right()
    
    pygame.display.update()
    clock.tick(FPS)