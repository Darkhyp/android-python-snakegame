from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import StringProperty, NumericProperty, ListProperty

from CONFIGS import STEP_SIZE


class SnakePart(Widget):
    size = [STEP_SIZE, STEP_SIZE]
    image_angle = NumericProperty(0)
    image_center = ListProperty([0, 0])
    image_source = StringProperty("")
    part_type = 0

    def __init__(self, **kwargs):
        super().__init__()
        self.change_image(part_type=kwargs.get('part_type', 0))

    def change_image(self, part_type=0):
        self.part_type = part_type
        if part_type == 0:
            self.image_source = "assets/images/snake_head0.png"
        elif part_type == 1:
            self.image_source = "assets/images/snake_head.png"
        elif part_type == 2:
            self.image_source = "assets/images/snake_body.png"
        elif part_type == 3:
            self.image_source = "assets/images/snake_angle.png"
        elif part_type == 4:
            self.image_source = "assets/images/snake_tail.png"
        else:
            self.image_source = ""

    def rotate_image(self, angle):
        if self.part_type >= 0:
            self.image_center = Vector(self.pos) + Vector(self.size)/2
            self.image_angle = angle


