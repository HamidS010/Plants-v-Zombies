import arcade
import animate
import time
import objects

SCALE = 0.12

class Plant(animate.Animate):
    def __init__(self,image,health,price):
        super().__init__(image,SCALE)
        self.health = health
        self.price = price
        self.row = 0
        self.column = 0
    def update(self):
        if self.health == 0:
            self.kill()
    def planting(self,center_x,center_y,row,column):
        self.set_position(center_x,center_y)
        self.row = row
        self.column = column


class Sunflower(Plant):
    def __init__(self,window):
        super().__init__("plants/sun1.png",80,50)
        self.append_texture(arcade.load_texture("plants/sun1.png"))
        self.append_texture(arcade.load_texture("plants/sun2.png"))
        self.sun_spawn_time = time.time()
        self.window = window
    def update(self):
        if time.time() - self.sun_spawn_time >= 15:
            new_sun = objects.Sun(self.right,self.top)
            self.sun_spawn_time = time.time()
            self.window.suns_object.append(new_sun)
            


class Peashooter(Plant):
    def __init__(self, window):
        super().__init__("plants/pea1.png", 80, 100)
        self.append_texture(arcade.load_texture("plants/pea1.png"))
        self.append_texture(arcade.load_texture("plants/pea2.png"))
        self.append_texture(arcade.load_texture("plants/pea3.png"))
        self.window = window
        self.last_shot_time = time.time()
    def update(self):
        if self.health > 0:
            current_time = time.time()
            if current_time - self.last_shot_time >= 3:
                new_bul = objects.Bul(self.right, self.top)
                self.window.buls_object.append(new_bul)  
                self.last_shot_time = current_time  