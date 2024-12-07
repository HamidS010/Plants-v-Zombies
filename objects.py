import arcade

SPEED = 1


class Sun(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__("items/sun.png", 0.12)
        self.center_x = center_x
        self.center_y = center_y

    def update(self):
        self.angle += SPEED


class Bul(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__("items/bul.png", 0.12)
        self.center_x = center_x
        self.center_y = center_y
        self.damage = 1

    def update(self):
        self.center_x += SPEED


class Firebul(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__("items/bul.png", 0.12)
        self.center_x = center_x
        self.center_y = center_y

    def update(self):
        self.center_x += SPEED
