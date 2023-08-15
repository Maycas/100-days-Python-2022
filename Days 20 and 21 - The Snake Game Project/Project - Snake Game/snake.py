from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

SNAKE_COLOR = "white"
BODY_SEGMENT_SIZE = 20
STEP = 20


class Snake:

    def __init__(self):
        self.snake_body_segments = []
        self.create_snake(BODY_SEGMENT_SIZE)
        self.head = self.snake_body_segments[0]

    def create_snake(self, body_segment_size):
        for index in range(3):
            x = - (body_segment_size * index)
            y = 0
            self.add_segment((x, y))

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color(SNAKE_COLOR)
        new_segment.goto(position)

        self.snake_body_segments.append(new_segment)

    def extend(self):
        self.add_segment(self.snake_body_segments[-1].position())

    def collision_with_tail(self):
        for segment in self.snake_body_segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seg_num in range(len(self.snake_body_segments) - 1, 0, -1):
            # Moving segments to the position of the previous one, so we can keep track of the movement when the first
            # segment moves to a different direction
            new_x = self.snake_body_segments[seg_num - 1].xcor()
            new_y = self.snake_body_segments[seg_num - 1].ycor()
            self.snake_body_segments[seg_num].setpos(new_x, new_y)

        self.head.forward(STEP)
