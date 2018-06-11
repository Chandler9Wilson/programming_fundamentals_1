# Name: Chandler Wilson
# COSC1336, Lab 2, 4 parts:
#   part 1: Compute MPG
#   part 2: Convert temperature
#   part 3: Stock sale
#   part 4: Draw initials using turtle graphics
import time


def hello_user():
    horizontal_rule()
    print('Hello what would you like to do?')
    horizontal_rule()
    print('    1. Compute MPG')
    print('    2. Convert Celsius to Fahrenheit')
    print('    3. Compute Stock Gain or Loss')
    print("    4. Draw Chandler's Initials")
    print('    5. Run all of the above')
    print('    6. Quit')
    horizontal_rule()
    user_input = input('Enter a number (1-6): ')

    if user_input is '1':
        horizontal_rule()
        compute_mpg()
        # Delay recursive call so the user has a chance to read output
        delay(hello_user, 2)
    elif user_input is '2':
        horizontal_rule()
        convert_temp()
        # Delay recursive call so the user has a chance to read output
        delay(hello_user, 2)
    elif user_input is '3':
        horizontal_rule
        print('You entered 3')
        # Delay recursive call so the user has a chance to read output
        delay(hello_user, 2)
    elif user_input is '4':
        print('-' * 30)
        print('You entered 4')
    elif user_input is '5':
        print('-' * 30)
        print('You entered 5')
        # Delay recursive call so the user has a chance to read output
        delay(hello_user, 2)
    elif user_input is '6':
        print('-' * 30)
        print('Goodbye')
        exit()
    else:
        print('-' * 30)
        print('Please enter a valid integer (1-6)')
        print('-' * 30)
        # Delay recursive call so the user has a chance to read error
        delay(hello_user, 1.5)


def compute_mpg():
    """Collects user input and returns mpg based on miles travelled and
    gallons used.
    """
    vehicle_make = input('What is the cars make?: ')
    vehicle_model = input('What is the cars model?: ')
    miles_traveled = input('How many miles were traveled on this trip?: ')
    gallons_used = input('How many gallons were used on this trip?: ')

    try:
        gas_mileage_unformated = float(miles_traveled) / float(gallons_used)
    except ValueError:
        print('-' * 30)
        print('ERROR: Please enter an integer or float on miles traveled and' +
              ' gallons used')
        print('-' * 30)
        # Delay recursive call so the user has a chance to read error
        time.sleep(1)

        compute_mpg()
    else:
        gas_mileage = format(gas_mileage_unformated, '.1f')
        output_list = ['Your', vehicle_make, vehicle_model, 'traveled',
                       miles_traveled, 'miles on', gallons_used,
                       'gallons at a rate of', gas_mileage,
                       'miles to the gallon.']
        output_statement = ' '.join(output_list)

        print('-' * 30)
        print(output_statement)


def convert_temp():
    celsius_temperature = input('What is the temperature you would like to ' +
                                'convert?: ')

    try:
        fahrenheit_unformated = float(celsius_temperature) * 9 / 5 + 32
    except ValueError:
        print('-' * 30)
        print('ERROR: Please enter an integer or float for the temperature')
        print('-' * 30)
        # Delay recursive call so the user has a chance to read error
        time.sleep(1)

        convert_temp()
    else:
        fahrenheit_temp = format(fahrenheit_unformated, '.1f')
        output_list = [celsius_temperature, 'degrees celsius is approximately',
                       'equal to', fahrenheit_temp, 'degrees fahrenheit.']
        output_statement = ' '.join(output_list)

        print('-' * 30)
        print(output_statement)


def horizontal_rule():
    print(30 * '-')


def delay(callback, seconds):
    """Delay a function call using time.sleep"""
    time.sleep(seconds)
    callback()


hello_user()
