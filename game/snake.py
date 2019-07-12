import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game")

#Game Variables

screen_width = 500
screen_height = 500
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
fps = 30
font=pygame.font.SysFont(None,30)


#Display

gamewindow=pygame.display.set_mode((screen_width,screen_height))
clock=pygame.time.Clock()

#Function

def text_scren(text,color,x,y):
    screen_text=font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])

def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, black, [x,y, snake_size, snake_size])
#Logic

def gameloop():

    score = 0
    exit_game = False
    gameover=0
    snakeX = 10
    snakeY = 30
    snake_size = 10
    food_size=7
    snk_length = 1
    velocityX = 0
    velocityY = 0
    foodX = random.randint(30, screen_width / 2)
    foodY = random.randint(30, screen_height / 2)
    snk_list = []

    while not exit_game:
            if gameover:
                gamewindow.fill(white)
                text_scren("Press Enter To Restart The Game!!",red,80,250)
                for x in pygame.event.get():
                    if x.type == pygame.QUIT:
                        exit_game = True
                    if x.type==pygame.KEYDOWN:
                        if x.key==pygame.K_RETURN:
                            gameloop()

            else:
                for x in pygame.event.get():
                    if x.type == pygame.QUIT:
                        exit_game = True

                    if x.type==pygame.KEYDOWN:
                        if x.key==pygame.K_RIGHT:
                            velocityY=0
                            velocityX=5

                        if x.key==pygame.K_LEFT:
                            velocityY=0
                            velocityX=-5

                        if x.key==pygame.K_UP:
                            velocityX=0
                            velocityY=-5

                        if x.key==pygame.K_DOWN:
                            velocityX=0
                            velocityY=5

                snakeX=snakeX+velocityX
                snakeY=snakeY+velocityY

                if abs(snakeX-foodX)<10 and abs(snakeY-foodY)<10:
                    score+=10
                    foodX = random.randint(30, screen_width/2)
                    foodY = random.randint(30, screen_height/2)
                    snk_length+=5


                if snakeX>=screen_width:
                    snakeX=1

                if snakeX<=0:
                    snakeX=screen_width-1

                if snakeY>=screen_height:
                    snakeY=1

                if snakeY<=0:
                    snakeY=screen_height

                gamewindow.fill(white)
                text_scren("Score:"+str(score),red,5,5)
                head=[]
                head.append(snakeX)
                head.append(snakeY)
                snk_list.append(head)

                plot_snake(gamewindow,black,snk_list,snake_size)

                if len(snk_list)>snk_length:
                    del snk_list[0]


                if head in snk_list[:-1]:
                    gameover=1
                pygame.draw.rect(gamewindow,red, [foodX, foodY, food_size, food_size])
            pygame.display.update()
            clock.tick(fps)

gameloop()
