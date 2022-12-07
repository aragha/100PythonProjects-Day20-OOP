from turtle import Screen
import time
from food import Food
from scores import Score
from snake import Snake
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Feed the snake!')

game_is_on = True
def end_game():
    game_is_on = False
    screen.bye()
serp = Snake()
food = Food()
scoreboard = Score()
screen.listen()
screen.tracer()
screen.onkey(key="Up", fun=serp.go_north)
screen.onkey(key="Down", fun=serp.go_south)
screen.onkey(key="Left", fun=serp.go_west)
screen.onkey(key="Right", fun=serp.go_east)
screen.onkey(key="Escape", fun=end_game)
scoreboard.write_score()
while game_is_on:
    screen.update()
    # time.sleep(0.1)
    game_is_on = serp.move_forward()
    # detect collision with food
    # using the turtle's distance method
    if serp.head.distance(food) < 15:
        print("food picked up")
        scoreboard.score += 1
        scoreboard.write_score()
        # food = Food()
        food.refresh()
        serp.extend()
    #  if head collides with any part of the snake, the game should end

    # for segment in serp.segments:
    #     if segment == serp.head:
    #         pass
    #     elif serp.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    #  same as above, but using slicing
    temp_segments = serp.segments[1:] # remove the first entry in segments, which is the head
    for segment in temp_segments:
        if serp.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    if not game_is_on:
        # print("snake hit a wall. game over")
        scoreboard.game_over()


screen.exitonclick()