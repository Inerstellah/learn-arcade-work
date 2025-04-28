import arcade

WIDTH = 16
HEIGHT = 16
MARGIN = 5
ROW_COUNT = 16
COLUMN_COUNT = 16

SCREEN_WIDTH = ROW_COUNT * (WIDTH + MARGIN) + MARGIN
SCREEN_HEIGHT = COLUMN_COUNT * (HEIGHT + MARGIN) + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        # --- Create grid of numbers
        # Create an empty list
        self.grid = []
        # Loop for each row
        for row in range(ROW_COUNT):
            # For each row, create a list that will
            # represent an entire row
            self.grid.append([])
            # Loop for each column
            for column in range(COLUMN_COUNT):
                # Add the number zero to the current row
                self.grid[row].append(0)

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        for column in range(COLUMN_COUNT):
            x = column * WIDTH + WIDTH / 2 + (column + 1) * MARGIN
            for row in range(ROW_COUNT):
                y = row * HEIGHT + HEIGHT / 2 + (row + 1) * MARGIN
                self.color = arcade.csscolor.WHITE
                if self.grid[row][column] == 1:
                    self.color = arcade.csscolor.GREEN
                else:
                    self.color = arcade.csscolor.WHITE
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, self.color)

    def on_mouse_press(self, x, y, button, key_modifiers):

        box_x = x // (WIDTH + MARGIN)
        box_y = y // (HEIGHT + MARGIN)
        print(f"Click coordinates: {x, y}, "
              f"box coordinates: {box_x, box_y}")

        # List of (dx, dy) offsets: current box + adjacent boxes
        neighbors = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in neighbors:
            new_x = box_x + dx
            new_y = box_y + dy

            # Check if the new coordinates are inside the grid so that it doesn't crash when u click an edge
            if 0 <= new_x < COLUMN_COUNT and 0 <= new_y < ROW_COUNT:
                if self.grid[new_y][new_x] == 0:
                    self.grid[new_y][new_x] = 1
                else:
                    self.grid[new_y][new_x] = 0

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            arcade.close_window()


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()