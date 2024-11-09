import arcade
import animate
import game


class Zombie(animate.animate):
    def __init__(self,image,health,row,center_y):
        super().__init__(image,scale=0.09)
        self.health = health
        self.row = row
        self.center_y = game.lawn_y(center_y)
        self.center_x = game.SCREEN_WIDTH
        self.speed = 0.2
    def update(self):
        self.center_x -= self.speed
        if self.health <= 0:
            self.kill()


class OrdinaryZombie(Zombie):
    def __init__(self,row, center_y):
        super().__init__("zombies/OrdinaryZombie/Zombie0.png",12,row,center_y)
        for i in range(22):
            self.append_texture(arcade.load_texture(f"zombies/OrdinaryZombie/Zombie_{i}.png"))


class ConeheadZombie(Zombie):
    def __init__(self,row, center_y):
        super().__init__("zombies/ConeheadZombie/ConeheadZombie_0.png",12,row,center_y)
        for i in range(21):
            self.append_texture(arcade.load_texture(f"zombies/ConeheadZombie/ConeheadZombie_{i}.png"))


class BucketheadZombie(Zombie):
    def __init__(self,row, center_y):
        super().__init__("zombies/BucketheadZombie/BucketheadZombie_0.png",12,row,center_y)
        for i in range(15):
            self.append_texture(arcade.load_texture(f"zombies/BucketheadZombie/BucketheadZombie_{i}.png"))    