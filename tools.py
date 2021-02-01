from kivy.core.window import Window
import random

from CONFIGS import STEP_SIZE


def check_widgets_collision(wid1, wid2):
    return ((wid1.pos[0] <= wid2.pos[0] < wid1.pos[0]+wid1.size[0]) \
            or (wid1.pos[0] < wid2.pos[0]+wid2.size[0] <= wid1.pos[0]+wid1.size[0]))\
        and ((wid1.pos[1] <= wid2.pos[1] < wid1.pos[1]+wid1.size[1]) \
            or (wid1.pos[1] < wid2.pos[1]+wid2.size[1] <= wid1.pos[1]+wid1.size[1]))


def new_random_unique_position(parts, new_part, pos0):
    is_occupied = True
    while is_occupied:
        new_part.pos = (pos0[0] + random.randint(0, (Window.width - new_part.width) // STEP_SIZE) * STEP_SIZE,
                        pos0[1] + random.randint(0, (Window.height - new_part.height) // STEP_SIZE) * STEP_SIZE)
        # check collision of a new snack with snake
        is_occupied = False
        for part in parts:
            if check_widgets_collision(part, new_part):
                # find new random new_part position again
                is_occupied = True
                break


def rotate(part, dr, dr0):
    if dr == dr0 or part.part_type == 4:
        # release angle part
        if part.part_type == 3:
            part.change_image(part_type=2)

        if dr.x == 0:
            angle = 180 if dr.y > 0 else 0
        else:
            angle = 90 if dr.x > 0 else -90
    else:
        # angle part
        r = dr - dr0
        if r.x < 0 and r.y < 0: angle = 0
        elif r.x > 0 and r.y > 0: angle = 180
        elif r.x < 0 and r.y > 0: angle = -90
        elif r.x > 0 and r.y < 0: angle = 90
        else: angle = 0
        part.change_image(part_type=3)
    part.rotate_image(angle=angle)

