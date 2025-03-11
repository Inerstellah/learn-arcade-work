class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []

    # PSA the exit is not an option cause it's dark outside and you're a kid.

    # South Hall
    room = Room("You're in the South Hall. There is the bedroom "
                "to the west, the bathroom\nto the east, the North Hall"
                " to the north, and the exit to the south.",
                4, 3, 2, 1)

    room_list.append(room)

    # Bedroom
    room = Room("You are in the bedroom. Only path is back to the South Hall.",
                None, 1, None, None)

    # North Hall
    room = Room("You're in the North Hall. There is the kitchen to the west,"
                "the living room\nto the east, the back porch to the north,"
                "and the South Hall to the south.", 6, 5, 1, 6)

    room_list.append(room)



    room_list.append(room)

    # Bathroom
    room = Room("You are in the bathroom. There is the South Hall\nto the west and"
                " the living room to the north.", 5, None, None, 0)

    room_list.append(room)

    # Living room
    room = Room("You're are in the living room. There is the \nNorth Hall to the west and "
                "the bathroom to the south.", None, None, 3, 4)

    room_list.append(room)

    # Kitchen
    room = Room("You are in the kitchen. Only way out is to the North Hall, which is "
                "to the east.", None, 4, None, None)

    room_list.append(room)

    # Back Porch
    room = Room("You are outside on the back porch. Only path is back to the North Hall, "
                "which is to the south.", None, None, 4, None)

    room_list.append(room)


    current_room = 0

    done = False

    while not done:
        print(room_list[current_room].description)
        print()
        answer = input("What direction do you wanna go? ")
        if answer.lower() == "n" or answer.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("Homie you can't go that way :skull:")
            else:
                current_room = next_room



main()