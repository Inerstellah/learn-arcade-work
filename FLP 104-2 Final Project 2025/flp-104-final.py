import arcade
from arcade import AnimationKeyframe
import webbrowser

screen_width = 1024
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
    def __init__(self, x, y, image, scale, text, kind):
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
        self.image = image
        self.scale = scale
        self.text = text
        self.kind = kind


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

        self.is_touching_links_icon = False


    def setup(self):
        arcade.set_background_color(arcade.color.NAVY_PURPLE)

        self.player_list = arcade.SpriteList()

        # Create the player
        self.player_sprite = Player()
        self.player_list.append(self.player_sprite.player_sprite)

        # Make it so player can move and doesn't phase through stuff and move
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite.player_sprite, self.icon_list)

        # Create icon objects
        icon = Icon(150, 100, "info_icon.png", icon_scaling,
                    "Did you know that surveillance tech has been sold to\n"
                    "schools for decades? The goal is to increase safety.\n"
                    "Apps such as Gaggle, Bark, and Securly have not done\n"
                    "what they were intended to do, and actually violated\n"
                    "basic student privacy.", 1)
        self.icon_list.append(icon)

        icon = Icon(375, 100, "info_icon.png", icon_scaling,
                    "The best learning happens when students are autonomous,\n"
                    "which does not happen when they are under constant high\n"
                    "surveillance. Studies show that surveillance pressures\n"
                    "students to act differently than they normally would, in hopes\n"
                    "of appeasing whoever, or whatever, is watching them.", 1)
        self.icon_list.append(icon)

        icon = Icon(600, 100, "info_icon.png", icon_scaling,
                    "To learn, students have to make mistakes. However,\n"
                    "because there is fear that any mistakes could be used\n"
                    "against them, students are scared to fully participate, if\n"
                    "at all, which disrupts the learning process.", 1)
        self.icon_list.append(icon)

        icon = Icon(600, -200, "info_icon.png", icon_scaling,
                    "Surveillance in general has been an issue since at least the\n"
                    "1850's, where the Pinkerton National Detective Agency would spy\n"
                    "on any organized labor. Later, in 1870, the U.S. Justice Department\n"
                    "was established and they would often contract with these private\n"
                    "detective firms.", 1)
        self.icon_list.append(icon)

        icon = Icon(375, -200, "info_icon.png", icon_scaling,
                    "Critics point out that the main goal of personalized learning\n"
                    "and EdTech, a 'global research partnership' is to rid of public\n"
                    "education and to replace it with a financialized authoritarian\n"
                    "system. In this system, education would be run privately, but a\n"
                    "state subsidized part of Big Data. This education model has no\n"
                    "human interaction, which is a huge part in children learning\n"
                    "effectively, and instead has children sitting in front of screens.", 1)
        self.icon_list.append(icon)

        icon = Icon(150, -200, "info_icon.png", icon_scaling,
                    "In order for this 'personalized learning' to function\n"
                    "properly, data from all students would have to be collected\n"
                    "and used. At scale, this seems like a huge crime - collecting\n"
                    "data from millions of kids. It can be misleading because it\n"
                    "promises that everyone will reach a 'mastery level' and has\n"
                    "the illusion of freedom. Of course, personalized learning is\n"
                    "all about control and conditioning.", 1)
        self.icon_list.append(icon)

        icon = Icon(150, -500, "info_icon.png", icon_scaling,
                    "While it makes sense to collect some children's educational\n"
                    "data, so as to see how they are doing, teachers and even schools\n"
                    "admit that they don't know what else happens to the data that they\n"
                    "collect about their students.", 1)
        self.icon_list.append(icon)

        icon = Icon(375, -500, "info_icon.png", icon_scaling,
                    "A common app teachers use is GoGuardian, a parental app that\n"
                    "allows the controller to see the screens of every student. It\n"
                    "greatly oversimplifies student behavior though, leaving only\n"
                    "statistics in numbers of each student without context.", 1)
        self.icon_list.append(icon)

        icon = Icon(600, -500, "info_icon.png", icon_scaling,
                    "For example, I could say that if you've only been in this game\n"
                    "for a minute, you probably didn't read everything. Or, if you have\n"
                    "been in this game for 15 minutes then you probably have been side\n"
                    "tracked. Of course, I can't be for certain what you have really\n"
                    "been doing just by looking at how long you've been in the game for.", 1)
        self.icon_list.append(icon)

        icon = Icon(600, -800, "info_icon.png", icon_scaling,
                    "Dr. Hillman, a researched at the London School for Economics, said\n"
                    "'stronger regulation is essential to protect students and ensure that\n"
                    "technology supports their learning without compromising their privacy\n"
                    "or wellbeing. We must prioritise children's interests on safeguard their\n"
                    "future in a safe and ethical way, in an increasingly digitised school\n"
                    "environment.'", 1)
        self.icon_list.append(icon)

        icon = Icon(1145, -800, "info_icon.png", icon_scaling,
                    "I personally think that surveillance in education is a less than\n"
                    "ideal thing. I believe that collecting the data of children is\n"
                    "morally wrong, especially when they don't know what's happening.\n"
                    "Some may say 'oh, so we'll just ask if it's okay' but I don't\n"
                    "think that's a good idea either because most children wouldn't\n"
                    "fully understand what data collection really is.", 1)
        self.icon_list.append(icon)

        icon = Icon(1370, -800, "info_icon.png", icon_scaling,
                    "Artificial intelligence may also improperly interpret the\n"
                    "data that it collects. We have seen examples of what AI\n"
                    "thinks about when collecting data, like how likely that\n"
                    "person is to skip school. It has also incorrectly identified\n"
                    "people as criminals, and they get sent to jail for something\n"
                    "that they never did. This being said, I don't think AI should\n"
                    "be used in education to collect children's data - teachers\n"
                    "should just be more attentive to their students.", 1)
        self.icon_list.append(icon)

        icon = Icon(1370, -1025, "info_icon.png", icon_scaling,
                    "Sources:\n"
                    "www.teenvogue.com - Press 1 to open\n"
                    "www.newswise.com - Press 2 to open\n"
                    "www.dissidentvoice.org - Press 3 to open\n"
                    "www.hackeducation.com - Press 4 to open\n"
                    "Chapter of 'Four Surveillance Technologies Creating... - Press 5 to open", 2)
        self.icon_list.append(icon)


    def on_draw(self):
        arcade.start_render()

        arcade.start_render()

        arcade.draw_text("W - up", 50, 570, arcade.color.WHITE, 20)
        arcade.draw_text("A - left", 56, 540, arcade.color.WHITE, 20)
        arcade.draw_text("S - down", 55, 510, arcade.color.WHITE, 20)
        arcade.draw_text("D - right", 54, 480, arcade.color.WHITE, 20)

        arcade.draw_text("Get close to an icon to learn about surveillance in education!",
                         23, 610, arcade.color.WHITE,20)

        self.camera_for_sprites.use()

        self.player_list.draw()
        self.icon_list.draw()

        #  Horizontal
        arcade.draw_line(200, 100, 325, 100, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(425, 100, 550, 100, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(200, -200, 325, -200, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(425, -200, 550, -200, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(200, -500, 325, -500, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(425, -500, 550, -500, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(650, -800, 775, -800, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(965, -800, 1090, -800, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(1195, -800, 1315, -800, arcade.csscolor.DARK_RED, 4)

        #  Vertical
        arcade.draw_line(600, 50, 600, -150, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(150, -250, 150, -450, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(600, -550, 600, -750, arcade.csscolor.DARK_RED, 4)
        arcade.draw_line(1370, -850, 1370, -975, arcade.csscolor.DARK_RED, 4)

        arcade.draw_text("My opinion?", 800, -807, arcade.csscolor.BLACK, 20)

        self.camera_for_gui.use()

        if self.text_to_display:  # ChatGPT wrote this part
            lines = self.text_to_display.split('\n')
            start_y = 175  # Start higher on the screen so text isn't at the bottom
            for i, line in enumerate(lines):
                arcade.draw_text(line, 20, start_y - i * 25, arcade.color.WHITE, 16)


    def on_update(self, delta_time):
        self.physics_engine.update()

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
                    if icon.kind == 2:
                        self.is_touching_links_icon = True
                    else:
                        self.is_touching_links_icon = False
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
        elif key == arcade.key.KEY_1 and self.is_touching_links_icon:
            webbrowser.open("www.teenvogue.com/story/surveillance-education-spying-technology-schools")
        elif key == arcade.key.KEY_2 and self.is_touching_links_icon:
            webbrowser.open("www.newswise.com/articles/classrooms-under-surveillance")
        elif key == arcade.key.KEY_3 and self.is_touching_links_icon:
            webbrowser.open("dissidentvoice.org/2016/10/education-technology-"
                            "surveillance-and-americas-authoritarian-democracy")
        elif key == arcade.key.KEY_4 and self.is_touching_links_icon:
            webbrowser.open("hackeducation.com/2019/08/28/surveillance-ed-tech")
        elif key == arcade.key.KEY_5 and self.is_touching_links_icon:
            webbrowser.open("https://doi.org/10.1007/978-3-031-09687-7_19")
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