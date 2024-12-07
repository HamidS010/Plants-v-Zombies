import arcade
import animate
import constants
import services


class Zombie(animate.Animate):
    def __init__(self, image, health, center_y,window):
        super().__init__(image, scale=0.75)
        self.health = health
        self.center_y, self.row = services.lawn_y(center_y)
        self.center_x = constants.SCREEN_WIDTH
        self.speed = 0.2
        self.dmg = 5
        self.hit_sound = arcade.load_sound("sounds/hit.mp3")
        self.grass_sound = arcade.load_sound("sounds/grasswalk.mp3")
        arcade.play_sound(self.grass_sound, 0.5)
        self.window = window

    def update(self):
        self.center_x -= self.speed
        if self.health <= 0:
            self.window.killed_zombies+=1
            self.kill()
        hit_list = arcade.check_for_collision_with_list(self,self.window.buls_object)
        if hit_list:
            for bul in hit_list:
                self.health -= bul.damage
                bul.kill()
                arcade.play_sound(self.hit_sound,0.5)
        hit_list_plants = arcade.check_for_collision_with_list(self,self.window.plants)
        if hit_list_plants:
            self.speed= 0
            for plant in hit_list_plants:
                plant.health -= self.dmg
                print(plant.health)
        hit_list_firebul = arcade.check_for_collision_with_list(self,self.window.firebuls_object)
        if hit_list_firebul:
            for firebul in hit_list_firebul:
                self.health -= 2
                firebul.kill()
                arcade.play_sound(self.hit_sound,0.5)

            




class OrdinaryZombie(Zombie):
    def __init__(self, center_y,window):
        super().__init__("zombies/OrdinaryZombie/Zombie_0.png", 12, center_y,window)
        for i in range(22):
            self.append_texture(
                arcade.load_texture(f"zombies/OrdinaryZombie/Zombie_{i}.png")
            )


class ConeheadZombie(Zombie):
    def __init__(self, center_y,window):
        super().__init__(
            "zombies/ConeheadZombie/ConeheadZombie_0.png", 12, center_y,window
        )
        for i in range(21):
            self.append_texture(
                arcade.load_texture(f"zombies/ConeheadZombie/ConeheadZombie_{i}.png")
            )


class BucketheadZombie(Zombie):
    def __init__(self, center_y,window):
        super().__init__(
            "zombies/BucketheadZombie/BucketheadZombie_0.png", 12, center_y,window
        )
        for i in range(15):
            self.append_texture(
                arcade.load_texture(
                    f"zombies/BucketheadZombie/BucketheadZombie_{i}.png"
                )
            )
