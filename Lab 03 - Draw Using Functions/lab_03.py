import arcade as arc

def on_draw(delta_time):  # draws everybody
    arc.start_render()
    #  IF STATIONARY:
    #   x1 and y1 are for head, x2 and y2 are for the body,
    #  not sure why I didn't make it all part of the same thing...
    #  y2 should be 20 less than y1
    #  x1 and x2 should be the same
    arc.draw_lrtb_rectangle_filled(0, 799, 375, 0, arc.csscolor.SANDY_BROWN)  # draw sand
    arc.draw_lrtb_rectangle_filled(0, 799, 550, 375, arc.csscolor.DARK_BLUE)
    arc.draw_circle_filled(ball_x, ball_y, 23, arc.csscolor.ORANGE)  # draws the beach ball
    draw_person(400, 400, 400, 380)  # left main dude
    draw_person(300, 400, 300, 380)  # right main dude
    draw_person(500, 500, 500, 480)  # left guy in water
    draw_person(570, 500, 570, 480)  # right guy in water
    draw_person(155, 330, 155, 310)  # guy under left umbrella
    sun_rays = [
        (720, 650, 720, 790),  # vertical sun ray
        (650, 720, 790, 720),  # horizontal sun day
        (670, 670, 770, 770),  # sun ray slope = 1
        (670, 770, 770, 670),  # sun ray slope = -1
    ]

    for line in sun_rays:
        arc.draw_line(line[0], line[1], line[2], line[3], arc.csscolor.YELLOW, 4)
        #  draws sun rays (copied fom lab 2)

    draw_umbrella(100, 225)
    draw_umbrella(600, 170)

    arc.draw_circle_filled(720, 720, 40, arc.csscolor.YELLOW)  # draws the sun

    arc.draw_polygon_filled(((322, 310),
                             (332, 355),
                             (362, 355),
                             (372, 310)
                             ),
                            arc.csscolor.SADDLE_BROWN)

ball_x = 525
ball_y = 560

def draw_umbrella(x, y):
    arc.draw_line(x, y, x + 30, y + 170, arc.csscolor.WHITE, 4)
    arc.draw_parabola_filled(x - 66, y + 120, x + 130, 50, arc.csscolor.GOLD, 8)
    arc.draw_polygon_filled(((x - 80, y),
                             (x - 50, y + 65),
                             (x, y + 65),
                             (x - 30, y)
                             ),
                            arc.csscolor.LIME_GREEN)

def start():
    arc.open_window(800, 800, "A Day at the Beach")
    arc.set_background_color(arc.csscolor.SKY_BLUE)
    arc.schedule(on_draw, 1 / 60)
    arc.run()

def draw_person(x1, y1, x2, y2):
    draw_head(x1, y1, x1 - 5, y1 + 5)
    draw_body(x2, y2)


def draw_head(x1, y1, x2, y2):
    arc.draw_circle_filled(x1, y1, 20, arc.csscolor.PEACH_PUFF)  # draws head
    arc.draw_circle_filled(x2, y2, 5, arc.csscolor.GREEN)
    arc.draw_circle_filled(x2 + 12, y2, 5, arc.csscolor.GREEN)
    arc.draw_parabola_outline(x1 - 13, y1 - 15, x1 + 13, 10, arc.csscolor.DARK_ORANGE, 5, 180)


def draw_body(x, y):
    lines = [
        (x, y, x, y - 30),  # torso
        (x, y - 30, x - 15, y - 60),  # leg left --> right
        (x, y - 30, x + 15, y - 60),  # leg right --> left
        (x, y - 30, x - 10, y - 10),  # arm left --> right
        (x, y - 30, x + 10, y - 10),  # arm right --> left
    ]

    for line in lines:
        arc.draw_line(line[0], line[1], line[2], line[3], arc.csscolor.BLACK)

start()
