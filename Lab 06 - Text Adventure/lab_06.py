class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description  # only part that is a string
        self.north = north  # room number that is to the north
        self.east = east  # room number that is to the east
        self.south = south  # room number that is to the south
        self.west = west  # room number that is to the west


def main():
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
    room = Room("You crossed the street. From here, you can go north to back where you just were,"
                " east towards\nyour other friend's crib, or west to the gas station. You have "
                "no idea where south goes.", 8, 12, None, 11)

    room_list.append(room)

    # Gas station entrance (11)
    room = Room("You walked to the gas station and realize you're a bit hungry. Do you wanna "
                "pick up chips or a candy bar?\n(n for chips, e for candy bar)", 13, 14, None, None)

    room_list.append(room)

    # Other friend's crib (12)
    room = Room("You march diligently into your other friend's crib. He isn't home either. Unlucky, go back.",
                None, None, None, 10)

    room_list.append(room)

    # Gas station chips (13)
    room = Room("You picked up some chips. They were $1.59. Time to go! "
                    "(go east)", None, 8, None, None)

    room_list.append(room)

    # Gas station candy bar (14)
    room = Room("You picked up a candy bar. It was $1.39. Time to go! "
                    "(go east)", None, 8, None, None)

    current_room = 0  # 0 is the south hall

    done = False  # makes game not insta-end

    while not done:
        print(room_list[current_room].description)
        print()
        answer = input("What direction do you wanna go? Or q to quit. ")
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
                print("Homie you can't go that way :skull:")
            else:
                current_room = next_room
        elif answer.lower() == "q" or answer.lower() == "quit":
            print("ggs")
            break
        else:
            print("Bro I'm a dumb computer idk what this", answer, "nonsense is.\n")


main()