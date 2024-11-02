import arcade
import plants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Plants v Zombies"
CELL_WIDTH = 78
CELL_HEIGHT = 100
def lawn_x(x):
    right_x = 248 + CELL_WIDTH
    column = 1
    while right_x <= x:
        right_x += CELL_WIDTH
        column += 1
    center_x = right_x - CELL_WIDTH / 2
    return center_x, column
def lawn_y(y):
    top_y = 24 + CELL_HEIGHT
    row = 1
    while top_y <= y:
        top_y += CELL_HEIGHT
        row += 1
    center_y = top_y - CELL_HEIGHT / 2
    return center_y, row
class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.bg = arcade.load_texture("textures/background.jpg")
        self.menu = arcade.load_texture("textures/menu_vertical.png")
        self.lawns = []
        self.plant_sound = arcade.load_sound("sounds/seed.mp3")
        self.suns_money = 300
    def setup(self):
        self.plants = arcade.SpriteList()
        self.seed = None
        self.suns_object = arcade.SpriteList()
        self.buls_object = arcade.SpriteList()
    def on_draw(self):
        self.clear((255,255,255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        arcade.draw_texture_rectangle(67, SCREEN_HEIGHT / 2, 134, SCREEN_HEIGHT, self.menu)
        self.plants.draw()
        if self.seed != None:
            self.seed.draw()
        self.suns_object.draw()
        self.buls_object.draw()
        arcade.draw_text(f"{self.suns_money}",34,490,(165,42,42),30)
    def update(self,delta_time):
        self.plants.update_animation()
        self.plants.update()
        self.suns_object.update()
        self.buls_object.update()
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        print(x,y)
        if 18 <= x <= 105:
            if 381 <= y <= 472:
                print("sunflower")
                self.seed = plants.Sunflower(self)
            if 270 <= y <= 362:
                print("Pea shooter")
                self.seed = plants.Peashooter(self)
            if 154 <= y <= 248:
                print("walnut")
            if 34 <= y <= 131:
                print("fire tree")
        if self.seed != None:
            self.seed.center_x = x
            self.seed.center_y = y
            self.seed.alpha = 150
    def on_mouse_motion(self,x,y,dx,dy):
        if self.seed != None:
            self.seed.center_x = x
            self.seed.center_y = y
    def on_mouse_release(self,x,y,button,modifiers):
        if 244 <= x <= 566 and 27 <= y <= 524:
            center_x, column = lawn_x(x)
            center_y, row = lawn_y(y)
            if (row,column) not in self.lawns and self.seed.price <= self.suns_money:
                self.seed.planting(center_x,center_y,row,column)
                self.suns_money -= self.seed.price
                self.seed.alpha = 255
                self.plants.append(self.seed)
                self.seed = None
                self.lawns.append((row,column))
                arcade.play_sound(self.plant_sound,0.5)
            if (row,column) in self.lawns:
                self.seed = None
                return
        else:
            self.seed = None
window = Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
window.setup()
arcade.run()