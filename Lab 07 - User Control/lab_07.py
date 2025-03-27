import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SPRITE_SCALING_CRAB = 0.05
SPRITE_SCALING_SEASHELL = 0.05
MOVEMENT_SPEED = 3

class Crab:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.dx = dx
        self.y = y
        self.dy = dy
        self.player_sprite = arcade.Sprite("crab.png", SPRITE_SCALING_CRAB)
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

class Seashell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player_sprite = arcade.Sprite("seashell.png", SPRITE_SCALING_SEASHELL)
        self.player_sprite.center_x = self.x
        self.player_sprite.center_y = self.y
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.crab = Crab(180, 180, 0, 0)
        self.seashell = Seashell(200, 200)
        self.beach_ball_x = 520
        self.beach_ball_y = 550
        self.beach_ball_dx = 1
        self.beach_ball_dy = 1

        self.set_mouse_visible(False)

        self.bump_sound = arcade.load_sound("hurt2.wav")  # load bump sound
        self.bump_sound_player = None  # keep track of whether it's playing

        self.click_sound = arcade.load_sound("on_click.mp3")

    def on_draw(self):
        """ Draw everything here """
        arcade.start_render()
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)

        # Draw the background
        arcade.draw_lrtb_rectangle_filled(0, 799, 375, 0, arcade.csscolor.SANDY_BROWN)
        arcade.draw_lrtb_rectangle_filled(0, 799, 599, 375, arcade.csscolor.DARK_BLUE)

        # Draw the beach ball
        self.draw_beach_ball(self.beach_ball_x, self.beach_ball_y)

        # Move the beach ball
        self.beach_ball_x += self.beach_ball_dx
        if self.beach_ball_x >= 560 or self.beach_ball_x <= 520:
            self.beach_ball_dx *= -1

        self.beach_ball_y += self.beach_ball_dy
        if self.beach_ball_y >= 570 or self.beach_ball_y <= 550:
            self.beach_ball_dy *= -1
        # draw people
        self.draw_person(400, 400, 400, 380)
        self.draw_person(300, 400, 300, 380)
        self.draw_person(500, 500, 500, 480)
        self.draw_person(570, 500, 570, 480)
        self.draw_person(155, 330, 155, 310)

        self.draw_sun()
        self.draw_umbrella(100, 225)
        self.draw_umbrella(600, 170)

        arcade.draw_circle_filled(720, 720, 40, arcade.csscolor.YELLOW)  # Draws the sun

        arcade.draw_polygon_filled(
            ((322, 310), (332, 355), (362, 355), (372, 310)),
            arcade.csscolor.SADDLE_BROWN
        )

        self.crab.player_list.draw()
        self.seashell.player_list.draw()

        arcade.draw_text("Press Space to close", 250, 30, arcade.color.BLACK, 12)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.W and self.crab.y < SCREEN_HEIGHT:
            self.crab.dy = MOVEMENT_SPEED
        if key == arcade.key.S and self.crab.y > 25:
            self.crab.dy = -MOVEMENT_SPEED
        if key == arcade.key.A and -10 < SCREEN_WIDTH:
            self.crab.dx = -MOVEMENT_SPEED
        if key == arcade.key.D and self.crab.y > 25:
            self.crab.dx = MOVEMENT_SPEED
        if key == arcade.key.SPACE:
            arcade.close_window()


    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.crab.dy = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.crab.dx = 0

    def on_update(self, delta_time):
        self.crab.x += self.crab.dx
        self.crab.y += self.crab.dy

        if self.crab.y >= SCREEN_HEIGHT - 25 or self.crab.y <= 25:
            if not self.bump_sound_player:
                self.bump_sound_player = arcade.play_sound(self.bump_sound)
        elif self.crab.x >= SCREEN_WIDTH - 25 or self.crab.x <= 25:
            if not self.bump_sound_player:
                self.bump_sound_player = arcade.play_sound(self.bump_sound)
        else:
            self.bump_sound_player = None

        self.crab.x = max(25, min(self.crab.x, SCREEN_WIDTH - 25))
        self.crab.y = max(25, min(self.crab.y, SCREEN_HEIGHT - 25))

        self.crab.player_sprite.center_x = self.crab.x
        self.crab.player_sprite.center_y = self.crab.y

    def on_mouse_motion(self, x, y, dx, dy):
        self.seashell.x = x
        self.seashell.y = y
        self.seashell.player_sprite.center_x = self.seashell.x
        self.seashell.player_sprite.center_y = self.seashell.y

    def on_mouse_press(self, x, y, button, modifiers):
        arcade.play_sound(self.click_sound)

    def draw_beach_ball(self, x, y):
        """ Draws the beach ball """
        arcade.draw_circle_filled(x, y, 23, arcade.csscolor.ORANGE)

    def draw_umbrella(self, x, y):
        """ Draws an umbrella """
        arcade.draw_line(x, y, x + 30, y + 170, arcade.csscolor.WHITE, 4)
        arcade.draw_parabola_filled(x - 66, y + 120, x + 130, 50, arcade.csscolor.GOLD, 350)
        arcade.draw_polygon_filled(
            ((x - 80, y), (x - 50, y + 65), (x, y + 65), (x - 30, y)),
            arcade.csscolor.LIME_GREEN
        )

    def draw_person(self, x1, y1, x2, y2):
        """ Draws a person """
        self.draw_head(x1, y1, x1 - 5, y1 + 5)
        self.draw_body(x2, y2)

    def draw_head(self, x1, y1, x2, y2):
        """ Draws the head of the person """
        arcade.draw_circle_filled(x1, y1, 20, arcade.csscolor.PEACH_PUFF)  # Head
        arcade.draw_circle_filled(x2, y2, 5, arcade.csscolor.GREEN)
        arcade.draw_circle_filled(x2 + 12, y2, 5, arcade.csscolor.GREEN)
        arcade.draw_parabola_outline(x1 - 13, y1 - 15, x1 + 13, 10, arcade.csscolor.DARK_ORANGE, 5, 180)

    def draw_body(self, x, y):
        """ Draws the body of the person """
        lines = [
            (x, y, x, y - 30),  # Torso
            (x, y - 30, x - 15, y - 60),  # Left leg
            (x, y - 30, x + 15, y - 60),  # Right leg
            (x, y - 30, x - 10, y - 10),  # Left arm
            (x, y - 30, x + 10, y - 10),  # Right arm
        ]
        for line in lines:
            arcade.draw_line(line[0], line[1], line[2], line[3], arcade.csscolor.BLACK)

    def draw_sun(self):
        """ Draws the sun with rays """
        sun_rays = [
            (720, 650, 720, 790),  # Vertical ray
            (650, 720, 790, 720),  # Horizontal ray
            (670, 670, 770, 770),  # Slope = 1
            (670, 770, 770, 670),  # Slope = -1
        ]
        for line in sun_rays:
            arcade.draw_line(line[0], line[1], line[2], line[3], arcade.csscolor.YELLOW, 4)



def main():

    window = MyGame()
    arcade.run()

main()