import random

#  introduction
print("Welcome to Breakout! You are running away from your mom who has gone rogue and is \n"
      "chasing you with a wooden spoon! You don't want to get spanked so you are running \n"
      "away. While running away, you must keep track of your water, food, and energy levels. \n"
      "Here are the instructions:")

#  initial instructions
print("\nTo run away, enter R\n"
      "To drink water ,enter W\n"
      "To eat food, enter F\n"
      "To rest, enter S\n"
      "To quit the game, enter Q\n"
      "To check your stats, enter E\n"
      "Let's get started! \n\n")

#  all needed variables
total_yards_ran = 0  #  tracks total yards
yards_ran = 0  #  random number when you run
yards_from_mom = 30  #  pretty self-explanatory
mom_yards_ran = 0  #  how far mom runs on a turn (random)
food = 100  #  food level
food_gained = 0  #  random number when you eat
water = 100  #  water level
water_gained = 0  #  random number when you drink
rest = 100  #  rest level
rest_gained = 0  #  random number when you sleep
done = False  #  game ends when True (user enters q)


def mom_chasing():  #  makes mom run after uses chooses an option
    global mom_yards_ran, yards_from_mom
    mom_yards_ran = random.randrange(25, 45)
    yards_from_mom -= mom_yards_ran
    if yards_from_mom < 20:
        print("Your mom is right on your tail!")


def done_running():  #  goes off whenever the user runs,
    #  changes all the values as necessary
    global yards_ran, food, water, rest, total_yards_ran, yards_from_mom
    if food > 10 and water > 12 and rest > 9:
        yards_ran = random.randrange(50, 90)
        print("You ran away " + str(yards_ran) + " yards.")
        total_yards_ran += yards_ran
        food -= random.randrange(8, 11)
        water -= random.randrange(10, 13)
        rest -= random.randrange(7, 10)
        yards_from_mom += yards_ran
        mom_chasing()
    elif food < 12:
        print("You are too hungry to keep running.")
    elif water < 14:
        print("You are too thirsty to keep running.")
    elif rest < 11:
        print("You are too tired to keep running.")
    print("You have finished running.")


def done_drinking():
    global water_gained, water
    if water < 75:
        water_gained = random.randrange(21, 25)
        print("You take a quick water break and gained", water_gained, "water.")
        water += water_gained
        mom_chasing()
    else:
        print("You aren't thirsty at the moment.")

    print("\nTo run away, enter R\n"
          "To drink water ,enter W\n"
          "To eat food, enter F\n"
          "To rest, enter S\n"
          "To quit the game, enter Q\n")


def done_resting():
    global rest, rest_gained
    if rest < 70:
        rest_gained = random.randrange(24, 30)
        print("You take a quick rest and gained", rest_gained, "rest.")
        rest += rest_gained
        mom_chasing()
    else:
        print("You aren't tired at the moment.")

    print("\nTo run away, enter R\n"
          "To drink water ,enter W\n"
          "To eat food, enter F\n"
          "To rest, enter S\n"
          "To quit the game, enter Q\n")


def done_eating():
    global food, food_gained
    if food < 80:
        food_gained = random.randrange(16, 20)
        print("You take a quick snack break and gained", food_gained, "food.")
        food += food_gained
        mom_chasing()
    else:
        print("You aren't hungry at the moment.")

    print("\nTo run away, enter R\n"
          "To drink water ,enter W\n"
          "To eat food, enter F\n"
          "To rest, enter S\n"
          "To quit the game, enter Q\n")

def stat_check():
    print("You have", food, " food.")
    print("You have", water, " water.")
    print("You have", rest, " rest.")
    print("Mom is", yards_from_mom, "yards behind you.")


while not done:
    user_choice = input("What do you want to do? ")
    print("You entered", user_choice)
    if user_choice.lower() == "q":
        print("Okay, the game has ended. You ran a total of ", total_yards_ran,
              "yards, or ", round(total_yards_ran * 3 / 5280, 3), "miles.")
        done = True
    elif user_choice.lower() == "r":
        done_running()
        if yards_from_mom < 1:
            print("Mom caught up to you! You lose! You ran a total of ", total_yards_ran,
              "yards, or ", round(total_yards_ran * 3 / 5280, 3), "miles.")
            break
    elif user_choice.lower() == "w":
        done_drinking()
        if yards_from_mom < 1:
            print("Mom caught up to you! You lose! You ran a total of ", total_yards_ran,
              "yards, or ", round(total_yards_ran * 3 / 5280, 3), "miles.")
            break
    elif user_choice.lower() == "f":
        done_eating()
        if yards_from_mom < 1:
            print("Mom caught up to you! You lose! You ran a total of ", total_yards_ran,
              "yards, or ", round(total_yards_ran * 3 / 5280, 3), "miles.")
            break
    elif user_choice.lower() == "s":
        done_resting()
        if yards_from_mom < 1:
            print("Mom caught up to you! You lose! You ran a total of ", total_yards_ran,
              "yards, or ", round(total_yards_ran * 3 / 5280, 3), "miles.")
            break
    elif user_choice.lower() == "e":
        stat_check()
    else:
        print("Bro I'm a dumb computer idk what", user_choice, "means.")