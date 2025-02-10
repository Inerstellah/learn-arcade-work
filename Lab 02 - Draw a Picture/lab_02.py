"""
Alright guys, we're gonna make a really cool drawing for the 2nd lab
(I didn't use ChatGPT I swear, except for the "for line in lines" list part)
"""

import arcade as arc
from arcade import draw_lrbt_rectangle_filled

arc.open_window(800, 800, "Is this a cool drawing? (I'm a beginner)")  # Makes the actual window

arc.set_background_color(arc.csscolor.SKY_BLUE)  # Makes a blue sky

arc.start_render()  # allows for things to be drawn

arc.draw_lrbt_rectangle_filled(0, 799, 0, 320, arc.csscolor.GREEN)  # draws the grass

draw_lrbt_rectangle_filled(120, 330, 285, 555, arc.csscolor.GRAY)  # draws the house

arc.draw_triangle_filled(80, 555, 370, 555, 225, 700, arc.csscolor.BLACK)  # draws a triangular roof

arc.draw_lbwh_rectangle_outline(160, 470, 40, 40, arc.csscolor.BLACK)  # draws a window outline
arc.draw_lbwh_rectangle_outline(250, 470, 40, 40, arc.csscolor.BLACK)  # draws a window outline

arc.draw_line(270, 470, 270, 510, arc.csscolor.BLACK)  # makes a vertical line for a window
arc.draw_line(180, 470, 180, 510, arc.csscolor.BLACK)  # makes a vertical line for a window
arc.draw_line(250, 490, 290, 490, arc.csscolor.BLACK)  # makes a horizontal line for a window
arc.draw_line(160, 490, 200, 490, arc.csscolor.BLACK)  # makes a horizontal line for a window

arc.draw_lrbt_rectangle_filled(212, 242, 285, 355, arc.csscolor.SADDLE_BROWN)  # draws a brown door

arc.draw.draw_circle_filled(234, 315, 4.5, arc.csscolor.YELLOW)  # draws a doorknob

arc.draw_circle_filled(600, 380, 25, arc.csscolor.PEACH_PUFF)  # draws a person's head

lines = [
    (600, 355, 600, 300),  # torso
    (600, 300, 580, 270),  # leg
    (600, 300, 620, 270),  # leg
    (600, 315, 590, 350),  # arm
    (600, 315, 610, 350),  # arm
]

for line in lines:
    arc.draw_line(line[0], line[1], line[2], line[3], arc.csscolor.BLACK)  # actually draws the lines

arc.draw_circle_filled(592, 390, 4.5, arc.csscolor.DODGER_BLUE)  # draws an eyeball
arc.draw_circle_filled(608, 390, 4.5, arc.csscolor.DODGER_BLUE)  # draws another eyeball

arc.draw_parabola_filled(585, 355, 615, 20, arc.csscolor.ORANGE_RED, 180)  # draws a smile

arc.draw_circle_filled(720, 720, 40, arc.csscolor.YELLOW)  # draws the sun

sun_rays = [
    (720, 650, 720, 790),  # vertical sun ray
    (650, 720, 790, 720),  # horizontal sun day
    (670, 670, 770, 770),  # sun ray slope = 1
    (670, 770, 770, 670),  # sun ray slope = -1
]

for line in sun_rays:
    arc.draw_line(line[0], line[1], line[2], line[3], arc.csscolor.YELLOW, 4)  # actually draws the suns' rays

arc.finish_render()  # stops drawing

arc.run()  # makes the window not insta-close
