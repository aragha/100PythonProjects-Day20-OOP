from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FOLLOWING_DISTANCE = 21
SCREEN_BOUNDARIES = [(-300, -300), (300, 300)]


class Snake:
    # attributes
    new_x = 0
    new_y = 0
    segments = []

    # methods

    def __init__(self):

        # print("initializing")
        # self.add_segment()
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]
    # def create_snake(self):
    #     for position in STARTING_POSITIONS:
    #         self.add_segment(position)
    def add_segment(self, position):
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()  # to remove the line that each block leaves behind
            new_segment.goto(position)
            self.segments.append(new_segment)
    def extend(self):
        # add new segment to snake when it gets a food
        self.add_segment(self.segments[-1].position())
    def check_wall_collision(self):
        # print(f"checking wall collision - {self.head.xcor()}, {self.head.ycor()}")
        if ((self.head.xcor() > SCREEN_BOUNDARIES[0][0]) and (self.head.xcor() < SCREEN_BOUNDARIES[1][0])
                and
                (self.head.ycor() > SCREEN_BOUNDARIES[0][1]) and (self.head.ycor() < SCREEN_BOUNDARIES[1][1])):
            # print(f"checking wall collision - {self.head.xcor()}, {self.head.ycor()}")
            return False
        else:
            return True

    def move_forward(self):

        # instead of focusing on moving the head, we're going to focus on the segments
        # in reverse order. so the for loop will need update
        for seg_num in range(len(self.segments) - 1, 0, -1):  # range(start=2, stop=0, step=-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            # time.sleep(0.1)  # little faster
        # self.segments[0].forward(FOLLOWING_DISTANCE)
        # print("inside move_forward method")
        if self.check_wall_collision():
            return False
        else:
            self.head.forward(FOLLOWING_DISTANCE)
            return True

    def go_north(self):
        # print(f"in north method. heading: {self.segments[0].heading()}")
        if self.head.heading() in [0, 180]:
            self.head.setheading(90)
        else:
            return
        # print(f"in north method.final  heading: {self.segments[0].heading()}")

    def go_south(self):
        # print("in south method")
        if self.head.heading() in [0, 180]:
            self.head.setheading(270)
        else:
            return
        # print(f"in south method.final  heading: {self.segments[0].heading()}")

    def go_west(self):
        # print("in west method")
        if self.head.heading() in [90, 270]:
            self.head.setheading(180)
        else:
            return
        # print(f"in west method.final  heading: {self.segments[0].heading()}")

    def go_east(self):
        # print("in east method")
        if self.head.heading() in [90, 270]:
            self.head.setheading(0)
        else:
            return
        # print(f"in east method.final  heading: {self.segments[0].heading()}")
