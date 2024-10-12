import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ping Pong"
class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
    def setup(self):
        pass
    def on_draw(self):
        self.clear((255,255,255))
    def update(self,delta_time):
        pass
    def on_key_press(self, symbol: int, modifiers: int):
        pass
    def on_key_release(self, symbol: int, modifiers: int):
        pass

window = Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
window.setup()
arcade.run()