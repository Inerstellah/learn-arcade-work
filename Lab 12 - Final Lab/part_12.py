import arcade
from arcade import AnimationKeyframe
import random
import math

"""Change PNG files on lines 174 and 178"""

# Base variables
movement_speed = 3
player_scaling = 0.65
zombie_scaling = 0.65
initial_zombie_count = 3
initial_zombie_health = 20
round_number = 1
upgrade_station_proximity = 100

camera_speed = 0.9
screen_width = 920
screen_height = 680

class Player:
    def __init__(self, x, y, health, max_health, points, damage):
        self.x = x
        self.y = y
        self.health = 100
        self.max_health = 100
        self.points = 500
        self.damage = 10
        self.player_sprite = arcade.AnimatedTimeBasedSprite(scale=player_scaling)

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


class Zombie:
    def __init__(self, x, y, health, speed):
        self.x = x
        self.y = y
        self.zombie_health = health
        self.speed = speed
        self.zombie_sprite = arcade.AnimatedTimeBasedSprite(scale=zombie_scaling)
        self.zombie_sprite.center_x = x
        self.zombie_sprite.center_y = y
        self.damage_delay = 0

        # Add animated frames properly
        for i in range(8):
            texture_path = f":resources:images/animated_characters/zombie/zombie_walk{i}.png"
            texture = arcade.load_texture(texture_path)
            keyframe = AnimationKeyframe(i, 125, texture)  # 125 ms = 0.125 seconds per frame
            self.zombie_sprite.frames.append(keyframe)

        self.zombie_sprite.texture = self.zombie_sprite.frames[0].texture


class Bullet(arcade.Sprite):
    def __init__(self, start_x, start_y, dest_x, dest_y):
        super().__init__(":resources:images/space_shooter/laserBlue01.png", 0.8)

        self.center_x = start_x
        self.center_y = start_y

        # Calculate angle to cursor
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        # Speed and direction
        bullet_speed = 10
        self.change_x = math.cos(angle) * bullet_speed
        self.change_y = math.sin(angle) * bullet_speed

        self.angle = math.degrees(angle)


class UpgradeStation(arcade.Sprite):
    def __init__(self, x, y, image, scale, station_type):
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
        self.station_type = station_type

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, "COD: Zombies ripoff")
        self.player_list = arcade.SpriteList()
        self.zombie_list = []
        self.zombies_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gun_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.upgrade_stations = arcade.SpriteList()

        self.player_sprite = None
        self.physics_engine = None
        self.physics_engine_upgrade_stations = None

        self.camera_for_sprites = arcade.Camera(screen_width, screen_height)
        self.camera_for_gui = arcade.Camera(screen_width, screen_height)

        self.health_loss_delay = 0.3  # how long it takes between hits to lose hp
        self.health_regen_delay = 0.5  # how long it takes to regen
        self.round_change_delay = 0  # delay to change round (set later on)
        self.fire_rate_delay = 0.33  # delay between shots with full auto
        self.bullets_in_gun_mag = 8  # initial bullets in mag
        self.bullets_in_gun_stock = 32  # initial bullets in stock
        self.max_bullets_in_gun_stock = 80  # initial gun stock max
        self.gun_mag_max = 8  # initial gun mag max
        self.gun_ammo_text = ""  # ammo text in bottom right
        self.is_reloading = False  # boolean to check if reloading
        self.reload_timer = 0  # how long player has been reloading for
        self.reload_duration = 0.9  # how long it takes to reload
        self.buy_ammo_cost = 0  # cost to buy ammo (determined by stock max - stock)
        self.buy_max_health_cost = 3000  # initial max health upgrade cost
        self.buy_speed_cost = 5000  # initial speed upgrade cost
        self.buy_damage_cost = 1750  # initial damage upgrade cost
        self.buy_fire_rate_cost = 3500  # initial fire rate upgrade cost
        self.buy_mag_cost = 1500  # initial mag max upgrade cost
        self.buy_stock_cost = 2000  # initial stock max upgrade cost
        self.color_val = 0  # variable to change "Round:" text color
        self.color_change_delay = 0  # time to switch "Round:" color (set later on)

        self.mouse_x = 0  # user cursor x
        self.mouse_y = 0  # user cursor y

        self.camera_pos = []  # list to help convert mouse xy to world xy

        self.mouse_held = False
        self.mouse_pressed = False
        self.has_full_auto = False
        self.full_auto_activated = False

        self.is_touching_ammo_station = False
        self.is_touching_max_health_station = False
        self.is_touching_speed_station = False
        self.is_touching_damage_station = False
        self.is_touching_fire_rate_station = False
        self.is_touching_mag_station = False
        self.is_touching_stock_station = False


    def setup(self):
        arcade.set_background_color(arcade.color.FOREST_GREEN)

        self.player_list = arcade.SpriteList()
        self.zombie_list = []
        self.upgrade_stations = arcade.SpriteList()

        # Create the player
        self.player_sprite = Player(200, 200, 100, 100, 500, 10)
        self.player_list.append(self.player_sprite.player_sprite)

        """ --- Create Upgrade Stations --- """

        upgrade_station = UpgradeStation(300, 400,
                                         "buy_ammo_station.png", 0.25, "ammo_station")
        self.upgrade_stations.append(upgrade_station)

        upgrade_station = UpgradeStation(600, 200,
                                         "max_health_station.png", 0.22, "max_health_station")
        self.upgrade_stations.append(upgrade_station)

        upgrade_station = UpgradeStation(100, -350,
                                         "speed_station.png", 0.23, "speed_station")
        self.upgrade_stations.append(upgrade_station)

        upgrade_station = UpgradeStation(300, -375,"speed_station.png",
                                         0.23, "fire_rate_station")
        self.upgrade_stations.append(upgrade_station)

        upgrade_station = UpgradeStation(-40, 300, "max_health_station.png",
                                         0.22, "damage_station")
        self.upgrade_stations.append(upgrade_station)

        # Create Zombies
        for i in range(initial_zombie_count + 2 * round_number):
            if round_number >= 10:
                speed = 2.5
            elif round_number >= 6:
                speed = random.choice([1.5, 2.5])
            elif round_number >= 3:
                speed = random.choice([0.5, 1.5])
            else:
                speed = 0.5

            zombie = Zombie(random.randrange(-350, -200), random.randrange(-350, -200),
                            initial_zombie_health + 8 * round_number, speed)
            self.zombie_list.append(zombie)
            self.zombies_list.append(zombie.zombie_sprite)

        # Make it so player can move and doesn't phase through zombies (physics engine uses sprite.change_x/y)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite.player_sprite, self.zombies_list)
        self.physics_engine_upgrade_stations = (arcade.PhysicsEngineSimple
                                                (self.player_sprite.player_sprite, self.upgrade_stations))


    def on_draw(self):
        arcade.start_render()
        self.camera_for_sprites.use()

        self.player_list.draw()
        for zombie in self.zombie_list:
            zombie.zombie_sprite.draw()

        self.upgrade_stations.draw()

        self.bullet_list.draw()

        self.camera_for_gui.use()

        arcade.draw_text(f"Health: {self.player_sprite.health}",
                         (screen_width / 2) - 60, 10, arcade.color.RED, 20)  # display player health

        arcade.draw_text(f"Round: {round_number}", 5, 10,
                         [255, self.color_val, self.color_val], 20)
                        # this displays the round number

        arcade.draw_text(f"{self.bullets_in_gun_mag}/{self.bullets_in_gun_stock}",
                         screen_width - 100, 50, arcade.color.WHITE, 20)  # show ammo

        arcade.draw_text(f"{self.player_sprite.points}",
                         screen_width - 100, 120, arcade.color.WHITE, 20)  # show points

        if self.is_reloading:
            bar_width = 200
            bar_height = 15
            reload_x = screen_width - 130
            reload_y = 20

            progress = min(self.reload_timer / self.reload_duration, 1.0)
            filled_width = bar_width * progress

            # draw the background (unfilled) reload progress
            arcade.draw_rectangle_filled(reload_x, reload_y, bar_width, bar_height, arcade.color.DARK_GRAY)
            # then draw the filled part
            arcade.draw_rectangle_filled(reload_x - (bar_width - filled_width) / 2,
                reload_y, filled_width, bar_height, arcade.color.YELLOW)

        # These if statements show text based on what upgrade station you're touching
        if self.is_touching_ammo_station:
            arcade.draw_text(f"Refill ammo: Cost {self.buy_ammo_cost}",
                             200, 200, arcade.color.WHITE, 22)
        if self.is_touching_max_health_station:
            arcade.draw_text(f"Upgrade Max Health: Cost {self.buy_max_health_cost}",
                             200, 200, arcade.color.WHITE, 22)
            arcade.draw_text(f"Current: {self.player_sprite.max_health}",
                             200, 170, arcade.color.WHITE, 22)
        if self.is_touching_speed_station:
            arcade.draw_text(f"Upgrade Speed: Cost {self.buy_speed_cost}",
                             200, 200, arcade.color.WHITE, 22)
            arcade.draw_text(f"Current: {round(movement_speed, 2)}",
                             200, 170, arcade.color.WHITE, 22)
        if self.is_touching_damage_station:
            arcade.draw_text(f"Upgrade Damage: Cost {self.buy_damage_cost}",
                             200, 200, arcade.color.WHITE, 22)
            arcade.draw_text(f"Current: {self.player_sprite.damage}",
                             200, 170, arcade.color.WHITE, 22)
        if self.is_touching_fire_rate_station:
            arcade.draw_text(f"Upgrade Fire Rate: Cost {self.buy_fire_rate_cost}",
                             200, 200, arcade.color.WHITE, 22)
            arcade.draw_text(f"Current: {self.fire_rate_delay} seconds per shot",
                             200, 170, arcade.color.WHITE, 22)
        if self.is_touching_mag_station:
            arcade.draw_text(f"Upgrade Mag Size: Cost {self.buy_mag_cost}",
                             200, 200, arcade.color.WHITE, 22)
            arcade.draw_text(f"Current: {self.bullets_in_gun_mag} max",
                             200, 170, arcade.color.WHITE, 22)
        if self.is_touching_stock_station:
            arcade.draw_text(f"Upgrade Stock Size: Cost {self.buy_stock_cost}",
                             200, 200, arcade.color.WHITE, 22)
            arcade.draw_text(f"Current: {self.max_bullets_in_gun_stock} max",
                             200, 170, arcade.color.WHITE, 22)


    def on_update(self, delta_time):
        self.physics_engine.update()
        self.physics_engine_upgrade_stations.update()
        lower_left_corner = (self.player_sprite.player_sprite.center_x - self.width / 2,
                             self.player_sprite.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, camera_speed)

        # Update player animation
        self.player_sprite.update(delta_time)

        self.bullet_list.update()

        # Update zombie movement and animation
        for zombie in self.zombie_list:
            sprite = zombie.zombie_sprite

            x_diff = self.player_sprite.player_sprite.center_x - sprite.center_x
            y_diff = self.player_sprite.player_sprite.center_y - sprite.center_y

            distance = math.hypot(x_diff, y_diff)
            sprite.update_animation(delta_time)


            if distance > 0:
                x_step = (x_diff / distance) * zombie.speed
                y_step = (y_diff / distance) * zombie.speed
                sprite.center_x += x_step
                sprite.center_y += y_step

            if arcade.check_for_collision(self.player_sprite.player_sprite, sprite):
                zombie.damage_delay += delta_time
                if self.health_loss_delay >= 0.25:
                    self.player_sprite.health -= 10
                    # player loses 10 health 4 times per sec when touching zombie
                    self.health_loss_delay = 0
            else:
                zombie.damage_delay += delta_time

        self.health_loss_delay += delta_time
        self.health_regen_delay += delta_time

        if self.player_sprite.health < self.player_sprite.max_health and self.health_regen_delay >= 0.5:
            self.player_sprite.health += 2  # player gains 2 health twice per second always (for now)
            self.health_regen_delay = 0

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(bullet, self.zombies_list)
            for zombie_sprite in hit_list:
                # Find corresponding zombie object
                for zombie in self.zombie_list:
                    if zombie.zombie_sprite == zombie_sprite:
                        zombie.zombie_health -= self.player_sprite.damage  # bullet always deals 10 damage right now
                        self.player_sprite.points += 10  # give 10 points for bullet hit
                        if zombie.zombie_health <= 0:
                            zombie_sprite.remove_from_sprite_lists()  # makes zombie disappear
                            self.zombie_list.remove(zombie)
                            self.player_sprite.points += 50  # + 50 points for kill
                bullet.remove_from_sprite_lists()  # makes bullet disappear

        self.is_touching_ammo_station = False
        self.is_touching_max_health_station = False
        self.is_touching_speed_station = False
        self.is_touching_damage_station = False
        self.is_touching_fire_rate_station = False

        # check if touching any upgrade station
        for upgrade_station in self.upgrade_stations:
            if isinstance(upgrade_station, UpgradeStation):
                if upgrade_station.station_type == "ammo_station":
                    distance = arcade.get_distance_between_sprites(self.player_sprite.player_sprite, upgrade_station)
                    if distance <= upgrade_station_proximity:
                        self.buy_ammo_cost = (self.max_bullets_in_gun_stock - self.bullets_in_gun_stock) * 5
                        self.is_touching_ammo_station = True
                        break
                elif upgrade_station.station_type == "max_health_station":
                    distance = arcade.get_distance_between_sprites(self.player_sprite.player_sprite, upgrade_station)
                    if distance <= upgrade_station_proximity:
                        self.is_touching_max_health_station = True
                        break
                elif upgrade_station.station_type == "speed_station":
                    distance = arcade.get_distance_between_sprites(self.player_sprite.player_sprite, upgrade_station)
                    if distance <= upgrade_station_proximity:
                        self.is_touching_speed_station = True
                        break
                elif upgrade_station.station_type == "damage_station":
                    distance = arcade.get_distance_between_sprites(self.player_sprite.player_sprite, upgrade_station)
                    if distance <= upgrade_station_proximity:
                        self.is_touching_damage_station = True
                        break
                elif upgrade_station.station_type == "fire_rate_station":
                    distance = arcade.get_distance_between_sprites(self.player_sprite.player_sprite, upgrade_station)
                    if distance <= upgrade_station_proximity:
                        self.is_touching_fire_rate_station = True
                        break


        self.camera_pos = lower_left_corner

        if len(self.zombie_list) == 0:  # If all zombies are dead
            # Change "Round:" color text
            self.color_change_delay += delta_time
            if self.color_change_delay >= 0.75:
                self.color_val = 255 if self.color_val == 0 else 0
                self.color_change_delay = 0

            global round_number
            self.round_change_delay += delta_time
            if self.round_change_delay >= 5:
                round_number += 1
                self.color_change_delay = 0
                self.round_change_delay = 0

                # Determine zombie speed based on round number
                for i in range(initial_zombie_count + 2 * round_number):
                    if round_number >= 18:
                        speed = random.choice([1, 2, 3, 4, 4.5])
                    elif round_number >= 14:
                        speed = random.choice([2.5, 3, 3.5])
                    elif round_number >= 10:
                        speed = 2.5
                    elif round_number >= 6:
                        speed = random.choice([1.5, 2.5])
                    elif round_number >= 3:
                        speed = random.choice([0.5, 1.5])
                    else:
                        speed = 0.5

                    # Create zombie object
                    zombie = Zombie(random.randrange(-350, -200), random.randrange(-350, -200),
                                    initial_zombie_health + 8 * round_number, speed)
                    self.zombie_list.append(zombie)
                    self.zombies_list.append(zombie.zombie_sprite)

        if self.is_reloading:  # if you're reloading
            self.reload_timer += delta_time  # start reload delay
            if self.reload_timer >= self.reload_duration:  # when delay is done
                # if you have enough in stock to fill mag
                if self.bullets_in_gun_stock >= self.gun_mag_max - self.bullets_in_gun_mag:
                    self.bullets_in_gun_stock -= self.gun_mag_max - self.bullets_in_gun_mag
                    self.bullets_in_gun_mag += self.gun_mag_max - self.bullets_in_gun_mag
                else:  # if you don't have enough to fill mag
                    self.bullets_in_gun_mag += self.bullets_in_gun_stock
                    self.bullets_in_gun_stock = 0
                self.is_reloading = False

        # Make shooting actually happen
        if self.has_full_auto and self.full_auto_activated:
            self.fire_rate_delay += delta_time
            if self.mouse_held and self.fire_rate_delay >= 0.33 and self.bullets_in_gun_mag > 0:
                world_x = self.mouse_x + self.camera_pos[0]  # makes mouse coords work with the camera
                world_y = self.mouse_y + self.camera_pos[1]  # makes mouse coords work with the camera
                bullet = Bullet(self.player_sprite.player_sprite.center_x,
                                self.player_sprite.player_sprite.center_y,
                                world_x,
                                world_y)
                self.bullet_list.append(bullet)
                self.bullets_in_gun_mag -= 1  # lose a bullet when user shoots
                self.fire_rate_delay = 0
            elif self.mouse_held and self.fire_rate_delay >= 0.33 and self.bullets_in_gun_mag == 0:
                self.reload()
        elif self.mouse_pressed and self.bullets_in_gun_mag > 0:
            world_x = self.mouse_x + self.camera_pos[0]  # makes mouse coords work with the camera
            world_y = self.mouse_y + self.camera_pos[1]  # makes mouse coords work with the camera
            bullet = Bullet(self.player_sprite.player_sprite.center_x,
                            self.player_sprite.player_sprite.center_y,
                            world_x,
                            world_y)
            self.bullet_list.append(bullet)
            self.bullets_in_gun_mag -= 1  # lose a bullet when user shoots
            self.mouse_pressed = False


    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.player_sprite.player_sprite.change_y = movement_speed / 2
            self.player_sprite.is_walking = True
        elif key == arcade.key.A:
            self.player_sprite.player_sprite.change_x = -movement_speed / 2
            self.player_sprite.is_walking = True
        elif key == arcade.key.S:
            self.player_sprite.player_sprite.change_y = -movement_speed / 2
            self.player_sprite.is_walking = True
        elif key == arcade.key.D:
            self.player_sprite.player_sprite.change_x = movement_speed / 2
            self.player_sprite.is_walking = True
        elif key == arcade.key.E:
            if self.is_touching_ammo_station and self.player_sprite.points >= self.buy_ammo_cost:
            # If you're touching ammo station, and you have enough points, then
                self.buy_ammo()
            elif self.is_touching_max_health_station and self.player_sprite.points >= self.buy_max_health_cost:
            # If you're touching max health station, and you have enough points, then
                self.buy_max_health()
            elif self.is_touching_speed_station and self.player_sprite.points >= self.buy_speed_cost:
            # If you're touching max health station, and you have enough points, then
                self.buy_speed()
        elif key == arcade.key.SPACE:
            arcade.close_window()
        elif key == arcade.key.R:
            self.reload()
        elif key == arcade.key.J:
            self.has_full_auto = True
        elif key == arcade.key.K and self.has_full_auto:
            if self.full_auto_activated is False:
                self.full_auto_activated = True
            else:
                self.mouse_pressed = False
                self.full_auto_activated = False


    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.player_sprite.change_x = 0

        if not (self.player_sprite.player_sprite.change_x or self.player_sprite.player_sprite.change_y):
            self.player_sprite.is_walking = False


    def reload(self):
        if not self.is_reloading and self.bullets_in_gun_stock > 0:  # if you have bullets in stock
            self.is_reloading = True
            self.reload_timer = 0


    def buy_ammo(self):
        self.player_sprite.points -= self.buy_ammo_cost
        self.bullets_in_gun_stock = self.max_bullets_in_gun_stock


    def buy_max_health(self):
        self.player_sprite.points -= self.buy_max_health_cost
        self.buy_max_health_cost += round(self.buy_max_health_cost * 0.25)
        self.player_sprite.max_health += 5


    def buy_speed(self):
        self.player_sprite.points -= self.buy_speed_cost
        self.buy_speed_cost += round(self.buy_speed_cost * 0.35)
        global movement_speed
        movement_speed += 0.2


    def buy_damage(self):
        self.player_sprite.points -= self.buy_damage_cost
        self.buy_damage_cost += round(self.buy_damage_cost * 0.2)
        self.player_sprite.damage += 5


    def buy_fire_rate(self):
        self.player.points -= self.buy_fire_rate_cost
        self.fire_rate_cost += round(self.buy_fire_rate_cost * 0.3)
        self.fire_rate_delay -= 0.02


    def buy_mag_max(self):
        self.player_sprite.points -= self.buy_mag_cost
        self.buy_mag_cost += round(self.buy_mag_cost * 0.25)
        self.gun_mag_max += 1


    def buy_stock_max(self):
        self.player_sprite.points -= self.buy_stock_cost
        self.buy_stock_cost += round(self.buy_stock_cost * 0.18)
        self.max_bullets_in_gun_stock += 4


    def on_mouse_press(self, x, y, button, modifiers):
        if self.bullets_in_gun_mag > 0 and button == arcade.MOUSE_BUTTON_LEFT:
            self.mouse_held = True
            self.mouse_pressed = True
            self.mouse_x = x
            self.mouse_y = y

        elif button == arcade.MOUSE_BUTTON_LEFT:
            self.reload()  # reload automatically when u try to shoot with 0 bullets
                           # only works with semi auto


    def on_mouse_release(self, x, y, button, modifiers):
        self.mouse_held = False


    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_x = x
        self.mouse_y = y


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()