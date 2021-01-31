from kivy.utils import platform

# object size
if platform == 'android':
    STEP_SIZE = 300
else:
    STEP_SIZE = 50

# snake speed
TIME_STEP = 0.25
