import pygame
import os
import sys
import random

sys.path.insert(0, os.path.join(os.getcwd(), *([".."] * 3)))
from common.Logger.logger import LogConfig, ExceptionCatch

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

class start(object):
    """docstring for start."""
    def __init__(self, LOGGER, CATCH):
        self.LOGGER = LOGGER
        self.CATCH = CATCH
        pygame.init()
        self.SIZE = (700, 500)
        self.CENTER = (250, 250)
        self.SCREEN = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption('Snake')
        self.DONE = False
        self.direction = 'r'
        clock = pygame.time.Clock()
        self.SNAKE = []
        self.LENGTH = 0
        self.RADIUS = 5
        self.INMOTION = False
        self.FOOD = []
        self.ISFOOD = False
        self.FPS = 10
        self.FOOD_SIZE = self.RADIUS+5
        self.SCREEN.fill(BLACK)
        self.snakeAtom(3)
        while not self.DONE:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Quit()
                elif event.type == pygame.KEYDOWN:
                    if(event.key in [pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT]):
                        self.Turn(event.key)

            if(self.INMOTION):
                self.Move()
                if(self.ISFOOD):
                    self.Eat()

            if(self.ISFOOD and random.randrange(100)>98):
                self.Eat(1)

            if(random.randrange(100) > 90 and not self.ISFOOD ):
                self.ISFOOD = True
                self.FOOD = [random.randrange(self.SIZE[0]),random.randrange(self.SIZE[1])]
                pygame.draw.circle(self.SCREEN, BLUE, self.FOOD, self.FOOD_SIZE, self.FOOD_SIZE)
            # -\-- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            self.FPS = self.LENGTH*3

            # --- Limit to 60 frames per second
            clock.tick(self.FPS)
        pygame.quit()

    def Quit(self):
        LOGGER.info('Quit event triggered')
        self.DONE = True

    def Turn(self,key):
        self.INMOTION = True
        LOGGER.info(str(key) + ' is pressed')
        if(key == pygame.K_UP and self.direction != 'd'):
            self.direction = 'u'
        elif(key == pygame.K_LEFT and self.direction != 'r'):
            self.direction = 'l'
        elif(key == pygame.K_RIGHT and self.direction != 'l'):
            self.direction = 'r'
        elif(key == pygame.K_DOWN and self.direction != 'u'):
            self.direction = 'd'


    def Move(self,pop = True):
        if(self.direction == 'r'):
            if(self.SNAKE[0][0]+2*self.RADIUS > self.SIZE[0]):
                LOGGER.info('GameOver')
                self.Quit()
            self.SNAKE = [[self.SNAKE[0][0]+2*self.RADIUS,self.SNAKE[0][1]]] + self.SNAKE
            pygame.draw.circle(self.SCREEN, WHITE, self.SNAKE[0], self.RADIUS, 5)
            pygame.draw.circle(self.SCREEN, BLACK, self.SNAKE[-1], self.RADIUS, 5)
        elif(self.direction == 'l'):
            if(self.SNAKE[0][0]-2*self.RADIUS < 0):
                LOGGER.info('GameOver')
                self.Quit()
            self.SNAKE = [[self.SNAKE[0][0]-2*self.RADIUS,self.SNAKE[0][1]]] + self.SNAKE
            pygame.draw.circle(self.SCREEN, WHITE, self.SNAKE[0], self.RADIUS, 5)
            pygame.draw.circle(self.SCREEN, BLACK, self.SNAKE[-1], self.RADIUS, 5)
        elif(self.direction == 'u'):
            if(self.SNAKE[0][1]-2*self.RADIUS < 0):
                LOGGER.info('GameOver')
                self.Quit()
            self.SNAKE = [[self.SNAKE[0][0], self.SNAKE[0][1]-2*self.RADIUS]] + self.SNAKE
            pygame.draw.circle(self.SCREEN, WHITE, self.SNAKE[0], self.RADIUS, 5)
            pygame.draw.circle(self.SCREEN, BLACK, self.SNAKE[-1], self.RADIUS, 5)
        elif(self.direction == 'd'):
            if(self.SNAKE[0][1]+2*self.RADIUS > self.SIZE[1]):
                LOGGER.info('GameOver')
                self.Quit()
            self.SNAKE = [[self.SNAKE[0][0], self.SNAKE[0][1]+2*self.RADIUS ]] + self.SNAKE
            pygame.draw.circle(self.SCREEN, WHITE, self.SNAKE[0], self.RADIUS, 5)
            pygame.draw.circle(self.SCREEN, BLACK, self.SNAKE[-1], self.RADIUS, 5)
        if(pop):
            self.SNAKE.pop()
            self.LENGTH = len(self.SNAKE)

    def Eat(self,vanish = 0):
        if(vanish == 1):
            pygame.draw.circle(self.SCREEN, BLACK, self.FOOD, self.FOOD_SIZE, self.FOOD_SIZE)
            self.ISFOOD = False
            return
        if( -self.FOOD_SIZE < self.SNAKE[0][0]-self.FOOD[0] < self.FOOD_SIZE and -self.FOOD_SIZE < self.SNAKE[0][1]-self.FOOD[1] < self.FOOD_SIZE):
            pygame.draw.circle(self.SCREEN, BLACK, self.FOOD, self.FOOD_SIZE, self.FOOD_SIZE)
            self.Move(False)
            self.ISFOOD = False

    def snakeAtom(self,length):
        for i in range(0,length):
            self.SNAKE = [[self.CENTER[0]+2*self.RADIUS*i,self.CENTER[1]]] + self.SNAKE
            pygame.draw.circle(self.SCREEN, WHITE, [self.CENTER[0]+2*self.RADIUS*i,self.CENTER[1]], self.RADIUS, 5)
            self.LENGTH += 1

if __name__ == '__main__':
    SRC_PATH = os.path.normpath(os.getcwd() + 4*(os.sep + os.pardir))
    LOGGER = LogConfig(SRC_PATH).ESP_LOGGER
    CATCH = ExceptionCatch(SRC_PATH)
    start(LOGGER,CATCH)
