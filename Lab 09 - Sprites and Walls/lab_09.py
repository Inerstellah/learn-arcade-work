""" Sprite Sample Program """

import arcade
import random

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.15
GEM_SCALING = 0.4
JERRY_SCALING = 0.013
GEM_COUNT = 15
JERRY_COUNT = 10
KEY_SCALING = 0.4
KEY_TEXT = ""

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 1


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "What Even Is This Game")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.green_wall_list = None
        self.red_wall_list = None
        self.green_wall_list = None
        self.blue_wall_list = None
        self.yellow_wall_list = None
        self.gem_list = None
        self.special_gem_list = None
        self.jerry_list = None
        self.blue_key_list = None
        self.red_key_list = None
        self.green_key_list = None
        self.yellow_key_list = None
        self.collected_keys_list = None


        # Set up the player
        self.player_sprite = None

        # Set up Jerry
        self.jerry_sprite = arcade.Sprite("jerry.png", JERRY_SCALING)

        # This variable holds our simple "physics engine"
        self.physics_engine = None
        self.physics_engine_green = None
        self.physics_engine_blue = None
        self.physics_engine_red = None
        self.physics_engine_yellow = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.squeak = arcade.load_sound("squeak.mp3")
        self.aah = arcade.load_sound("aah.wav")
        self.aaaah = arcade.load_sound("aaaah.wav")
        self.coin_sound = arcade.load_sound("coin2.wav")

        # Booleans to see if player has a key
        self.has_blue_key = False
        self.has_red_key = False
        self.has_green_key = False
        self.has_yellow_key = False

    class Gem:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.gem_sprite = arcade.Sprite("real-rock.png", GEM_SCALING)
            self.gem_sprite.center_x = self.x

    class Jerry:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.jerry_sprite = arcade.Sprite("jerry.png", JERRY_SCALING)
            self.jerry_sprite.center_x = self.x
            self.jerry_sprite.center_y = self.y

    class BlueKey:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.key_sprite = "It literally doesn't matter cause it gets set when it's created"
            self.key_sprite.center_x = self.x
            self.key_sprite.center_y = self.y


    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.jerry_list = arcade.SpriteList()
        self.special_gem_list = arcade.SpriteList()
        self.blue_key_list = arcade.SpriteList()
        self.red_key_list = arcade.SpriteList()
        self.green_key_list = arcade.SpriteList()
        self.yellow_key_list = arcade.SpriteList()
        self.collected_keys_list = arcade.SpriteList()
        self.blue_wall_list = arcade.SpriteList()
        self.red_wall_list = arcade.SpriteList()
        self.green_wall_list = arcade.SpriteList()
        self.yellow_wall_list = arcade.SpriteList()
        self.green_wall_list = arcade.SpriteList()


        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite("CAT.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 0
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Make some walls
        for i in range(3):
            for x in range(64, 640, 64):
                wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
                wall.center_x = x
                wall.center_y = 192 * i + 64
                if not wall.center_x % 192 == 0:
                    self.wall_list.append(wall)

        # Okay again but vertically
        for y in range(64, 640, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = 704
            wall.center_y = y
            if not wall.center_y % 192 == 0:
                self.wall_list.append(wall)

        # Tall wall on the very left
        for y in range(-64, 768, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = -512
            wall.center_y = y
            self.wall_list.append(wall)

        # Long wall on the very bottom
        for x in range (-512, 1024, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = -64
            self.wall_list.append(wall)

        # Build a great wall on the very right
        for y in range(-64, 768, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = 1088
            wall.center_y = y
            self.wall_list.append(wall)

        # Long wall on very top
        for x in range(-512, 1152, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 768
            self.wall_list.append(wall)

        # Now draw an arrow that points to the easter egg
        for x in range(960, 1334, 64):
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = -512
            self.wall_list.append(wall)

        # Manually place the diagonals cause I'm lazy
        coordinate_list = [(1216, -448),
                           (1152, -384),
                           (1216, -576),
                           (1152, -640)]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Then make another arrow
        for y in range(-576, -192, 64):
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING_BOX)
            wall.center_x = 2880
            wall.center_y = y
            self.wall_list.append(wall)

        # Using specific coordinates again yay!
        coordinate_list_2 = [(2816, -320),
                             (2752, -384),
                             (2944, -320),
                             (3008, -384)]

        # Then actually use the coords (again)
        for coordinate in coordinate_list_2:
            wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Two more set of walls teehee
        for i in range(2):
            for j in range(3):
                for y in range(64, 864, 160):
                    wall = arcade.Sprite("brickGrey.png", SPRITE_SCALING_BOX)
                    wall.center_x = (j * 64 + 768) - i * 1024
                    wall.center_y = y
                    self.wall_list.append(wall)

        # Now draw all the colored walls
        # Green walls:
        for i in range(2):
            for y in range(0, 960, 64):
                green_wall = arcade.Sprite("greenBoxCrate_double.png", SPRITE_SCALING_BOX * 2)
                green_wall.center_x = 2560 + i * 960
                green_wall.center_y = y
                self.green_wall_list.append(green_wall)
        for i in range(2):
            for x in range(2624, 3520, 64):
                green_wall = arcade.Sprite("greenBoxCrate_double.png", SPRITE_SCALING_BOX * 2)
                green_wall.center_x = x
                green_wall.center_y = i * 896
                self.green_wall_list.append(green_wall)

        # Blue walls:
        for i in range(2):
            for y in range(64, 896, 64):
                blue_wall = arcade.Sprite("blueBoxCrate_double.png", SPRITE_SCALING_BOX * 2)
                blue_wall.center_x = 2624 + i * 832
                blue_wall.center_y = y
                self.blue_wall_list.append(blue_wall)
        for i in range(2):
            for x in range(2688, 3456, 64):
                blue_wall = arcade.Sprite("blueBoxCrate_double.png", SPRITE_SCALING_BOX * 2)
                blue_wall.center_x = x
                blue_wall.center_y = 64 + i * 768
                self.blue_wall_list.append(blue_wall)

        # Red walls
        for i in range(2):
            for y in range(128, 832, 64):
                red_wall = arcade.Sprite("redBoxCrate_double.png", SPRITE_SCALING_BOX * 2)
                red_wall.center_x = 2688 + i * 704
                red_wall.center_y = y
                self.red_wall_list.append(red_wall)
        for i in range(2):
            for x in range(2688, 3456, 64):
                red_wall = arcade.Sprite("redBoxCrate_double.png", SPRITE_SCALING_BOX * 2)
                red_wall.center_x = x
                red_wall.center_y = 128 + i * 640
                self.red_wall_list.append(red_wall)

        # Yellow walls
        for i in range(2):
            for y in range(192, 768, 64):
                yellow_wall = arcade.Sprite("yellowBoxCrate_double.png", SPRITE_SCALING_BOX * 2)
                yellow_wall.center_x = 2752 + i * 576
                yellow_wall.center_y = y
                self.yellow_wall_list.append(yellow_wall)
        for i in range(2):
            for x in range(2752, 3392, 64):
                yellow_wall = arcade.Sprite("yellowBoxCrate_double.png", SPRITE_SCALING_BOX * 2)
                yellow_wall.center_x = x
                yellow_wall.center_y = 192 + i * 512
                self.yellow_wall_list.append(yellow_wall)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        self.physics_engine_green = arcade.PhysicsEngineSimple(self.player_sprite, self.green_wall_list)
        self.physics_engine_blue = arcade.PhysicsEngineSimple(self.player_sprite, self.blue_wall_list)
        self.physics_engine_red = arcade.PhysicsEngineSimple(self.player_sprite, self.red_wall_list)
        self.physics_engine_yellow = arcade.PhysicsEngineSimple(self.player_sprite, self.yellow_wall_list)
        # Create the gems
        for i in range(GEM_COUNT):
            # Create the gem objects
            gem = arcade.Sprite("real-rock.png", GEM_SCALING)

            # Boolean variable if we successfully placed the gem
            gem_placed_successfully = False

            # Keep trying until success
            while not gem_placed_successfully:
                # Position the gem
                gem.center_x = random.randrange(-500, SCREEN_WIDTH + 200)
                gem.center_y = random.randrange(SCREEN_HEIGHT + 80)

                # See if the gem is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)

                # See if the gem is hitting another gem
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                # See if the gem is hitting the player
                gem_hits_list = arcade.check_for_collision_with_list(gem, self.player_list)

                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0 and len(gem_hits_list) == 0:
                    # It is!
                    gem_placed_successfully = True

            # Add the gem to the list
            self.gem_list.append(gem)

        # Make a special gem far to the right
        gem = arcade.Sprite("real-rock.png", 3)
        gem.center_x = 3100
        gem.center_y = 300
        self.special_gem_list.append(gem)

        # Now draw some mice, because Sidney wanted mice
        for i in range(JERRY_COUNT):
            # Create the jerrys
            jerry = arcade.Sprite("jerry.png", JERRY_SCALING)

            jerry_placed_successfully = False

            while not jerry_placed_successfully:
                # Position jerry
                jerry.center_x = random.randrange(-500, SCREEN_WIDTH + 200)
                jerry.center_y = random.randrange(SCREEN_HEIGHT + 80)

                # Check if jerry is hitting a wall
                jerry_wall_hit_list = arcade.check_for_collision_with_list(jerry, self.wall_list)

                # Check if jerry is hitting a gem
                jerry_gem_hit_list = arcade.check_for_collision_with_list(jerry, self.gem_list)

                # Check is jerry is hitting another jerry
                jerry_jerry_hit_list = arcade.check_for_collision_with_list(jerry, self.jerry_list)

                # Check if jerry is hitting a player
                jerry_player_hit_list = arcade.check_for_collision_with_list(jerry, self.player_list)

                if (len(jerry_wall_hit_list) == 0 and len(jerry_gem_hit_list) == 0 and
                        len(jerry_jerry_hit_list) == 0 and len(jerry_player_hit_list) == 0):
                    jerry_placed_successfully = True

            # Add jerry the list
            self.jerry_list.append(jerry)

        # Now make the keys that we need and append them to their respective list
        blue_key = arcade.Sprite("keyBlue.png", KEY_SCALING)
        blue_key.center_x = -576
        blue_key.center_y = 768
        self.blue_key_list.append(blue_key)
        red_key = arcade.Sprite("keyRed.png", KEY_SCALING)
        red_key.center_x = 832
        red_key.center_y = 128
        self.red_key_list.append(red_key)
        green_key = arcade.Sprite("keyGreen.png", KEY_SCALING)
        green_key.center_x = -448
        green_key.center_y = 504
        self.green_key_list.append(green_key)
        yellow_key = arcade.Sprite("keyYellow.png", KEY_SCALING)
        yellow_key.center_x = 3008
        yellow_key.center_y = -576
        self.yellow_key_list.append(yellow_key)


    def on_draw(self):
        arcade.start_render()

        # Select the scrolled camera for our sprites
        self.camera_for_sprites.use()

        # Draw the sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.gem_list.draw()
        self.special_gem_list.draw()
        self.jerry_list.draw()
        self.blue_key_list.draw()
        self.red_key_list.draw()
        self.green_key_list.draw()
        self.yellow_key_list.draw()
        self.green_wall_list.draw()
        self.blue_wall_list.draw()
        self.red_wall_list.draw()
        self.yellow_wall_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)
        arcade.draw_text("X: " + str(round(self.player_sprite.center_x)),
                         730, 30, arcade.color.WHITE, 14)
        arcade.draw_text("Y: " + str(round(self.player_sprite.center_y)),
                         730, 10, arcade.color.WHITE, 14)
        arcade.draw_text("Hit R to restart", 320, 10, arcade.color.WHITE, 22)
        arcade.draw_text(KEY_TEXT, 210, 50, arcade.color.WHITE, 22)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.physics_engine_green.update()
        self.physics_engine_blue.update()
        self.physics_engine_red.update()
        self.physics_engine_yellow.update()

        # Scroll the window to the player.
        #
        # If CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        # Anything between 0 and 1 will have the camera move to the location with a smoother
        # pan.
        CAMERA_SPEED = 1
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

        gems_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.gem_list)

        jerry_players_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.jerry_list)

        special_gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.special_gem_list)

        for gem in gems_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.aah)

        for jerry in jerry_players_hit_list:
            jerry.remove_from_sprite_lists()
            self.score += 2
            arcade.play_sound(self.squeak)

        for special_gem in special_gem_hit_list:
            special_gem.remove_from_sprite_lists()
            self.score += 5
            arcade.play_sound(self.aaaah)

        global KEY_TEXT
        if arcade.check_for_collision_with_list(self.player_sprite, self.blue_key_list):
            KEY_TEXT = "Press E to pick up the Blue Key"
        elif arcade.check_for_collision_with_list(self.player_sprite, self.red_key_list):
            KEY_TEXT = "Press E to pick up the Red Key"
        elif arcade.check_for_collision_with_list(self.player_sprite, self.green_key_list):
            KEY_TEXT = "Press E to pick up the Green Key"
        elif arcade.check_for_collision_with_list(self.player_sprite, self.yellow_key_list):
            KEY_TEXT = "Press E to pick up the Yellow Key"
        else:
            KEY_TEXT = ""

        # Test for keys to remove walls
        if self.has_green_key:
            for green_wall in self.green_wall_list:
                green_wall.remove_from_sprite_lists()
        if self.has_blue_key:
            for blue_wall in self.blue_wall_list:
                blue_wall.remove_from_sprite_lists()
        if self.has_red_key:
            for red_wall in self.red_wall_list:
                red_wall.remove_from_sprite_lists()
        if self.has_yellow_key:
            for yellow_wall in self.yellow_wall_list:
                yellow_wall.remove_from_sprite_lists()

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed. """

        if key == arcade.key.W:
            if self.score >= 35:
                self.player_sprite.change_y = MOVEMENT_SPEED * 2
            else:
                self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            if self.score >= 35:
                self.player_sprite.change_y = -MOVEMENT_SPEED * 2
            else:
                self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            if self.score >= 35:
                self.player_sprite.change_x = -MOVEMENT_SPEED * 2
            else:
                self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            if self.score >= 35:
                self.player_sprite.change_x = MOVEMENT_SPEED * 2
            else:
                self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            arcade.close_window()
        elif key == arcade.key.R:
            self.setup()
        elif key == arcade.key.E:
            if arcade.check_for_collision_with_list(self.player_sprite, self.blue_key_list):
                self.has_blue_key = True
                arcade.play_sound(self.coin_sound)
                for blue_key in self.blue_key_list:
                    blue_key.remove_from_sprite_lists()
            elif arcade.check_for_collision_with_list(self.player_sprite, self.red_key_list):
                self.has_red_key = True
                arcade.play_sound(self.coin_sound)
                for red_key in self.red_key_list:
                    red_key.remove_from_sprite_lists()
            elif arcade.check_for_collision_with_list(self.player_sprite, self.green_key_list):
                self.has_green_key = True
                arcade.play_sound(self.coin_sound)
                for green_key in self.green_key_list:
                    green_key.remove_from_sprite_lists()
            elif arcade.check_for_collision_with_list(self.player_sprite, self.yellow_key_list):
                self.has_yellow_key = True
                arcade.play_sound(self.coin_sound)
                for yellow_key in self.yellow_key_list:
                    yellow_key.remove_from_sprite_lists()

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key. """

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()