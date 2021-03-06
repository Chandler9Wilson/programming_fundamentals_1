# Name: Chandler Wilson
# Date: 06/14/2018
# COSC1336, Lab 3, 7 parts:
#   part 1: Dress for weather
#   part 2: Flowchart
#   part 3: Rock, paper, scissors
#   part 4: Seasons
#   part 5: Drive car
#   part 6: Combine into one file (started from part 7 so not applicable)
#   part 7: User decision structure
import time


def hello_user():
    horizontal_rule()
    print('Hello what would you like to do?')
    horizontal_rule()
    print('    1. Dress based on the weather')
    print('    2. Run the flowchart')
    print('    3. Play rock, paper, scissors')
    print('    4. Choose a season')
    print('    5. Should you drive?')
    print('    6. Quit')
    horizontal_rule()
    user_input = input('Enter a number (1-6): ')

    if user_input is '1':
        horizontal_rule()
        how_to_dress()
        # Delay recursive call so the user has a chance to read output
        delay(hello_user, 2)
    elif user_input is '2':
        horizontal_rule()
        flowchart()
        delay(hello_user, 2)
    elif user_input is '3':
        horizontal_rule
        rock_paper_scissor()
        delay(hello_user, 2)
    elif user_input is '4':
        horizontal_rule()
        season()
        delay(hello_user, 2)
    elif user_input is '5':
        horizontal_rule()
        should_you_drive()
        delay(hello_user, 2)
    elif user_input is '6':
        horizontal_rule()
        print('Goodbye')
        exit()
    else:
        horizontal_rule()
        print('Please enter a valid integer (1-6)')
        horizontal_rule()
        # Delay recursive call so the user has a chance to read error
        delay(hello_user, 1.5)


def how_to_dress():
    def is_it_raining():
        if raining_outside in ['Y', 'y', 'yes']:
            print('Bring an umbrella')
        elif raining_outside in ['N', 'n', 'no']:
            print("Hopefully we aren't in a drought")
        else:
            print('-' * 30)
            print('ERROR: Please enter y or n')
            print('-' * 30)
            # Delay recursive call so the user has a chance to read error
            delay(is_it_raining, 1)

    print('Go to the window')
    temperature_outside = input(
        'What temperature does the thermometer on the window display?: ')

    try:
        temperature_outside = int(temperature_outside)
    except ValueError:
        print('-' * 30)
        print('ERROR: Please enter an integer in degrees fahrenheit for the',
              'temperature outside')
        print('-' * 30)
        # Delay recursive call so the user has a chance to read error
        delay(how_to_dress, 1)
    else:
        if temperature_outside <= 40:
            print('Grab a coat before you go outside')

    print('Open the door')
    raining_outside = input('Is it raining outside (y/n)?: ')

    is_it_raining()

    print('Go outside and enjoy the day.')


def flowchart():
    print('Inspect your wordworking project.')
    stained_and_sealed = input(
        'Have you stained and sealed your project? (y/n): ')

    if stained_and_sealed in ['Y', 'y', 'yes']:
        print('Let your project cure overnight.')
    elif stained_and_sealed in ['N', 'n', 'no']:
        do_you_want_to = input(
            'Do you intend to stain and seal your project? (y/n): ')

        if do_you_want_to in ['Y', 'y', 'yes']:
            print('Stain and seal your project then let it cure overnight')

    print('Enjoy your woodworking project.')


def rock_paper_scissor():
    def rock_paper_scissor_prompt():
        player_1 = sanitize_rps_input(input(
            "What is player one's choice?: r)ock, p)aper, or s)cissors: "))
        player_2 = sanitize_rps_input(input(
            "What is player two's choice?: r)ock, p)aper, or s)cissors: "))

        result = determine_rps_result(player_1, player_2)

        horizontal_rule()
        print('Player one', result, 'player two because',
              player_1, result, player_2)

    def sanitize_rps_input(input):
        if input in ['r', 'R']:
            return 'rock'
        elif input in ['p', 'P']:
            return 'paper'
        elif input in ['s', 'S']:
            return 'scissors'
        else:
            # Default to rock if invalid
            return 'rock'

    def determine_rps_result(player_1, player_2):
        rock_paper_scissor_table = {
            'rock': {
                'scissors': 'beats',
                'paper': 'loses to',
                'rock': 'ties'
            },
            'paper': {
                'scissors': 'loses to',
                'paper': 'ties',
                'rock': 'wins'
            },
            'scissors': {
                'scissors': 'ties',
                'paper': 'beats',
                'rock': 'loses to'
            }
        }

        return rock_paper_scissor_table[player_1][player_2]

    rock_paper_scissor_prompt()


def season():
    season_input = input('What is the season? (1-4): ')

    if season_input is '1':
        print('Winter isnt very cold here in Texas.')
    elif season_input is '2':
        print("Spring is green if we aren't in a drought.")
    elif season_input is '3':
        print('Summer is always hot.')
    elif season_input is '4':
        print('Fall is usally hot also, but sometimes it cooler.')
    else:
        print("ERROR: Couldn't process your input skipping this section")


def should_you_drive():
    battery_charged = True
    got_car = True
    drunk = False
    gas = 2  # (gallons) # gas currently in the tank of the car
    distance = 100  # miles from home
    mpg = 35  # miles per gallon expected to be used driving home
    nighttime = False
    headlights_out = True

    if (battery_charged and got_car and not drunk and
            (gas * mpg) >= distance and not nighttime and not headlights_out):
        print('Drive home')
    else:
        print('Do not drive home')


# Some utility functions


def horizontal_rule():
    print(30 * '-')


def delay(callback, seconds):
    """Delay a function call using time.sleep"""
    time.sleep(seconds)
    callback()


hello_user()

# Test below
#
# (env) chandler@chandler-G551JM: ~/ACC/programming_fundamentals_1/labs/decision_structures_L3$ python TT18_L3_Wilson_parts1-7.py
# ------------------------------
# Hello what would you like to do?
# ------------------------------
#     1. Dress based on the weather
#     2. Run the flowchart
#     3. Play rock, paper, scissors
#     4. Choose a season
#     5. Should you drive?
#     6. Quit
# ------------------------------
# Enter a number(1-6): 1
# ------------------------------
# Go to the window
# What temperature does the thermometer on the window display?: 52
# Open the door
# Is it raining outside(y/n)?: n
# Hopefully we aren't in a drought
# Go outside and enjoy the day.
# ------------------------------
# Hello what would you like to do?
# ------------------------------
#     1. Dress based on the weather
#     2. Run the flowchart
#     3. Play rock, paper, scissors
#     4. Choose a season
#     5. Should you drive?
#     6. Quit
# ------------------------------
# Enter a number(1-6): 2
# ------------------------------
# Inspect your wordworking project.
# Have you stained and sealed your project? (y/n): y
# Let your project cure overnight.
# Enjoy your woodworking project.
# ------------------------------
# Hello what would you like to do?
# ------------------------------
#     1. Dress based on the weather
#     2. Run the flowchart
#     3. Play rock, paper, scissors
#     4. Choose a season
#     5. Should you drive?
#     6. Quit
# ------------------------------
# Enter a number(1-6): 3
# What is player one's choice?: r)ock, p)aper, or s)cissors: r
# What is player two's choice?: r)ock, p)aper, or s)cissors: p
# - -----------------------------
# Player one loses to player two because rock loses to paper
# - -----------------------------
# Hello what would you like to do?
# - -----------------------------
# 1. Dress based on the weather
# 2. Run the flowchart
# 3. Play rock, paper, scissors
# 4. Choose a season
# 5. Should you drive?
# 6. Quit
# - -----------------------------
# Enter a number(1-6): 4
# - -----------------------------
# What is the season? (1-4): 1
# Winter isnt very cold here in Texas.
# ------------------------------
# Hello what would you like to do?
# - -----------------------------
# 1. Dress based on the weather
# 2. Run the flowchart
# 3. Play rock, paper, scissors
# 4. Choose a season
# 5. Should you drive?
# 6. Quit
# - -----------------------------
# Enter a number(1-6): 5
# - -----------------------------
# Do not drive home
