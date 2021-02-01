from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import StringProperty, NumericProperty, ListProperty

from CONFIGS import STEP_SIZE, SNAKE_THEME

# list of images for snake parts
SNAKE_PART_IMAGES = [
    f"assets/images/{SNAKE_THEME}.snake_head0.png",
    f"assets/images/{SNAKE_THEME}.snake_head.png",
    f"assets/images/{SNAKE_THEME}.snake_body.png",
    f"assets/images/{SNAKE_THEME}.snake_angle.png",
    f"assets/images/{SNAKE_THEME}.snake_tail.png"
]


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
        try:
            self.image_source = SNAKE_PART_IMAGES[part_type]
        except Exception as e:
            self.image_source = ""

    def rotate_image(self, angle):
        if self.part_type >= 0:
            self.image_center = Vector(self.pos) + Vector(self.size)/2
            self.image_angle = angle


