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


def candy_bar(key, modifiers):
    item_list.append("milky way")


def on_key_press(key, modifiers):
    arcade.close_window()


def main():  # literally runs the entire game
    room_list = []  # temporary empty list that all the rooms go in to.

    # South Hall (0)
    room = Room("You're in the South Hall. There is the bedroom "
                "to the west, the bathroom\nto the east, the North Hall"
                " to the north, and the exit to the south.",
                4, 3, 2, 1)
    room_list.append(room)

    # Bedroom (1)
    room = Room("You are in the bedroom. Only path is back to the South Hall. (go east)",
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
    room = Room("You're in the living room. There is the \nNorth Hall to the west and "
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
    room = Room("You are outside. Going west takes you to the gas station,"
                " going east leads\nyou to your friend's crib, north is back inside,"
                " and south brings you across the street.", 0, 9, 10, 11)

    room_list.append(room)

    # Friend's crib (9)
    room = Room("You're at your friend's crib. The address is 4937 Smith Avenue."
                "\nUnfortunately, no one is home, so you gotta dip by going west",
                None, None, None, 8)

    room_list.append(room)

    # Across street (10)
    room = Room("You are across the street. From here, you can go north to in front of your house,"
                " east towards\nyour other friend's crib, or west to the library.",
                8, 12, 14, 13)

    room_list.append(room)

    # Gas station entrance (11)
    room = Room("You walked to the gas station and realize you're a bit hungry.",
                13, 14, None, None)

    room_list.append(room)

    # Other friend's crib (12)
    room = Room("You are at your other friend's crib. The address is 3894 Neutral Drive.\n"
                "He isn't home either. Unlucky, go back.",
                None, None, None, 10)

    room_list.append(room)

    # Library (13)
    room = Room("You are in the library. Non one is home, but there is an old, dusty book"
                " on a table.", None, 10, None, None)

    room_list.append(room)

    # Jeff the Killer encounter (14)
    room = Room("You are where you encountered Jeff the Killer.\nGoing north takes you across the street and "
                "going south leads you to McDonald's.", 10, None, 15, None)

    room_list.append(room)

    # Micky D's (15)
    room = Room("You're at Micky D's.", 14, None, None, None)

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
    dark_alley = False
    mcdonalds = False
    gave_flashlight = False
    jeff_defeated = False
    decryption_key1 = 4937
    decryption_key2 = 3894
    username = "MrCoolGuy123"
    password = "Jellybean"
    encrypted = ""
    decrypted = ""

    while True:
        print(room_list[current_room].description)
        print()
        if current_room == 1 and not has_flashlight:
            answer = input("There's a flashlight on the bed. "
                           "Do you want to pick it up? (yes/no) ")
            if answer.lower() == "yes" or answer.lower() == "y":
                print("You decided to pick up the flashlight. It's in your inventory now.")
                print()
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
            if jeff_defeated:
                answer = input("Do you want to use the computer? ")
                if answer.lower() == "yes" or answer.lower() == "y":
                    for c in username:
                        encrypted += chr(ord(c) + decryption_key1)
                    print("Your McDonald's username is:", encrypted)
                    answer = int(input("Enter a 4-digit number to decrypt this bad boy. "))
                    for c in encrypted:
                        decrypted += chr(ord(c) - answer)
                    print("With your decryption key, your username is:", decrypted)
                    encrypted = ""
                    decrypted = ""
                    print()
                    for c in password:
                        encrypted += chr(ord(c) + decryption_key2)
                    print("Your McDonald's password is:", encrypted)
                    answer = int(input("Enter a 4-digit number to decrypt this bad boy. "))
                    for c in encrypted:
                        decrypted += chr(ord(c) - answer)
                    print("With your decryption key, your password is:", decrypted)
                    encrypted = ""
                    decrypted = ""
        if current_room == 6:
            kitchen = True
            answer = input("There's a knife sitting out on the counter. Want to grab it? ")
            if answer.lower() == "yes" or answer.lower() == "y":
                item_list.append("knife")
                print("You pick up the knife")
                print()
            else:
                print("You left the knife on the counter.")
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
            answer = input("You're deciding between chips and a candy bar. Which one do you want? ")
            print()
            if answer.lower() == "chips":
                print("You picked up a bag of chips for $1.59\n")
                item_list.append("bag of salt and vinegar chips")
            elif answer.lower() == "candy" or answer.lower() == "candy bar" or answer.lower() == "bar":
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
                print("You're still in the library btw, go east.")
            else:
                print("You left the old book alone.")
        if current_room == 14 and not jeff_defeated:
            print("You adventure south down the street the gas station worker "
                      "told you about.")
            if "knife" in item_list:
                print("Thankfully, you were able to defend yourself with the "
                          "kitchen knife you \ngrabbed earlier from Jeff the Killer"
                          ". Jeffy, after being defeated, leaves behind\n what looks like a second map! "
                          "It can be accessed by typing 'map2'")
                jeff_defeated = True
                print()
            else:
                print("Little did you know, Jeff the Killer was "
                          "waiting on the other end, \nand now the game is over because "
                          "you are so incredibly cooked.")
                break
        else:
            dark_alley = True
        if current_room == 15:
            mcdonalds = True
            answer = input("What's the username to the McDonald's account? ")
            if answer == "MrCoolGuy123":
                answer = input("What the password to the McDonald's account? ")
                if answer == "Jellybean":
                    print("Success! You used your McDonald's app to get a great deal.")
                else:
                    print("That's not right, I should check my pc in my living room. Going back to Outside now.")
                    current_room = 8
            else:
                print("That's not right, I should check my pc in my living room. Going back to Outside now.")
                current_room = 8
        print()
        answer = input("What direction do you wanna go? Or q to quit. You can also type "
                       "i to check your inventory, or map to see the map (duh). ")
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
                if current_room == 10 and not gave_flashlight:
                    print("Homie you can't go that way :skull:")
            else:
                current_room = next_room
        elif answer.lower() == "i":
            if len(item_list) == 0:
                print("You don't have anything in your inventory.\n")
            else:
                print()
                print(item_list)
                print()
        elif answer.lower() == "map":
            window = arcade.Window(600, 600, "Map")
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
                arcade.draw_text("Outside", 280, 147, arcade.csscolor.BLACK, 8, bold=True)
            if friend_house:
                arcade.draw_text("Friend's", 404, 153, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("crib", 413, 143, arcade.csscolor.BLACK, 8, bold=True)
            if across_street:
                arcade.draw_text("Across", 280, 87, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("street", 280, 77, arcade.csscolor.BLACK, 8, bold=True)
            if gas_station:
                arcade.draw_text("Gas", 160, 152, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("station", 154, 142, arcade.csscolor.BLACK, 8, bold=True)
            if friend2_house:
                arcade.draw_text("Other", 407, 89, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("friend's", 405, 79, arcade.csscolor.BLACK, 8, bold=True)
                arcade.draw_text("crib", 413, 69, arcade.csscolor.BLACK, 8, bold=True)
            if library:
                arcade.draw_text("Library", 154, 82, arcade.csscolor.BLACK, 8, bold=True)
            if dark_alley:
                arcade.draw_text("Dark alley", 272, 32, arcade.csscolor.BLACK, 8, bold=True)
            for i in range (4):  # draw porch, north hall, south hall (repeat), and exit
                arcade.draw_lrtb_rectangle_outline(275, 325, 275 + 50 * i, 225 + 50 * i,
                                                   arcade.csscolor.BLACK, 3)
            arcade.draw_lrtb_rectangle_outline(325, 375, 375, 325,
                                               arcade.csscolor.BLACK, 3)  # draws living room
            arcade.draw_lrtb_rectangle_outline(225, 275, 375, 350,
                                               arcade.csscolor.BLACK, 3)  # draws kitchen
            for i in range(3):  # draws gas station, outside, and friend's house
                arcade.draw_lrtb_rectangle_outline(150 + 125 * i, 200 + 125 * i, 180, 130,
                                                   arcade.csscolor.BLACK, 3)
            for i in range(3):
                arcade.draw_lrtb_rectangle_outline(150 + 125 * i, 200 + 125 * i, 105, 55,
                                                   arcade.csscolor.BLACK, 3)
            arcade.draw_text("Press any key to close", 190, 500,
                             arcade.csscolor.BLACK, 20, bold=True)
            arcade.draw_text(f"Current Location: {room_list[current_room].description.split('.')[0]}", 20, 560,
                             arcade.csscolor.BLACK, 12, bold=True)
            arcade.draw_lrtb_rectangle_outline(270, 330, 50, 10,
                                               arcade.csscolor.BLACK, 3)
            arcade.finish_render()
            window.on_key_press = on_key_press
            arcade.run()
        elif answer.lower() == "map2" and jeff_defeated:
            window = arcade.Window(600, 600, "Second map")
            arcade.set_background_color(arcade.csscolor.SKY_BLUE)
            arcade.start_render()
            arcade.draw_lrtb_rectangle_outline(320, 380, 375, 325,
                                               arcade.csscolor.BLACK, 3)
            if mcdonalds:
                arcade.draw_text("Micky D's", 325, 350, arcade.csscolor.BLACK, 8, bold=True)
            arcade.finish_render()
            window.on_key_press = on_key_press
            arcade.run()
        elif answer.lower() == "q" or answer.lower() == "quit":
            print("ggs")
            break
        else:
            print("Bro I'm a dumb computer idk what this '" + answer + "' nonsense is.\n")


main()
