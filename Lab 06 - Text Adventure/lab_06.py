import arcade

class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description  # only part that is a string
        self.north = north  # room number that is to the north
        self.east = east  # room number that is to the east
        self.south = south  # room number that is to the south
        self.west = west  # room number that is to the west

item_list = []

def item1():
     item_list.append("flashlight")


def chips():
    item_list.append("bag of salt and vinegar chips")


def candy_bar():
    item_list.append("milky way")


def main():  # literally runs the entire game
    room_list = []  # temporary empty list that all the rooms go in to.

    # South Hall (0)
    room = Room("You're in the South Hall. There is the bedroom "
                "to the west, the bathroom\nto the east, the North Hall"
                " to the north, and the exit to the south.",
                4, 3, 2, 1)
    room_list.append(room)

    # Bedroom (1)
    room = Room("You are in the bedroom. Only path is back to the South Hall.",
                None, 0, None, None)

    room_list.append(room)

    # Exit (2)
    room = Room("""This is the exit. Are you sure you want to leave your house? You can go 
north to the South Hall instead. (Type "s" to leave, or "n")""", 0, None, 8, None)

    room_list.append(room)

    # Bathroom (3)
    room = Room("You are in the bathroom. There is the South Hall\nto the west and"
                " the living room to the north.", 5, None, None, 0)

    room_list.append(room)

    # North Hall (4)
    room = Room("You're in the North Hall. There is the kitchen to the west, "
                "the living room\nto the east, the back porch to the north,"
                "and the South Hall to the south.", 7, 5, 0, 6)

    room_list.append(room)

    # Living room (5)
    room = Room("You're are in the living room. There is the \nNorth Hall to the west and "
                "the bathroom to the south.", None, None, 3, 4)

    room_list.append(room)

    # Kitchen (6)
    room = Room("You are in the kitchen. Only way out is to the North Hall, which is "
                "to the east.", None, 4, None, None)

    room_list.append(room)

    # Back Porch (7)
    room = Room("You are outside on the back porch. Only path is back to the North Hall, "
                "which is to the south.", None, None, 4, None)

    room_list.append(room)

    # Outside (8)
    room = Room("You decided to go outside. Going west takes you to the gas station,"
                " going east leads\nyou to your friend's crib, north is back inside,"
                " and south brings you across the street.", 0, 9, 10, 11)

    room_list.append(room)

    # Friend's crib (9)
    room = Room("You're now in your friend's crib. Unfortunately, no one is home, so"
                " you gotta dip by going west", None, None, None, 8)

    room_list.append(room)

    # Across street (10)
    room = Room("You crossed the street. From here, you can go north to in front of your house,"
                " east towards\nyour other friend's crib, or west to the library.",
                8, 12, None, 13)

    room_list.append(room)

    # Gas station entrance (11)
    room = Room("You walked to the gas station and realize you're a bit hungry.",
                13, 14, None, None)

    room_list.append(room)

    # Other friend's crib (12)
    room = Room("You march diligently into your other friend's crib. He isn't home either. Unlucky, go back.",
                None, None, None, 10)

    room_list.append(room)

    # Library (13)
    room = Room("You go into the library. Non one is home, but there is an old, dusty book"
                " on a table.", None, 10, None, None)

    room_list.append(room)

    current_room = 0  # 0 is the south hall btw

    has_flashlight = False
    has_read_book = False
    bedroom = False
    exits = False
    bathroom = False
    north_hall = False
    kitchen = False
    living_room = False
    porch = False
    outside = False
    across_street = False
    gas_station = False
    friend_house = False
    friend2_house = False
    library = False
    gave_flashlight = False

    while True:
        print(room_list[current_room].description)
        print()
        if current_room == 1 and not has_flashlight:
            answer = input("There's a flashlight on the bed. "
                           "Do you want to pick it up? (yes/no) ")
            if answer.lower() == "yes":
                item1()  # Call the function that adds the flashlight to the inventory
                has_flashlight = "flashlight" in item_list  # Update flashlight status
            else:
                print("You left the flashlight alone.")
            print(room_list[current_room].description)
            print()
            bedroom = True
        if current_room == 2:
            exits = True
        if current_room == 3:
            bathroom = True
        if current_room == 4:
            north_hall = True
        if current_room == 5:
            living_room = True
        if current_room == 6:
            kitchen = True
        if current_room == 7:
            porch = True
        if current_room == 8:
            outside = True
        if current_room == 9:
            friend_house = True
        if current_room == 10:
            across_street = True
        if current_room == 11:
            gas_station = True
            answer = input("Do you wanna pick up some chips or a candy bar? ")
            print()
            if answer.lower() == "chips":
                print("You picked up a bag of chips for $1.59\n")
                item_list.append("bag of salt and vinegar chips")
            elif answer.lower() == "candy" or answer.lower() == "candy bar":
                print("You picked up a milky way for $1.19\n")
                item_list.append("milky way")
            elif answer.lower() == "flashlight" and "flashlight" in item_list and has_read_book:
                print("You give your flashlight to the worker. In return, he tells you what "
                      "lies south from across the street.\n")
                item_list.remove("flashlight")
                gave_flashlight = True
            else:
                print("You didn't buy anything. Leaving the gas station.\n")
            current_room = 8
            print(room_list[current_room].description)
            print()
        if current_room == 12:
            friend2_house = True
        if current_room == 13 and not has_read_book:
            library = True
            answer = input("Do you want to read it? ")
            print()
            if answer.lower() == "yes" or answer.lower() == "y":
                has_read_book = True
                print("You try to read the book. Most of it is illegible, but one part says "
                      "'the worker likes flashlights!")
            else:
                print("You left the old book alone.")

        answer = input("What direction do you wanna go? Or q to quit. You can also type "
                       "i to check your inventory, or map to see the map (duh). ")
        print()
        if answer.lower() == "n" or answer.lower() == "north":  # if user says north
            next_room = room_list[current_room].north
            if next_room is None:
                print("Homie you can't go that way :skull:")
            else:
                current_room = next_room
        elif answer.lower() == "w" or answer.lower() == "west":  # if user says west
            next_room = room_list[current_room].west
            if next_room is None:
                print("Homie you can't go that way :skull:")
            else:
                current_room = next_room
        elif answer.lower() == "e" or answer.lower == "east":  # if user says east
            next_room = room_list[current_room].east
            if next_room is None:
                print("Homie you can't go that way :skull:")
            else:
                current_room = next_room
        elif answer.lower() == "s" or answer.lower() == "south":  # if user says south
            next_room = room_list[current_room].south
            if next_room is None:
                if current_room == 10 and gave_flashlight:
                    print("You adventure south down the street the gas station worker "
                          "told you about. \nLittle did you know, Jeff the Killer was "
                          "waiting on the other end, \nand now the game is over because "
                          "you are so incredibly cooked.")
                    break
                else:
                    print("Homie you can't go that way :skull:")
            else:
                current_room = next_room
        elif answer.lower() == "i":
            if len(item_list) == 0:
                print("You don't have anything in your inventory.\n")
            else:
                print(item_list)
                print()
        elif answer.lower() == "map":
            arcade.open_window(600, 600, "Map")
            arcade.set_background_color(arcade.csscolor.SKY_BLUE)
            arcade.start_render()
            for i in range(3):  # draws bedroom, south hall, and bathroom
                arcade.draw_lrtb_rectangle_outline(225 + 50 * i, 275 + 50 * i, 325, 275,
                                                   arcade.csscolor.BLACK, 3)
            arcade.draw_text("South", 288, 294, arcade.csscolor.BLACK, 8, bold=True)
            arcade.draw_text("Hall", 288, 284, arcade.csscolor.BLACK, 8, bold=True)
            if bedroom:
                arcade.draw_text("Bedroom", 225, 290, arcade.csscolor.BLACK, 8, bold=True)
            if exits:
                arcade.draw_text("Exit", 288, 250, arcade.csscolor.BLACK, 8, bold=True)
            if bathroom:
                arcade.draw_text("Bath", 334, 294, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("room", 334, 284, arcade.csscolor.BLACK, 8, bold=True)
            if north_hall:
                arcade.draw_text("North", 288, 344, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("Hall", 288, 334, arcade.csscolor.BLACK, 8, bold=True)
            if living_room:
                arcade.draw_text("Living", 338, 344, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("room", 338, 334, arcade.csscolor.BLACK, 8, bold=True)
            if kitchen:
                arcade.draw_text("Kitchen", 227, 355, arcade.csscolor.BLACK, 8, bold=True)
            if porch:
                arcade.draw_text("Porch", 288, 385, arcade.csscolor.BLACK, 8, bold=True)
            if outside:
                arcade.draw_text("Outside", 280, 117, arcade.csscolor.BLACK, 8, bold=True)
            if friend_house:
                arcade.draw_text("Friend's", 404, 123, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("crib", 413, 113, arcade.csscolor.BLACK, 8, bold=True)
            if across_street:
                arcade.draw_text("Across", 280, 57, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("street", 280, 47, arcade.csscolor.BLACK, 8, bold=True)
            if gas_station:
                arcade.draw_text("Gas", 160, 122, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("station", 154, 112, arcade.csscolor.BLACK, 8, bold=True)
            if friend2_house:
                arcade.draw_text("Other", 407, 59, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("friend's", 405, 49, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("crib", 413, 39, arcade.csscolor.BLACK, 8, bold=True)
            if library:
                arcade.draw_text("Library", 154, 52, arcade.csscolor.BLACK, 8, bold=True)
            for i in range (4):  # draw porch, north hall, south hall (repeat), and exit
                arcade.draw_lrtb_rectangle_outline(275, 325, 275 + 50 * i, 225 + 50 * i,
                                                   arcade.csscolor.BLACK, 3)
            arcade.draw_lrtb_rectangle_outline(325, 375, 375, 325,
                                               arcade.csscolor.BLACK, 3)  # draws living room
            arcade.draw_lrtb_rectangle_outline(225, 275, 375, 350,
                                               arcade.csscolor.BLACK, 3)  # draws kitchen
            for i in range(3):  # draws gas station, outside, and friend's house
                arcade.draw_lrtb_rectangle_outline(150 + 125 * i, 200 + 125 * i, 150, 100,
                                                   arcade.csscolor.BLACK, 3)
            for i in range(3):
                arcade.draw_lrtb_rectangle_outline(150 + 125 * i, 200 + 125 * i, 75, 25,
                                                   arcade.csscolor.BLACK, 3)
            arcade.finish_render()
            arcade.run()
        elif answer.lower() == "q" or answer.lower() == "quit":
            print("ggs")
            break
        else:
            print("Bro I'm a dumb computer idk what this '" + answer + "' nonsense is.\n")


main()
