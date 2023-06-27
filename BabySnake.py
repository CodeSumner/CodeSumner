from graphics import Canvas
import time
import random

#https://codeinplace.stanford.edu/cip3/share/GoYVskzeM7gxzIzT5qdR

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
VELOCITY = 20
START_X = 0
START_Y = 0

# if you make this larger, the game will go slower
DELAY = 0.1 

def game_over_message(canvas, points):
    canvas.create_text(140, 100, text='GAME OVER', color = 'salmon', 
                    font ='Courier', font_size = 20)
    canvas.create_text(110, 120, text='You get ' + str(points) +
                    ' points', color = 'salmon', font ='Courier', font_size = 20)
 
def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # set snake 
    snake_x = START_X
    snake_y = START_Y
    snake = canvas.create_rectangle(snake_x, snake_x, snake_x + SIZE, snake_x + SIZE, 'blue')
    
    # set bird
    bird_x = 360
    bird_y = 360
    bird = canvas.create_rectangle(bird_x, bird_y, bird_x + SIZE, bird_y +SIZE,"salmon")
    
    
    # write text of points
    points = 0
    txt_p = canvas.create_text(10, 370, text='  points', 
            color = 'orange', font ='Courier', font_size = 20)
    txt_pt = canvas.create_text(10, 370, text= str(points), 
            color = 'orange', font ='Courier', font_size = 20)
    
    # set variables and flag
    x_velocity = VELOCITY
    y_velocity = VELOCITY
    direction = "right"
    
    # animation loop
    while True:
        
        canvas.moveto(snake, snake_x, snake_y)
        key = canvas.get_last_key_press()

        # detect collison
        if snake_x == bird_x and snake_y == bird_y:
                points += 1 # add points
                canvas.change_text(txt_pt, str(points)) # display changed points. 
                canvas.delete(bird) # delete previous bird
                
                # create random bird 
                bird_x = random.randint(0, CANVAS_WIDTH/SIZE-1)*SIZE
                bird_y = random.randint(0, CANVAS_HEIGHT/SIZE-1)*SIZE
                bird = canvas.create_rectangle(bird_x, bird_y, bird_x + SIZE, bird_y +SIZE,"salmon");
            
        # set snake move at tendency.    
        if key == None: 
            if direction == "left":
                snake_x -= x_velocity
            if direction == "right":
                snake_x += x_velocity
            if direction == "up":
                snake_y -= y_velocity
            if direction == "down":
                snake_y += y_velocity
                
        # set snake move left at 'ArrowLeft' key.    
        if key == 'ArrowLeft':
            snake_x -= x_velocity
            direction = "left"
            
        # set snake move right at 'ArrowRight' key.     
        if key == 'ArrowRight':
            snake_x += x_velocity
            direction = "right"
            
        # set snake move up at 'ArrowUp' key.
        if key == 'ArrowUp':
            snake_y -= VELOCITY 
            direction = "up"
            
        # set snake move down at 'ArrowDown' key.    
        if key == 'ArrowDown':
            snake_y += VELOCITY 
            direction = "down"
            
        # game over when snake hit the walls.
        if snake_x > CANVAS_WIDTH - SIZE or snake_y > CANVAS_HEIGHT - SIZE:
                game_over_message(canvas, points)
                break
            
        # game over when snake hit the walls.    
        if snake_x < START_X or snake_y < START_Y:
            game_over_message(canvas, points)
            break
        
        # sleep
        time.sleep(DELAY)
        

if __name__ == '__main__':
    main()

