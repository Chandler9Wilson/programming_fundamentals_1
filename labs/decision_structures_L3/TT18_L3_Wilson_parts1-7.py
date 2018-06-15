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
        rock_paper_scissor()
        delay(hello_user, 2)
    elif user_input is '3':
        horizontal_rule
        calculate_profit()
        delay(hello_user, 2)
    elif user_input is '4':
        horizontal_rule()
        draw_initials()
        hello_user()
    elif user_input is '5':
        horizontal_rule()
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


# Some utility functions

def horizontal_rule():
    print(30 * '-')


def delay(callback, seconds):
    """Delay a function call using time.sleep"""
    time.sleep(seconds)
    callback()


hello_user()
