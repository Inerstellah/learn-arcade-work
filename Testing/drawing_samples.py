"""
This code is a test run from chapter 5
We are going to be drawing woohoo!
We have to import more code. Check out line 6
"""
import arcade

arcade.open_window(600, 600, "Drawing Cool Stuff")

# setting background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# getting ready to draw
arcade.start_render()

arcade.draw_lrbt_rectangle_filled(0, 599, 0 , 300, arcade.csscolor.GREEN)
arcade.draw_lrbt_rectangle_filled(90, 110, 280, 340, arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_lrbt_rectangle_filled(190, 210, 280, 340, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)


# finishing up drawing
arcade.finish_render()

# the line below this one keeps the window open so it doesn't insta-close
arcade.run()
