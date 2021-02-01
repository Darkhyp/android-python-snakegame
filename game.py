import random

from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivymd.toast import toast
from kivy.graphics import Line, Color

from CONFIGS import STEP_SIZE, SCORE_LABEL_Y, IS_BACKGROUND_GRADIENT, ALPHA_CHANNEL_RATE_FUNC
from snake_part import SnakePart
from snack import Snack
from tools import new_random_unique_position, check_widgets_collision, rotate


class GameScreen(Widget):
    dr = [0, 0]
    snake_length = 1
    snake_parts = []
    add_new_part = False
    snack = None
    pos0 = (0, 0)

    def set_game_window(self):
        self.size_hint = [None, None]
        # correct widget size with respect to STEP_SIZE
        old_width = self.width
        old_height = self.height
        self.width = (self.width//STEP_SIZE) * STEP_SIZE
        self.height = (self.height//STEP_SIZE) * STEP_SIZE
        self.pos = [(old_width-self.width)/2, (old_height-self.height)/2]
        self.pos0 = self.pos

        if IS_BACKGROUND_GRADIENT:
            self.add_gradient()

    def add_gradient(self):
        for sep in range(self.width):
            alpha_channel_rate = ALPHA_CHANNEL_RATE_FUNC(sep)
            self.canvas.add(Color(rgba=(0, 1, 0, alpha_channel_rate)))
            self.canvas.add(Line(points=[self.pos[0]+sep, self.pos[1], self.pos[0]+sep, self.pos[1]+self.height], width=1))
        for sep in range(self.height):
            alpha_channel_rate = ALPHA_CHANNEL_RATE_FUNC(sep)
            self.canvas.add(Color(rgba=(0, 1, 0, alpha_channel_rate)))
            self.canvas.add(Line(points=[self.pos[0], self.pos[1]+sep, self.pos[0]+self.width, self.pos[1]+sep], width=1))

    def new_game(self):
        # add a snack
        if self.snack is None:
            self.snack = Snack()
            new_random_unique_position([], self.snack, self.pos0)
            self.add_widget(self.snack)

        # clear snake parts
        for part in self.snake_parts:
            self.remove_widget(part)
        self.snake_parts = []
        self.dr = [0, 0]

        # new head
        head = SnakePart(part_type=0)
        # head random position
        new_random_unique_position([self.snack], head, self.pos0)
        # head random direction
        head.rotate_image(random.choice([0, 90, 180, 270]))
        # append head to list and to widget
        self.snake_parts.append(head)
        self.add_widget(head)

        # display score
        self.display_score()

    def on_touch_up(self, touch):
        # read input
        dr = Vector(touch.x, touch.y) - touch.opos
        if abs(dr.x) > abs(dr.y):
            # move left or right
            self.dr = [STEP_SIZE if dr.x > 0 else -STEP_SIZE, 0]
        else:
            # move up or down
            self.dr = [0, STEP_SIZE if dr.y > 0 else -STEP_SIZE]

    def move_snake(self, *args):
        """
        move snake
        """
        if self.dr != [0, 0]:
            # if it is needed to add a new part
            if self.add_new_part:
                self.add_part()

            # if there is a movement
            # store current snake body positions
            old_r = [tuple(part.pos) for part in self.snake_parts]
            for i, part in enumerate(self.snake_parts):
                if i == 0:
                    # move head
                    part.pos = Vector(part.pos) + self.dr
                    rotate(part, Vector(self.dr), Vector(self.dr))
                else:
                    part.pos = old_r[i-1]
                    rotate(part, Vector(self.snake_parts[i-1].pos)-Vector(part.pos),
                                 Vector(old_r[i-1]) - Vector(old_r[i]))

            # check snake head collisions
            self.check_collision(self.snake_parts[0])

    def check_collision(self, head):
        # check collision of head with snake
        for part in self.snake_parts:
            if part != head:
                if head.pos == part.pos:
                    toast(f"Game over. Last snake size is {len(self.snake_parts)}")
                    self.new_game()

        # check collision with walls (is out of region)
        if not check_widgets_collision(self, head):
            toast(f"Game over. Last snake size is {len(self.snake_parts)}")
            self.new_game()

        # check collision with snack
        snack = self.snack
        if check_widgets_collision(head, snack):
            # new position of a snack
            new_random_unique_position(self.snake_parts, snack, self.pos0)
            # add a new block at the end of the snake
            self.add_new_part = True

    def add_part(self):
        # add tail
        new_tail = SnakePart(part_type=4)
        new_tail.pos = self.snake_parts[-1].pos
        if len(self.snake_parts) == 1:
            # change head from only head part
            self.snake_parts[0].change_image(part_type=1)
        else:
            # change a non head part from a tail (to a body part)
            self.snake_parts[-1].change_image(part_type=2)
        self.snake_parts.append(new_tail)
        self.add_widget(new_tail)
        self.add_new_part = False

        # display score
        self.display_score()

    def display_score(self):
        self.snake_length = len(self.snake_parts)
        self.score_label.text = "Score: " + str(self.snake_length-1)
        self.align_label(self.score_label)

    def align_label(self, label):
        try:
            label.pos = ((self.size[0] - label.width) / 2, self.size[1] - SCORE_LABEL_Y)
        except Exception as e:
            print(e)
            assert False
