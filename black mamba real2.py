from turtle import Turtle, Screen # turtle 객체와 스크린 띄우기
import time
import random

def up():
    if snakes[0].heading() != 270: #위쪽으로 향할땐 꼬리와 머리가 겹치지 않게 완전 반대로 내려가지 못하게(꼬리와 머리가 만나면 게임 아웃)
       snakes[0].setheading(90)

def down():
    if snakes[0].heading() != 90: 
       snakes[0].setheading(270)
    
def right():
    if snakes[0].heading() != 180: 
       snakes[0].setheading(0)

def left():
    if snakes[0].heading() != 0:
       snakes[0].setheading(180)
    
    
def create_snake(pos): #위치 값 매개변수 사용하여 넣기
    snake_body= Turtle()
    snake_body.shape("square") #snake 모양
    snake_body.color("black") #snake 색
    snake_body.up() 
    snake_body.goto(pos)
    snakes.append(snake_body)
  
def rand_pos():
    rand_x = random.randint(-250, 250)
    rand_y = random.randint(-250, 250)
    return rand_x, rand_y  
  
def score_update():  # 함수만들기
        global score
        score += 1
        score_pen.clear()
        score_pen.write(f"점수 : {score}", font = ("", 15, "bold"))

def score_update_2():
        global score
        score_pen.clear()
        score_pen.write(f"점수 : {score}", font = ("", 15, "bold"))
        
def game_over():
    score_pen.goto(0,0)
    score_pen.write("Game Over", False, "center", ("", 30, "bold"))
      
        
screen = Screen() # 스크린 사용하기
screen.setup(600, 600) #스크린 크기
screen.bgcolor("pink") #background color 설정
screen.title("Snake Game") #이름 정하기
screen.tracer(0) #깜빡임 끄기(실행된 모든 과정을 한번에 업데이트)

#snake body
start_pos = [(0,0), (-20,0), (-40,0)] #snake 위치 
snakes = [] # 리스트 저장
score = 0 #스코어 변수 생성

for pos in start_pos:
    create_snake(pos) #시작했을때 위치

#먹이 만들기
food = Turtle()
food.shape("circle")
food.color("snow")
food.up()
food.speed(0)
food.goto(rand_pos())

#소화제 만들기
medicine = Turtle()
medicine.shape("square")
medicine.color("green")
medicine.up()
medicine.speed(0)
medicine.goto(rand_pos())

#점수 카운트
score_pen = Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270, 250)
score_pen.write(f"점수 :{score}", font = ("", 15, "bold"))
    

screen.listen() #키를 통해 상하좌우 이동 가능하게 만들기
screen.onkeypress(up, "Up")    
screen.onkeypress(down, "Down")    
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

game_on = True #while문 통해 뱀이 계속 움직일 수 있게 변수를 만들어 놓는것
while game_on:
    screen.update()# tracer 사용
    time.sleep(0.1) #천천히 하기 위해    
  
    for i in range(len(snakes) -1, 0, -1):
        snakes[i].goto(snakes[i-1].pos())
  
    snakes[0].forward(20)
    
    if snakes[0].distance(food) < 15:
        score_update()
        food.goto(rand_pos())
        create_snake(snakes[-1].pos()) # 음식을 먹었을때 뱀의 꼬리도 길어지게 만들기 (매개변수 사용)
    if snakes[0].distance(medicine) < 15:
        score_update_2()
        medicine.goto(rand_pos())
        snakes[-1].goto(1000,1000)
        del snakes[-1] # 소화제를 먹었을때 뱀의 꼬리가 짧아지게 만들기 (매개변수 사용)
       
    #뱀이 벽면에 닿았을 경우 끝나게 하기
    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 \
       or snakes[0].ycor() > 280 or snakes[0].ycor() < -280:
      game_on = False  
      game_over()
      
    # 뱀이 자기 몸에 부딪힐 경우 게임오버
    for body in snakes[1:]:
        if snakes[0].distance(body) < 10:
           game_on = False
           game_over()

