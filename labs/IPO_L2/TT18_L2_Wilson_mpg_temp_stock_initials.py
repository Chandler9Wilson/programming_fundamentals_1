# Name: Chandler Wilson
# Date: 06/12/2018
# COSC1336, Lab 2, 4 parts:
#   part 1: Compute MPG
#   part 2: Convert temperature
#   part 3: Stock sale
#   part 4: Draw initials using turtle graphics
import time
import turtle


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
        compute_mpg()
        horizontal_rule()

        convert_temp()
        horizontal_rule()

        calculate_profit()
        horizontal_rule()

        draw_initials()
        hello_user()
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


def compute_mpg():
    """Collects user input and returns mpg based on miles travelled and
    gallons used.
    """
    intro_statement = 'This part computes gas mileage.'

    print(intro_statement)
    horizontal_rule()
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
        delay(compute_mpg, 1)
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
    """Convert a celsius temp to fahrenheit"""
    intro_statement = 'This part performs a temperature unit conversion ' + \
        'from celsius to fahrenheit.'

    print(intro_statement)
    horizontal_rule()
    celsius_temperature = input('What is the temperature you would like to ' +
                                'convert?: ')
    MELTING_POINT_DIFFERENCE = 32
    ONE_DEGREE_C_TO_F = 9 / 5

    try:
        fahrenheit_unformated = (float(celsius_temperature) *
                                 ONE_DEGREE_C_TO_F +
                                 MELTING_POINT_DIFFERENCE)
    except ValueError:
        print('-' * 30)
        print('ERROR: Please enter an integer or float for the temperature')
        print('-' * 30)
        # Delay recursive call so the user has a chance to read error
        delay(convert_temp, 1)
    else:
        fahrenheit_temp = format(fahrenheit_unformated, '.1f')
        output_list = [celsius_temperature, 'degrees celsius is approximately',
                       'equal to', fahrenheit_temp, 'degrees fahrenheit.']
        output_statement = ' '.join(output_list)

        print('-' * 30)
        print(output_statement)


def calculate_profit():
    intro_statement = 'This part computes the result of a stock transaction.'

    print(intro_statement)
    horizontal_rule()
    number_of_shares_purchased = input('How many shares were bought?: ')
    price_per_share_bought = input('How much was paid per share?: ')
    commision_on_buy = input('What was the commision on the purchase?: ')
    number_of_shares_sold = input('How many shares were sold?: ')
    price_per_share_sold = input('How much was the stock sold at per share?: ')
    commision_on_sell = input('What was the commision on the sale?: ')

    try:
        # strip the dollar sign if it exists
        stripped_price_per_share_bought = strip_dollar(price_per_share_bought)
        stripped_price_per_share_sold = strip_dollar(price_per_share_sold)

        purchase_price = (float(number_of_shares_purchased) *
                          float(stripped_price_per_share_bought))
        sell_price = (float(number_of_shares_sold) *
                      float(stripped_price_per_share_sold))

        # strip the percentage sign if it exists
        stripped_buy_commision = strip_percentage(commision_on_buy)
        stripped_sell_commision = strip_percentage(commision_on_sell)

        # format percentage format to make it easier to work with
        formatted_buy_commision = standardize_percentage_format(
            float(stripped_buy_commision))
        formatted_sell_commision = standardize_percentage_format(
            float(stripped_sell_commision))
    except ValueError:
        print('-' * 30)
        # TODO This is not a great error message
        print('ERROR: Please enter an integer or float for all input values')
        print('-' * 30)
        # Delay recursive call so the user has a chance to read error
        delay(calculate_profit, 1)
    else:
        gross_purchase_price = purchase_price + (purchase_price *
                                                 formatted_buy_commision)
        gross_sell_price = sell_price - (sell_price * formatted_sell_commision)
        gross_profit = gross_sell_price - gross_purchase_price
        formatted_gross_profit = format(gross_profit, ',.2f')

    if gross_profit < 0:
        horizontal_rule()
        print('You lost', '$' + formatted_gross_profit,
              'on your transaction')
    elif gross_profit >= 0:
        horizontal_rule()
        print('You gained', '$' + formatted_gross_profit,
              'on your transaction')


def draw_initials():
    intro_statement = 'This part draws my initials.'

    print(intro_statement)
    horizontal_rule()

    # Runs turtle again after exitonclick()
    turtle.TurtleScreen._RUNNING = True

    turtle.pencolor('purple')
    turtle.pensize(3)

    # Some variables to make sense of stuff
    y_origin = 0
    top_of_w = 250

    # Partial circle for C
    turtle.penup()              # Don't draw while positioning
    turtle.goto(125, y_origin)  # Move to the bottom of C
    turtle.pendown()            # Start drawing
    turtle.circle(125, -180)    # Draw semicircle clockwise with radius 125px
    turtle.penup()              # Don't draw while positioning

    # Draw far left stem of w
    turtle.goto(175, top_of_w)  # Move to the top left of W
    turtle.pendown()            # Start drawing
    # Space each line of w by 50px on x
    turtle.goto(225, y_origin)  # Draw diagnal line to bottom left of W

    # Draw middle left stem of w
    turtle.goto(275, top_of_w)  # Draw diagnal line to middle of W

    # Draw middle right stem of w
    turtle.goto(325, y_origin)  # Draw diagnal line to bottom right of W

    # Draw far right stem of w
    turtle.goto(375, top_of_w)  # Draw diagnal line to top right of W
    turtle.penup()              # Don't draw while positioning

    # Draw 400x400 test box
    # turtle.goto(0, 0)
    # turtle.pendown()
    # turtle.goto(0, 400)
    # turtle.goto(400, 400)
    # turtle.goto(400, 0)
    # turtle.goto(0, 0)
    # turtle.penup()

    # Draw statement above aprox. middle of initials
    turtle.goto(100, 300)
    turtle.write('   CW is for Chandler Wilson, Good-bye!')
    turtle.hideturtle()    # hide turtle to see initials clearly

    # Exit turtle on User click
    turtle.exitonclick()


# Some utility functions

def horizontal_rule():
    print(30 * '-')


def delay(callback, seconds):
    """Delay a function call using time.sleep"""
    time.sleep(seconds)
    callback()


def strip_percentage(to_strip):
    return to_strip.strip('%')


def strip_dollar(to_strip):
    return to_strip.strip('$')


def standardize_percentage_format(percentage):
    if percentage >= 1:
        return percentage / 100
    elif percentage < 1 and percentage > 0:
        return percentage
    else:
        # TODO This could use improvement
        return percentage


hello_user()

# First test below
#
# (env) chandler@chandler-G551JM: ~/ACC/programming_fundamentals_1/labs/IPO_L2$ python TT18_L2_Wilson_mpg_temp_stock_initials.py
# ------------------------------
# Hello what would you like to do?
# ------------------------------
#     1. Compute MPG
#     2. Convert Celsius to Fahrenheit
#     3. Compute Stock Gain or Loss
#     4. Draw Chandler's Initials
#     5. Run all of the above
#     6. Quit
# ------------------------------
# Enter a number(1-6): 5
# ------------------------------
# This part computes gas mileage.
# ------------------------------
# What is the cars make?: Chevy
# What is the cars model?: Impala
# How many miles were traveled on this trip?: 150
# How many gallons were used on this trip?: 5
# ------------------------------
# Your Chevy Impala traveled 150 miles on 5 gallons at a rate of 30.0 miles to the gallon.
# ------------------------------
# This part performs a temperature unit conversion from celsius to fahrenheit.
# ------------------------------
# What is the temperature you would like to convert?: 32
# ------------------------------
# 32 degrees celsius is approximately equal to 89.6 degrees fahrenheit.
# ------------------------------
# This part computes the result of a stock transaction.
# ------------------------------
# How many shares were bought?: 2000
# How much was paid per share?: $40
# What was the commision on the purchase?: 3%
# How many shares were sold?: 2000
# How much was the stock sold at per share?: $42.75
# What was the commision on the sale?: 3%
# ------------------------------
# You gained $535.00 on your transaction
# ------------------------------
# This part draws my initials.
# ------------------------------
#
# Second Test
#
# (env) chandler@chandler-G551JM: ~/ACC/programming_fundamentals_1/labs/IPO_L2$ python TT18_L2_Wilson_mpg_temp_stock_initials.py
# ------------------------------
# Hello what would you like to do?
# ------------------------------
#     1. Compute MPG
#     2. Convert Celsius to Fahrenheit
#     3. Compute Stock Gain or Loss
#     4. Draw Chandler's Initials
#     5. Run all of the above
#     6. Quit
# ------------------------------
# Enter a number(1-6): 5
# ------------------------------
# This part computes gas mileage.
# ------------------------------
# What is the cars make?: Chevy
# What is the cars model?: Traverse
# How many miles were traveled on this trip?: 250
# How many gallons were used on this trip?: 17
# ------------------------------
# Your Chevy Traverse traveled 250 miles on 17 gallons at a rate of 14.7 miles to the gallon.
# ------------------------------
# This part performs a temperature unit conversion from celsius to fahrenheit.
# ------------------------------
# What is the temperature you would like to convert?: 45
# ------------------------------
# 45 degrees celsius is approximately equal to 113.0 degrees fahrenheit.
# ------------------------------
# This part computes the result of a stock transaction.
# ------------------------------
# How many shares were bought?: 2000
# How much was paid per share?: 40.00
# What was the commision on the purchase?: .03
# How many shares were sold?: 2000
# How much was the stock sold at per share?: 42.75
# What was the commision on the sale?: 3%
# ------------------------------
# You gained $535.00 on your transaction
# ------------------------------
# This part draws my initials.
# ------------------------------
