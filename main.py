from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder

# setup
from CONFIGS import STEP_SIZE, TIME_STEP
from tools import new_random_unique_position
from game import GameScreen


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file("snake.kv")

    def build(self):
        return self.screen

    def on_start(self):
        # start new game
        game = self.root
        game.set_game_window()
        game.new_game()

        # init main loop
        Clock.schedule_interval(game.move_snake, TIME_STEP)


MainApp().run()
