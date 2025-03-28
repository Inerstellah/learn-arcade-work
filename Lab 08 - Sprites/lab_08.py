import random
import arcade

SPRITE_SCALING_PLAYER = 0.05
SPRITE_SCALING_SEASHELL = 0.04
SEASHELL_COUNT = 50
OBJECT_SPEED = 2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Really cool lab")

        # these bad boys will hold sprite lists
        self.player_list = None
        self.seashell_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.csscolor.NAVY)

    class Seashell:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.player_sprite = arcade.Sprite("seashell.png", SPRITE_SCALING_SEASHELL)
            self.player_sprite.center_x = self.x
            self.player_sprite.center_y = self.y

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.seashell_list = arcade.SpriteList()

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("crab.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the seashells
        for i in range(SEASHELL_COUNT):
            # Create the seashell instance
            seashell = arcade.Sprite("seashell.png", SPRITE_SCALING_SEASHELL)

            # Position the seashell
            seashell.center_x = random.randrange(SCREEN_WIDTH)
            seashell.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the seashell to the list
            self.seashell_list.append(seashell)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.seashell_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.seashell_list.update()

        # Generate a list of all sprites that collided with the player.
        seashells_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.seashell_list)

        for seashell in self.seashell_list:
            seashell.center_x += OBJECT_SPEED

        # Loop through each colliding sprite, remove it, and add to the score.
        for seashell in seashells_hit_list:
            seashell.remove_from_sprite_lists()
            self.score += 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
