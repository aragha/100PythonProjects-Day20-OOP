from turtle import Screen
import time
from food import Food

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Feed the snake!')


game_is_on = True
from snake import Snake
def end_game():
    game_is_on = False
    screen.bye()
serp = Snake()
food = Food()
screen.listen()
screen.tracer()
screen.onkey(key="Up", fun=serp.go_north)
screen.onkey(key="Down", fun=serp.go_south)
screen.onkey(key="Left", fun=serp.go_west)
screen.onkey(key="Right", fun=serp.go_east)
screen.onkey(key="Escape", fun=end_game)

while game_is_on:
    screen.update()
    game_is_on = serp.move_forward()
    # detect collision with food
    # using the turtle's distance method
    if serp.head.distance(food) < 15:
        print("food picked up")
        # food = Food()
        food.refresh()
    if not game_is_on:
        print("snake hit a wall. game over")
    time.sleep(0.1)

# screen.exitonclick()?