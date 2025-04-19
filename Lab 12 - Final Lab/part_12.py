import arcade
import random

""" First of all, set some base variables """
movement_speed = 3
zombie_speed = 1
player_scaling = 0.2
zombie_scaling = 0.2
initial_zombie_count = 3
initial_zombie_health = 20
round_number = 1

screen_width = 800
screen_height = 600

class Player:
    def __init__(self, x, y, health, points):
        self.x = x
        self.y = y
        self.health = 100
        self.points = 0

class Zombie:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = initial_zombie_health
        self.zombie_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_walk_0.png", zombie_scaling)
        self.zombie_sprite.center_x = x
        self.zombie_sprite.center_y = y

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, "COD: Zombies ripoff")

        """ Sprite Lists """
        self.player_list = None
        self.zombie_list = None
        self.wall_list = None
        self.gun_list = None

        self.physics_engine = None

        self.camera_for_sprites = arcade.Camera(screen_width, screen_height)
        self.camera_for_gui = arcade.Camera(screen_width, screen_height)

    def setup(self):
        arcade.set_background_color(arcade.color.FOREST_GREEN)

        """ Now make the sprite lists exist """
        self.player_list = arcade.SpriteList()
        self.zombie_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gun_list = arcade.SpriteList()



        """ Draw Zombies """
        for i in range(initial_zombie_count + 2 * round_number):  # add 2 zombies per round
            zombie = Zombie(50, 50, initial_zombie_health + 15 * round_number)  # All zombies gain 15
                                                                                      # health per round
            self.zombie_list.append(zombie)



