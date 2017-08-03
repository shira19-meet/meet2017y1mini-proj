import turtle
import random

turtle.tracer(1,0)

SIZE_X=1200
SIZE_Y=900
turtle.setup(SIZE_X,SIZE_Y)
turtle.bgcolor("pink")

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=14
score = 0

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamp=[]

snake=turtle.clone()
snake.shape("square")
snake.color("light blue")

turtle.hideturtle()

for i in range ( START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    stamp_id=snake.stamp()
    stamp_list.append(stamp_id)

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR="space"
UP=0
LEFT=1
DOWN=2
RIGHT=3

direction=UP
UP_EDGE=400
DOWN_EDGE=-400
RIGHT_EDGE=550
LEFT_EDGE=-550
def up():
    global direction
    direction=UP
    
    print("you pressed the up key")

def down():
    global direction
    direction=DOWN
    
    print("you pressed the down key")

def left():
    global direction
    direction=LEFT
    
    print("you pressed the left key")

def right():
    global direction
    direction=RIGHT
    
    print("you pressed the right key")

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()


def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE

  
    food.goto(food_x,food_y)
    my_pos=(food_x,food_y)
    food_pos.append(my_pos)
    new_food=food.stamp()
    food_stamp.append(new_food)

def draw_rectangle(x,y,w,h):
    draw = turtle.clone()
    draw.hideturtle()
    draw.begin_fill()
    draw.penup()
    draw.goto(x,y)
    draw.pendown()
    draw.goto(x+w,y)
    draw.goto(x+w,y+h)
    draw.goto(x,y+h)
    draw.goto(x,y)
    draw.fillcolor("white")
    draw.end_fill()
    
    
def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    
    
   
    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print("you moved right")
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print("you moved left")
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("you moved up")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print("you moved down")
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)
    #special place-rememberit for part 5
    global food_stamp,food_pos
    if snake.pos() in food_pos:
        global score
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamp[food_ind])
        food_stamp.pop(food_ind)
        food_pos.pop(food_ind)
        score+=1
        scorePen = turtle.clone()
        scorePen.color("pink")
        scorePen.shape("square")
        scorePen.hideturtle()
        scorePen.penup()
        scorePen.goto(230, 192)
        scorePen.stamp()
        scorePen.goto(230 + SQUARE_SIZE, 192)
        scorePen.stamp()
        scorePen.goto(125,175)
        scorePen.color("black")
        scorePen.write("Score: " + str(score), font = ("Ariel", 20, "normal"))
        print("you have eaten the food")
        scorePen.color("white")
        scorePen.circle(30)
        make_food()
        #this if statment may be useful for part 8
    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
    if score>10:
        turtle.bgcolor("blue")
        scorePen = turtle.clone()
        scorePen.color("blue")
        scorePen.shape("square")
        scorePen.hideturtle()
        scorePen.penup()
        scorePen.goto(230, 192)
        scorePen.stamp()
        scorePen.goto(230 + SQUARE_SIZE, 192)
        scorePen.stamp()
        scorePen.goto(125,175)
        scorePen.color("black")
        scorePen.write("Score: " + str(score), font = ("Ariel", 20, "normal"))
        

        

    if score>20:
        turtle.bgcolor("green")
        scorePen = turtle.clone()
        scorePen.color("green")
        scorePen.shape("square")
        scorePen.hideturtle()
        scorePen.penup()
        scorePen.goto(230, 192)
        scorePen.stamp()
        scorePen.goto(230 + SQUARE_SIZE, 192)
        scorePen.stamp()
        scorePen.goto(125,175)
        scorePen.color("black")
        scorePen.write("Score: " + str(score), font = ("Ariel", 20, "normal"))
      
       

     
    if score>30:
        turtle.bgcolor("magenta")
        scorePen = turtle.clone()
        scorePen.color("magenta")
        scorePen.shape("square")
        scorePen.hideturtle()
        scorePen.penup()
        scorePen.goto(230, 192)
        scorePen.stamp()
        scorePen.goto(230 + SQUARE_SIZE, 192)
        scorePen.stamp()
        scorePen.goto(125,175)
        scorePen.color("black")
        scorePen.write("Score: " + str(score), font = ("Ariel", 20, "normal"))
        


      
        
        

    new_pos=snake.pos()
    new_x_pos=my_pos[0]
    new_y_pos=my_pos[1]

    if new_x_pos>=RIGHT_EDGE:
        print("you hit the right edge! game over!")
        quit()
    elif  new_x_pos<=LEFT_EDGE:
        print("you hit the left edge! game over!")
        quit()
    elif new_y_pos>=UP_EDGE:
        print("you hit the up edge! game over!")
        quit()
    elif new_y_pos<=DOWN_EDGE:
        print("you hit the down edge! game over!")
        quit()
    

    if snake.pos() in pos_list[:-1]:
        quit()

    turtle.ontimer(move_snake,TIME_STEP)

move_snake()


food=turtle.clone()
food.shape("turtle")
food.color("yellow")
food_pos=[(100,100),(-100,100),(-100,-100),(100,-100)]
food_stamp=[]

for id_food in food_pos:
    food.goto(id_food[0],id_food[1])
    id_stamp=food.stamp()
    food_stamp.append(id_stamp)
food.hideturtle()



