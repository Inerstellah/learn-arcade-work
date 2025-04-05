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

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5
JERRY_MOVEMENT_SPEED = 8
# Jerry is very quick

class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "What Even Is This Game")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.gem_list = None
        self.special_gem_list = None
        self.jerry_list = None

        # Set up the player
        self.player_sprite = None

        # Set up Jerry
        self.jerry_sprite = arcade.Sprite("jerry.png", JERRY_SCALING)

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.squeak = arcade.load_sound("squeak.mp3")
        self.aah = arcade.load_sound("aah.wav")
        self.aaaah = arcade.load_sound("aaaah.wav")

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

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.jerry_list = arcade.SpriteList()
        self.special_gem_list = arcade.SpriteList()

        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite("CAT.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # Make some walls
        for x in range(64, 640, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 192
            if not wall.center_x % 192 == 0:
                self.wall_list.append(wall)

        # Do it again but at a diff y-coord
        for x in range(64, 640, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 384
            if not wall.center_x % 192 == 0:
                self.wall_list.append(wall)

        # One more time
        for x in range(64, 640, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 576
            if not wall.center_x % 192 == 0:
                self.wall_list.append(wall)

        # Okay again but vertically
        for y in range(64, 640, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = 704
            wall.center_y = y
            if not wall.center_y % 192 == 0:
                self.wall_list.append(wall)

        # Nvm we need more
        for y in range(-64, 768, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        # Yeah, world barriers are probably necessary...
        for x in range (0, 768, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = -64
            self.wall_list.append(wall)

        # Build a great wall
        for y in range(-64, 768, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = 832
            wall.center_y = y
            self.wall_list.append(wall)

        # And another
        for x in range(0, 896, 64):
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

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Create the gems
        for i in range(GEM_COUNT):
            # Create the gem objects
            gem = arcade.Sprite("real-rock.png", GEM_SCALING)

            # Boolean variable if we successfully placed the gem
            gem_placed_successfully = False

            # Keep trying until success
            while not gem_placed_successfully:
                # Position the gem
                gem.center_x = random.randrange(SCREEN_WIDTH)
                gem.center_y = random.randrange(SCREEN_HEIGHT)

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
                jerry.center_x = random.randrange(SCREEN_WIDTH)
                jerry.center_y = random.randrange(SCREEN_HEIGHT)

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

        # Select the (unscrolled) camera for our GUI
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)
        arcade.draw_text("X: " + str(round(self.player_sprite.center_x)),
                         730, 30, arcade.color.WHITE, 14)
        arcade.draw_text("Y: " + str(round(self.player_sprite.center_y)),
                         730, 10, arcade.color.WHITE, 14)
        arcade.draw_text("Hit R to restart", 320, 10, arcade.color.WHITE, 22)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the window to the player.
        #
        # If CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        # Anything between 0 and 1 will have the camera move to the location with a smoother
        # pan.
        CAMERA_SPEED = 0.5
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

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

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