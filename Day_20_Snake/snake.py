from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)  
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
             new_x = self.segments[seg_num - 1].xcor()
             new_y = self.segments[seg_num - 1].ycor()
             self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        

    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # def wall_detect(self):
    #     x, y = self.head.pos()
    #     #if x < -280 or x > 280 or y < -280 or y > 280:
    #     if x > 580 or x < -580 or y > 380 or y < -380:
    #         return True

    def wrap_screen(self):
        x = self.head.xcor()
        y = self.head.ycor()
        if x > 580:
            self.head.goto(-580, y)
        elif x < -580:
            self.head.goto(580, y)
        if y > 380:
            self.head.goto(x, -380)
        elif y < -380:
            self.head.goto(x, 380)


    def snake_grow(self):
        add_segment = Turtle("square")
        add_segment.color("white")
        add_segment.penup()
        x_last, y_last = self.segments[-1].pos()
        print(x_last)
        add_segment.goto(x_last, y_last)
        self.segments.append(add_segment)

    def snake_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def snake_reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    
        
