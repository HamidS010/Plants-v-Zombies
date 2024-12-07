import arcade
import animate
import time
import objects

SCALE = 0.12


class Plant(animate.Animate):
    def __init__(self, image, health, price):
        super().__init__(image, SCALE)
        self.health = health
        self.price = price
        self.row = 0
        self.column = 0

    def update(self):
        if self.health <= 0:
            self.kill()

    def planting(self, center_x, center_y, row, column):
        self.set_position(center_x, center_y)
        self.row = row
        self.column = column


class Sunflower(Plant):
    def __init__(self, window):
        super().__init__("plants/sun1.png", 80, 50)
        self.append_texture(arcade.load_texture("plants/sun1.png"))
        self.append_texture(arcade.load_texture("plants/sun2.png"))
        self.sun_spawn_time = time.time()
        self.window = window

    def update(self):
        super().update()
        if time.time() - self.sun_spawn_time >= 15:
            new_sun = objects.Sun(self.right, self.top)
            self.sun_spawn_time = time.time()
            self.window.suns_object.append(new_sun)


class Peashooter(Plant):
    def __init__(self, window):
        super().__init__("plants/pea1.png", 80, 100)
        self.append_texture(arcade.load_texture("plants/pea1.png"))
        self.append_texture(arcade.load_texture("plants/pea2.png"))
        self.append_texture(arcade.load_texture("plants/pea3.png"))
        self.pea_sound = arcade.load_sound("sounds/peaspawn.mp3")
        self.window = window
        self.last_shot_time = time.time()

    def update(self):
        super().update()
        if self.health > 0:
            current_time = time.time()
            if current_time - self.last_shot_time >= 3:
                new_bul = objects.Bul(self.right, self.top)
                self.window.buls_object.append(new_bul)
                self.last_shot_time = current_time
                arcade.play_sound(self.pea_sound, 0.5)

class Walnut(Plant):
    def __init__(self, window):
        super().__init__("plants/nut1.png", 80, 50)
        self.append_texture(arcade.load_texture("plants/nut1.png"))
        self.append_texture(arcade.load_texture("plants/nut2.png"))
        self.append_texture(arcade.load_texture("plants/nut3.png"))
        self.window = window

    def update(self):
        super().update()


class Firetree(Plant):
    def __init__(self, window):
        super().__init__("plants/tree1.png", 80, 50)
        self.append_texture(arcade.load_texture("plants/tree1.png"))
        self.append_texture(arcade.load_texture("plants/tree2.png"))
        self.append_texture(arcade.load_texture("plants/tree3.png"))
        self.window = window

    def update(self):
        super().update()
        hit_list_firetree = arcade.check_for_collision_with_list(self,self.window.buls_object)
        if hit_list_firetree:
            for bul in hit_list_firetree:
                bul.texture = arcade.load_texture("items/firebul.png")
                bul.damage = 100
                continue
                #bul.texture = self.set_texture