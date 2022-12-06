
from turtle import Screen
import time
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Feed the snake!')
#
# def goto_NORTH():
#     if serp.heading == 0:
#         serp.setheading(90)
#     elif serp.heading == 180:
#         serp.setheading(-90)
#     elif serp.heading == 270:
#         serp.setheading(180)
#     else:
#         pass
# def goto_SOUTH():
#     if serp.heading == 0:
#         serp.setheading(-90)
#     elif serp.heading == 90:
#         serp.setheading(180)
#     elif serp.heading == 270:
#         serp.setheading(90)
#     else:
#         pass
# def goto_WEST():
#     if serp.heading == 0:
#         serp.setheading(180)
#     elif serp.heading == 90:
#         serp.setheading(90)
#     elif serp.heading == 270:
#         serp.setheading(-90)
#     else:
#         pass
# def goto_EAST():
#     if serp.heading == 90:
#         serp.setheading(-90)
#     elif serp.heading == 180:
#         serp.setheading(180)
#     elif serp.heading == 270:
#         serp.setheading(90)
#     else:
#         pass


game_is_on = True
from snake import Snake
def end_game():
    game_is_on = False
    screen.bye()
serp = Snake()
screen.listen()
screen.tracer()
screen.onkey(key="Up", fun=serp.go_north)
screen.onkey(key="Down", fun=serp.go_south)
screen.onkey(key="Left", fun=serp.go_west)
screen.onkey(key="Right", fun=serp.go_east)
screen.onkey(key="Escape", fun=end_game)

while game_is_on:
    screen.update()
    serp.move_forward()
    time.sleep(0.1)

# screen.exitonclick()?