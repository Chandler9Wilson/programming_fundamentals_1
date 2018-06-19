# Name: Chandler Wilson
# Date: 06/19/2018
# COSC1336, Lab 4, 9 parts:
#   part 1: Draw boxes
#   part 2: Draw triangles
#   part 3: Austin Temperature Stats
#   part 4: Is it prime?
#   part 5: Turtle graphics
#   part 6: Combine into one file (started from part 7 so not applicable)
#   part 7: User decision structure
#   part 8: Is it prime optimizations (Use timer to record improvments)
#   part 9: nth prime number


def hello_user():
    horizontal_rule()
    print('Hello what would you like to do?')
    horizontal_rule()
    print('    1. Draw boxes')
    print('    2. Draw triangles')
    print('    3. Play rock, paper, scissors')
    print('    4. Choose a season')
    print('    5. Should you drive?')
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
        rock_paper_scissor()
        hello_user()
    elif user_input is '4':
        horizontal_rule()
        season()
        hello_user()
    elif user_input is '5':
        horizontal_rule()
        should_you_drive()
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

    def convert_to_int(box_size):
        try:
            return int(box_size)
        except ValueError:
            horizontal_rule()
            print('ERROR: Please enter an integer for the box size')
            horizontal_rule()
            draw_boxes()

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
                    if width is 0 or width is (box_size - 1):
                        print('*', end='')
                    else:
                        print(' ', end='')

        # print newline after end of box
        print()

    box_size = input('What box size would you like? (0 to quit): ')

    box_size = convert_to_int(box_size)

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
        hello_user()


def draw_triangles():
    return None


def horizontal_rule():
    print(30 * '-')


hello_user()
