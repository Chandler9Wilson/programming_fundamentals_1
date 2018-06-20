# Name: Chandler Wilson
# Date: 06/19/2018
# COSC1336, Lab 4, 7 parts:
#   part 1: Draw boxes
#   part 2: Draw triangles
#   part 3: Austin Temperature Stats
#   part 4: Is it prime?
#   part 5: Turtle graphics
#   part 6: Combine into one file (started from part 7 so not applicable)
#   part 7: User decision structure


def hello_user():
    horizontal_rule()
    print('Hello what would you like to do?')
    horizontal_rule()
    print('    1. Draw boxes')
    print('    2. Draw triangles')
    print('    3. Compute statistics about Austin temperatures')
    print('    4. Is this number prime?')
    print('    5. Draw spiral circles')
    print('    6. Quit')
    horizontal_rule()
    user_input = input('Enter a number (1-6): ')

    if user_input is '1':
        horizontal_rule()
        draw_boxes()
        hello_user()
    elif user_input is '2':
        horizontal_rule()
        draw_triangles()
        hello_user()
    elif user_input is '3':
        horizontal_rule
        austin_temperature_statistics()
        hello_user()
    elif user_input is '4':
        horizontal_rule()
        is_it_prime()
        hello_user()
    elif user_input is '5':
        horizontal_rule()
        draw_spiral_circles()
        hello_user()
    elif user_input is '6':
        horizontal_rule()
        print('Goodbye')
        # Exit the program (really just this function)
        return
    else:
        horizontal_rule()
        print('Please enter a valid integer (1-6)')
        horizontal_rule()
        hello_user()


def draw_boxes():

    def draw_solid_box(box_size):
        for length in range(0, box_size):
            print()
            for width in range(0, box_size):
                print('*', end='')

        # print newline after end of box
        print()

    def draw_outline_box(box_size):
        box_range = range(0, box_size)

        for length in box_range:
            print()

            # Print solid lines for the top and bottom
            if length is 0 or length is (box_size - 1):
                for width in box_range:
                    print('*', end='')
            else:
                for width in box_range:
                    # if start or end column
                    if width is 0 or width is (box_size - 1):
                        print('*', end='')
                    else:
                        print(' ', end='')

        # print newline after end of box
        print()

    box_size = input('What box size would you like? (0 to quit): ')
    convert_error_message = 'ERROR: Please enter an integer for the box size'

    box_size = convert_to_int(box_size, draw_boxes, convert_error_message)

    if box_size > 0 and (box_size % 2) == 0:
        draw_solid_box(box_size)
        horizontal_rule()
        draw_boxes()
    elif box_size > 0 and (box_size % 2) != 0:
        draw_outline_box(box_size)
        horizontal_rule()
        draw_boxes()
    elif box_size < 0:
        horizontal_rule()
        print('ERROR: Please enter a positive integer for the box size')
        horizontal_rule()
        draw_boxes()
    elif box_size == 0:
        return


def draw_triangles():

    def draw_triangle(triangle_size):
        triangle_range = range(0, triangle_size)

        for index in triangle_range:
            width = index + 1
            print('*' * width)

    triangle_size = input('What size triangle would you like? (0 to quit): ')
    convert_error_message = 'ERROR: Please enter an integer for the ' + \
        'triangle size'

    triangle_size = convert_to_int(triangle_size, draw_triangles,
                                   convert_error_message)

    if triangle_size > 0:
        triangle_range = range(0, triangle_size)

        for index in triangle_range:
            horizontal_rule()
            triangle_size = index + 1
            draw_triangle(triangle_size)
        horizontal_rule()
        draw_triangles()
    elif triangle_size < 0:
        horizontal_rule()
        print('ERROR: Please enter a positive integer for the triangle size')
        horizontal_rule()
        draw_triangles()
    elif triangle_size == 0:
        return


def austin_temperature_statistics():

    def temp_input():
        temp = input(
            'Input a temperature (farenheit) to add to the list (q to quit): ')
        return temp

    def valid_temp(temp):
        if -5 <= temp <= 115:
            return True
        else:
            return False

    def input_and_validation():
        temp = temp_input()

        if temp in ['Q', 'q', 'quit']:
            compute_stats()
        else:
            convert_error_message = 'ERROR: Please enter an integer for ' + \
                'the temperature'
            temp = convert_to_int(temp, input_and_validation,
                                  convert_error_message)

            if valid_temp(temp):
                valid_temp_list.append(temp)
                input_and_validation()
            else:
                invalid_temp_list.append(temp)
                horizontal_rule()
                print('ERROR: Please enter an integer between -5 and 115')
                horizontal_rule()
                input_and_validation()

    def compute_stats():

        def is_freezing(temp):
            if temp <= 32:
                return True
            else:
                return False

        zero_base_offset = 1
        temp_list_length = len(valid_temp_list)
        sorted_temp_list = sorted(valid_temp_list)
        average_temp = sum(sorted_temp_list) / temp_list_length
        freezing_temp_list = list(filter(is_freezing, sorted_temp_list))

        horizontal_rule()
        print('    You entered', temp_list_length, 'temperatures')
        print('    The highest temperature you entered was', sorted_temp_list[(
            temp_list_length - zero_base_offset)], 'degrees farenheit')
        print('    The lowest temperature you entered was',
              sorted_temp_list[0], 'degrees farenheit')
        print('    The average temperature was',
              average_temp, 'degrees farenheit')
        print('    There were', len(freezing_temp_list),
              'temperatures below freezing')
        print('    You entered', temp_list_length, 'valid temperatures')
        print('    You entered', len(invalid_temp_list),
              'invalid temperatures')

    valid_temp_list = []
    invalid_temp_list = []

    input_and_validation()


def is_it_prime(number=None):

    def get_prime_number():
        number = input('Enter a positive integer to see if it is prime ' +
                       '(0 to quit): ')

        try:
            number = int(number)
        except ValueError:
            horizontal_rule()
            print('ERROR: Please enter an integer to test')
            horizontal_rule()
            is_it_prime()
        else:
            if number is 0:
                return

            unoptimized_prime_test(number)

    def unoptimized_prime_test(number):
        is_prime = True
        i = 2

        while i < number:
            if (number % i) == 0:
                is_prime = False
                break
            else:
                i += 1

        if is_prime:
            print(number, 'is prime')
            get_prime_number()
        else:
            print(number, 'is composite')
            get_prime_number()

    if number:
        unoptimized_prime_test(number)
    else:
        get_prime_number()


def draw_spiral_circles():
    import turtle

    # Runs turtle again after exitonclick()
    turtle.TurtleScreen._RUNNING = True

    NUM_CIRCLES = 36
    RADIUS = 100
    ANGLE = 10
    ANIMATION_SPEED = 0

    turtle.speed(ANIMATION_SPEED)

    for x in range(NUM_CIRCLES):
        turtle.circle(RADIUS)
        turtle.left(ANGLE)

    # Exit turtle on User click
    turtle.exitonclick()


# Some utility functions


def convert_to_int(int_to_convert,
                   callback,
                   error_message='ERROR: Please enter an integer'):
    try:
        return int(int_to_convert)
    except ValueError:
        horizontal_rule()
        print(error_message)
        horizontal_rule()
        callback()


def horizontal_rule():
    print(30 * '-')


hello_user()

# Test output below
# (env) chandler@chandler-G551JM:~/ACC/programming_fundamentals_1/labs/repetition_structures_L4$ python TT18_L4_Wilson_parts1-6.py
# ------------------------------
# Hello what would you like to do?
# ------------------------------
#     1. Draw boxes
#     2. Draw triangles
#     3. Compute statistics about Austin temperatures
#     4. Is this number prime?
#     5. Draw spiral circles
#     6. Quit
# ------------------------------
# Enter a number (1-6): 1
# ------------------------------
# What box size would you like? (0 to quit): 3

# ***
# * *
# ***
# ------------------------------
# What box size would you like? (0 to quit): 5

# *****
# *   *
# *   *
# *   *
# *****
# ------------------------------
# What box size would you like? (0 to quit): 4

# ****
# ****
# ****
# ****
# ------------------------------
# What box size would you like? (0 to quit): 0
# ------------------------------
# Hello what would you like to do?
# ------------------------------
#     1. Draw boxes
#     2. Draw triangles
#     3. Compute statistics about Austin temperatures
#     4. Is this number prime?
#     5. Draw spiral circles
#     6. Quit
# ------------------------------
# Enter a number (1-6): 2
# ------------------------------
# What size triangle would you like? (0 to quit): 3
# ------------------------------
# *
# ------------------------------
# *
# **
# ------------------------------
# *
# **
# ***
# ------------------------------
# What size triangle would you like? (0 to quit): 0
# ------------------------------
# Hello what would you like to do?
# ------------------------------
#     1. Draw boxes
#     2. Draw triangles
#     3. Compute statistics about Austin temperatures
#     4. Is this number prime?
#     5. Draw spiral circles
#     6. Quit
# ------------------------------
# Enter a number (1-6): 3
# Input a temperature (farenheit) to add to the list (q to quit): 12
# Input a temperature (farenheit) to add to the list (q to quit): 45
# Input a temperature (farenheit) to add to the list (q to quit): 78
# Input a temperature (farenheit) to add to the list (q to quit): 123
# ------------------------------
# ERROR: Please enter an integer between -5 and 115
# ------------------------------
# Input a temperature (farenheit) to add to the list (q to quit): 456
# ------------------------------
# ERROR: Please enter an integer between -5 and 115
# ------------------------------
# Input a temperature (farenheit) to add to the list (q to quit): -4
# Input a temperature (farenheit) to add to the list (q to quit): 0
# Input a temperature (farenheit) to add to the list (q to quit): 99
# Input a temperature (farenheit) to add to the list (q to quit): Q
# ------------------------------
#     You entered 6 temperatures
#     The highest temperature you entered was 99 degrees farenheit
#     The lowest temperature you entered was -4 degrees farenheit
#     The average temperature was 38.333333333333336 degrees farenheit
#     There were 3 temperatures below freezing
#     You entered 6 valid temperatures
#     You entered 2 invalid temperatures
# ------------------------------
# Hello what would you like to do?
# ------------------------------
#     1. Draw boxes
#     2. Draw triangles
#     3. Compute statistics about Austin temperatures
#     4. Is this number prime?
#     5. Draw spiral circles
#     6. Quit
# ------------------------------
# Enter a number (1-6): 4
# ------------------------------
# Enter a positive integer to see if it is prime (0 to quit): 9008711
# 9008711 is composite
# Enter a positive integer to see if it is prime (0 to quit): 0
# ------------------------------
# Hello what would you like to do?
# ------------------------------
#     1. Draw boxes
#     2. Draw triangles
#     3. Compute statistics about Austin temperatures
#     4. Is this number prime?
#     5. Draw spiral circles
#     6. Quit
# ------------------------------
# Enter a number (1-6): 6
# ------------------------------
# Goodbye