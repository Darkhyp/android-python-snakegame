from math import cos, pi

from kivy.utils import platform

# object size
if platform == 'android':
    STEP_SIZE = 150
else:
    STEP_SIZE = 65

# snake speed
TIME_STEP = 0.3
# snake theme
# SNAKE_THEME = 'light'
SNAKE_THEME = 'dark'

# y shift of score label
if platform == 'android':
    SCORE_LABEL_Y = 200
else:
    SCORE_LABEL_Y = 100

# add gradient to backgraound
# IS_BACKGROUND_GRADIENT = False
IS_BACKGROUND_GRADIENT = True
alpha_channel_rate_min = 0.7
alpha_channel_rate_max = 1
ALPHA_CHANNEL_RATE_FUNC = lambda x: alpha_channel_rate_min + (alpha_channel_rate_max - alpha_channel_rate_min) * (
        1 + cos(2 * pi * x / STEP_SIZE)) / 2

