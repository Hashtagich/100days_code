from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

width, height = 600, 600  # Параметры окна

# Создаём окно
screen = Screen()

screen.setup(width, height)
screen.bgcolor('black')
screen.title("Змейка")
screen.tracer(0)

# Создаём начальную змейку, еду и табло с результатом
snake = Snake()
food = Food()
score = Scoreboard()

# Создаём управление движение змеи
screen.listen()
# управление на стрелках
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
# управление на wasd
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

# Сама игра через цикл
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()  # Змея будет двигаться вперёд пока не врежется в стену или пока цикл не прекратиться

# Появление новой еды и сумма очков
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend()
        score.write_score()

# Проверка на столкновение со стеной
    if snake.head.xcor() > 280 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -280:
        game_is_on = False
        score.write_game_over()

# Проверка на укус хвоста
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.write_game_over()

screen.exitonclick()  # чтобы окно не исчезло сразу
