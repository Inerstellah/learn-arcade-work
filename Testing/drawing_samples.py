import time
import arcade

trainer_Name = input("Researcher: Welcome, Trainer! What is your name? ")

print("Researcher: Okay, nice to meet you", trainer_Name + "!")

time.sleep(1.2)

print("Researcher:", trainer_Name + ", you are about to embark on an epic quest of friendship, betrayals, "
                    "happiness, and sadness.")

time.sleep(2.5)

print("""Researcher: Let me back up... You are now part of a magic world with creatures that we call "Animons" """)

time.sleep(3)

print("Researcher: These Animons have completely changed our lives over the last few years.")

time.sleep(2.8)

print("Researcher: As a researcher, I have been trying to capture every type of Animon in the world.")

time.sleep(3.4)

print("Researcher: Starting today, you will help me fulfill my goal! Let's go!")

time.sleep(4)

print("You wake up the next morning, excited to begin your adventure")

SCREEN_WIDTH = 600
SCREEN_LENGTH = 600
WALKING_SPEED = 3

class Character:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x,
                               self.position_y,
                               self.radius,
                               self.color)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Character(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.A:
            self.ball.change_x = -WALKING_SPEED
        elif key == arcade.key.D:
            self.ball.change_x = WALKING_SPEED
        elif key == arcade.key.W:
            self.ball.change_y = WALKING_SPEED
        elif key == arcade.key.S:
            self.ball.change_y = -WALKING_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.ball.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.ball.change_y = 0


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()