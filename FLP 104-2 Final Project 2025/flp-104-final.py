import arcade
from arcade import AnimationKeyframe

screen_width = 768
screen_height = 640
camera_speed = 0.85
movement_speed = 3.5
icon_scaling = 1 / 16
icon_proximity = 100

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


class Icon(arcade.Sprite):
    def __init__(self, x, y, image, scale, text):
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
        self.image = image
        self.scale = scale
        self.text = text


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height,
                         "FLP 104-2 Final Project Spring 2025 - Surveillance in Education")

        self.player_list = arcade.SpriteList()
        self.icon_list = arcade.SpriteList()

        self.player_sprite = None
        self.physics_engine = None

        self.camera_for_sprites = arcade.Camera(screen_width, screen_height)
        self.camera_for_gui = arcade.Camera(screen_width, screen_height)

        self.text_to_display = ""


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
        icon = Icon(150, 100, "info_icon.png", icon_scaling,
                    "Did you know that surveillance tech has been sold to\nschools for decades? "
                    "The goal is to increase safety.\nApps such as Gaggle, Bark, and Securly have "
                    "not done\nwhat they were intended to do, and actually violated\nbasic student privacy.")
        self.icon_list.append(icon)

        icon = Icon(375, 100, "info_icon.png", icon_scaling,
                    "The best learning happens when students are autonomous,\nwhich does not happen "
                    "when they are under constant high\nsurveillance. Studies show that surveillance "
                    "pressures\nstudents to act differently than they normally would, in hopes\nof appeasing "
                    "whoever, or whatever, is watching them.")
        self.icon_list.append(icon)

        icon = Icon(600, 100, "info_icon.png", icon_scaling,
                    "To learn, students have to make mistakes. Because there\nis fear that any "
                    "mistakes could be used against them,\nstudents are scared to fully participate, "
                    "if at all, which\ndisrupts the learning process.")
        self.icon_list.append(icon)


    def on_draw(self):
        arcade.start_render()
        self.camera_for_sprites.use()

        self.player_list.draw()
        self.icon_list.draw()

        self.camera_for_gui.use()

        if self.text_to_display:
            lines = self.text_to_display.split('\n')
            start_y = 150  # Start higher on the screen so text isn't at the bottom
            for i, line in enumerate(lines):
                arcade.draw_text(line, 20, start_y - i * 25, arcade.color.WHITE, 16)

    def on_update(self, delta_time):
        self.player_sprite.player_sprite.center_x += self.player_sprite.player_sprite.change_x
        self.player_sprite.player_sprite.center_y += self.player_sprite.player_sprite.change_y

        # Check for collision
        collided = arcade.check_for_collision_with_list(self.player_sprite.player_sprite, self.icon_list)
        if collided:
            # Undo movement
            self.player_sprite.player_sprite.center_x -= self.player_sprite.player_sprite.change_x
            self.player_sprite.player_sprite.center_y -= self.player_sprite.player_sprite.change_y

        self.player_sprite.update(delta_time)

        lower_left_corner = (self.player_sprite.player_sprite.center_x - self.width / 2,
                             self.player_sprite.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, camera_speed)

        for icon in self.icon_list:
            if isinstance(icon, Icon):
                distance = arcade.get_distance_between_sprites(self.player_sprite.player_sprite, icon)
                if distance <= icon_proximity:
                    self.text_to_display = icon.text
                    break
                else:
                    self.text_to_display = ""


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
