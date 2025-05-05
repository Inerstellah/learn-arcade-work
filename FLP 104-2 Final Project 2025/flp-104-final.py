import arcade
from arcade import AnimationKeyframe

screen_width = 768
screen_height = 640
camera_speed = 0.85
movement_speed = 3.5
icon_scaling = 1 / 16

class Player:
    def __init__(self):
        self.player_sprite = arcade.AnimatedTimeBasedSprite(scale=0.65)

        self.idle_texture = arcade.load_texture(":resources:images/animated_characters/male_person/malePerson_idle.png")

        self.walking_textures = []
        for i in range(8):
            texture_path = f":resources:images/animated_characters/male_person/malePerson_walk{i}.png"
            texture = arcade.load_texture(texture_path)
            keyframe = AnimationKeyframe(i, 125, texture)  # 125 ms = 0.125 seconds per frame
            self.walking_textures.append(keyframe)

        self.player_sprite.texture = self.idle_texture
        self.is_walking = False

    def update(self, delta_time):
        if self.is_walking:
            self.player_sprite.frames = self.walking_textures  # Switch to walking frames
            self.player_sprite.update_animation(delta_time)
        else:
            self.player_sprite.texture = self.idle_texture  # Default to idle texture


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, "FLP 104-2 Final Project Spring 2025")

        self.player_list = arcade.SpriteList()
        self.icon_list = arcade.SpriteList()

        self.player_sprite = None
        self.physics_engine = None

        self.camera_for_sprites = arcade.Camera(screen_width, screen_height)
        self.camera_for_gui = arcade.Camera(screen_width, screen_height)


    def setup(self):
        arcade.set_background_color(arcade.color.FOREST_GREEN)

        self.player_list = arcade.SpriteList()

        # Create the player
        self.player_sprite = Player()
        self.player_list.append(self.player_sprite.player_sprite)

        # Make it so player can move and doesn't phase through stuff and move
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite.player_sprite, self.icon_list)

        # Create icon objects
        icon = arcade.Sprite("info_icon.png", icon_scaling)
        icon.center_x = 50
        icon_center_y = 50
        self.icon_list.append(icon)


    def on_draw(self):
        arcade.start_render()
        self.camera_for_sprites.use()

        self.player_list.draw()
        self.icon_list.draw()

        self.camera_for_gui.use()


    def on_update(self, delta_time):
        self.physics_engine.update()
        self.player_sprite.update(delta_time)

        lower_left_corner = (self.player_sprite.player_sprite.center_x - self.width / 2,
                             self.player_sprite.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, camera_speed)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.player_sprite.change_y = movement_speed
            self.player_sprite.is_walking = True
        elif key == arcade.key.A:
            self.player_sprite.player_sprite.change_x = -movement_speed
            self.player_sprite.is_walking = True
        elif key == arcade.key.S:
            self.player_sprite.player_sprite.change_y = -movement_speed
            self.player_sprite.is_walking = True
        elif key == arcade.key.D:
            self.player_sprite.player_sprite.change_x = movement_speed
            self.player_sprite.is_walking = True
        elif key == arcade.key.SPACE:
            arcade.close_window()


    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.player_sprite.change_x = 0

        if not (self.player_sprite.player_sprite.change_x or self.player_sprite.player_sprite.change_y):
            self.player_sprite.is_walking = False


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()