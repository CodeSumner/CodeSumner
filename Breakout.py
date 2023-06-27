#Breakout.py

#https://codeinplace.stanford.edu/cip3/share/BiVwen4sKsl5ih4BaQnK

import graphics
import time
import random
import math

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600
PADDLE_Y = CANVAS_HEIGHT - 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

BRICK_GAP = 5
BRICK_WIDTH = (CANVAS_WIDTH-BRICK_GAP*9) / 10
BRICK_HEIGHT = 10

white_space = (BRICK_HEIGHT + BRICK_GAP) *5
row_nums = 10
col_nums = 10

START_X = CANVAS_WIDTH/2 - BALL_RADIUS
START_Y = CANVAS_HEIGHT/2 - BALL_RADIUS
INITIAL_VELOCITY = 10
delete_bricks_num = []# count the number of bricks that have been deleted
DELAY = 0.001


    
def create_bricks(canvas):
    
  
    for row in range(row_nums):
        for col in range(col_nums):
            left_x = col*(BRICK_WIDTH + BRICK_GAP)
            top_y = white_space + row*(BRICK_HEIGHT + BRICK_GAP)
            right_x = left_x + BRICK_WIDTH
            bottom_y = top_y + BRICK_HEIGHT
            color = ['red','red','orange','orange','yellow','yellow','green','green','cyan','cyan']
            brick = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, color = color[row])
      

def main():
    
    canvas = graphics.Canvas(CANVAS_WIDTH,CANVAS_HEIGHT)
    create_bricks(canvas)
    
    # create_ball
    ball_x = START_X
    ball_y = START_Y
    ball = canvas.create_oval(ball_x, ball_y, ball_x + 2*BALL_RADIUS, 
                                       ball_y + 2*BALL_RADIUS, 'blue')
    
    # create_paddle
    paddle_x = CANVAS_WIDTH/2 - PADDLE_WIDTH/2 
    # 10 is the gap of paddle bottom to canvas bottom
    paddle_y = CANVAS_HEIGHT - PADDLE_HEIGHT - 10 
    paddle = canvas.create_rectangle(paddle_x, paddle_y, paddle_x + 
                     PADDLE_WIDTH, paddle_y + PADDLE_HEIGHT, "pink")
    
    # set bouncing ball velocity and variables
    x_velocity = random.choice([INITIAL_VELOCITY, -INITIAL_VELOCITY]) 
    y_velocity = INITIAL_VELOCITY
    collide = 0 # eliminate "glue" variable
    
    # set direction flag
    direction = 'down'
    
    while True:
        # set paddle track the mouse
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_x()
        paddle_x = mouse_x
        # set the mouse_x at the middle position of paddle
        canvas.moveto(paddle, mouse_x - PADDLE_WIDTH/2, paddle_y) 
        time.sleep(DELAY)
        
        # set the bouncing ball
        ball_x += x_velocity
        ball_y += y_velocity    
        canvas.moveto(ball, ball_x, ball_y)
        
        # after the ball hit bottom, program will return to main().
        if (ball_y + 2*BALL_RADIUS > CANVAS_HEIGHT):
            collide = 0 
            delete_bricks_num.clear() # prepare to restart the game.
            return
        
        # after the ball hit the left and right wall, ball's direction will reverse.
        if (ball_x < 0) or (ball_x + 2*BALL_RADIUS >= CANVAS_WIDTH):
            x_velocity = -x_velocity
            collide = 0 
        
        # after the ball hit the top wall, ball's direction will reverse to go down.  
        if (ball_y < 0):
            if direction == 'down':
                y_velocity = -y_velocity
        
        # detect all the shapes the ball meets.
        colliding_list = canvas.find_overlapping(ball_x, ball_y, ball_x + 2*BALL_RADIUS, 
                                       ball_y + 2*BALL_RADIUS)
      
        # detect the paddle collision and let ball bounces once at collide equals to 0.                       
        for shape in colliding_list:
            # shape_101 is the paddle, the ball will bounce after meets the paddle.
            if shape == 'shape_101' and collide == 0:
                    y_velocity = -y_velocity
                    collide += 1 # eliminate "glue"
            
            # detect the bricks collision and delete them.            
            if shape != ball and shape != 'shape_101':
                    y_velocity = -y_velocity
                    delete_bricks_num.append(shape)
                    canvas.delete(shape)
                    collide = 0 
                   
        # after all the bricks deleted, leave a message.       
        if len(delete_bricks_num) == 100:
            canvas.create_text(140, 100, text='YOU WIN!', color = 'black', 
                    font ='Courier', font_size = 40)
            break
        time.sleep(DELAY)
        
if len(delete_bricks_num) != 100:
    for i in range(2):# retart the game in two times.        
        main()


if __name__ == '__main__':
    main()