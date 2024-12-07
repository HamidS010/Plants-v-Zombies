import arcade
import plants
import time
import zombies
import random
import constants
import services


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("textures/background.jpg")
        self.menu = arcade.load_texture("textures/menu_vertical.png")
        self.lawns = []
        self.plant_sound = arcade.load_sound("sounds/seed.mp3")
        self.suns_money = 500
        self.win = False
        self.killed_zombies = 0
        self.spawn_timer = 25

    def setup(self):
        self.plants = arcade.SpriteList()
        self.seed = None
        self.suns_object = arcade.SpriteList()
        self.buls_object = arcade.SpriteList()
        self.firebuls_object = arcade.SpriteList()
        self.zombies = arcade.SpriteList()
        self.zombie_spawn_time = time.time()

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2,
            constants.SCREEN_WIDTH,
            constants.SCREEN_HEIGHT,
            self.bg,
        )
        arcade.draw_texture_rectangle(
            67, constants.SCREEN_HEIGHT / 2, 134, constants.SCREEN_HEIGHT, self.menu
        )
        self.plants.draw()
        if self.seed != None:
            self.seed.draw()
        self.suns_object.draw()
        self.buls_object.draw()
        self.zombies.draw()
        arcade.draw_text(f"{self.suns_money}", 34, 490, (165, 42, 42), 30)
        if self.win:
            self.win_screen = arcade.load_texture("textures/logo.png")
            arcade.draw_texture_rectangle(constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT,constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT /2,self.win_screen)
    def update(self, delta_time):
        if self.win == False:
            self.plants.update_animation()
            self.plants.update()
            self.suns_object.update()
            self.buls_object.update()
            self.firebuls_object.update()
            self.zombies.update()
            self.zombies.update_animation(delta_time)
            if self.killed_zombies == 5:
                self.spawn_timer = 20
            if self.killed_zombies == 10:
                self.spawn_timer = 15
            if self.killed_zombies == 15:
                self.spawn_timer = 10
            if self.killed_zombies == 20:
                self.spawn_timer = 5
                self.win = True
            if time.time() - self.zombie_spawn_time > self.spawn_timer:
                center_y, _= services.lawn_y(random.randint(24, 524))
                zombie_type = random.randint(1,3)
                if zombie_type == 1:
                    self.zombies.append(zombies.OrdinaryZombie(center_y,self))
                    self.zombie_spawn_time = time.time()
                elif zombie_type == 2:
                    self.zombies.append(zombies.ConeheadZombie(center_y,self))
                    self.zombie_spawn_time = time.time()
                else:
                    self.zombies.append(zombies.BucketheadZombie(center_y,self))
                    self.zombie_spawn_time = time.time()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if 18 <= x <= 105:
            if 381 <= y <= 472:
                self.seed = plants.Sunflower(self)
            if 270 <= y <= 362:
                self.seed = plants.Peashooter(self)
            if 154 <= y <= 248:
                self.seed = plants.Walnut(self)
            if 34 <= y <= 131:
                self.seed = plants.Firetree(self)
        if self.seed != None:
            self.seed.center_x = x
            self.seed.center_y = y
            self.seed.alpha = 150
        for sun in self.suns_object:
            if sun.left <=x <= sun.right and sun.bottom <= y <= sun.top:
                sun.kill()
                self.suns_money += 25
    def on_mouse_motion(self, x, y, dx, dy):
        if self.seed != None:
            self.seed.center_x = x
            self.seed.center_y = y

    def on_mouse_release(self, x, y, button, modifiers):
        if 244 <= x <= 950 and 27 <= y <= 524:
            center_x, column = services.lawn_x(x)
            center_y, row = services.lawn_y(y)
            if (row, column) not in self.lawns and self.seed.price <= self.suns_money:
                self.seed.planting(center_x, center_y, row, column)
                self.suns_money -= self.seed.price
                self.seed.alpha = 255
                self.plants.append(self.seed)
                self.seed = None
                self.lawns.append((row, column))
                arcade.play_sound(self.plant_sound, 0.5)
            if (row, column) in self.lawns:
                self.seed = None
                return
        else:
            self.seed = None


window = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
window.setup()
arcade.run()
