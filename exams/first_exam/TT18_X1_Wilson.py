# Name: Chandler Wilson
# Date: 06/19/2018
# COSC1336, Exam 1, 3 parts:
#   part 1: Maximum capacity for a campus
#   part 2: Enhance part 1
#   part 3: Running total of capacities


def calculate_campus_capacity():

    def get_campus_info(campus_name):
        buildings_on_campus = input('How many buildings on campus?: ')
        classrooms_per_building = input('How many classrooms per building?: ')
        seats_per_classroom = input('How many seats per classroom?: ')

        try:
            buildings_on_campus = int(buildings_on_campus)
            classrooms_per_building = int(classrooms_per_building)
            seats_per_classroom = int(seats_per_classroom)
        except ValueError:
            horizontal_rule()
            # Not the best error message
            print('ERROR: Please enter an integer')
            horizontal_rule()

            get_campus_info(campus_name)
        else:
            campus_capacity = buildings_on_campus * \
                classrooms_per_building * seats_per_classroom

            # Keep a running total of capacities
            campus_capacity_list.append(campus_capacity)

            formatted_campus_capacity = format(campus_capacity, ',')

            print("ACC's", campus_name, 'campus can serve up to',
                  formatted_campus_capacity, 'students.')

    def get_campus_abbreviation():
        campus_name = input('Please enter an ACC campus abbreviation ' +
                            '(q to quit): ')

        if campus_name in ['Q', 'q', 'quit']:
            horizontal_rule()
            return greeting_menu()
        elif campus_name in ['NRG', 'RRC', 'RGC', 'CYP', 'HLC']:
            get_campus_info(campus_name)
            get_campus_abbreviation()
        else:
            horizontal_rule()
            print(
                'ERROR: Please enter a valid ACC campus abbreviation',
                '(NRG, RRC, RGC, CYP, HLC)')
            horizontal_rule()
            get_campus_abbreviation()

    get_campus_abbreviation()


def greeting_menu():
    print('Hello your options are:')
    print('    d)isplay detailed instructions')
    print('    c)alculate campus capacity')
    print('    q)uit program')
    user_choice = input('Which option do you chose? (d,c,q): ')

    if user_choice in ['d', 'D']:
        horizontal_rule()
        print('Enter an ACC campus abbreviation then enter number of ' +
              'buildings, classrooms and average seats per classroom, and' +
              ' this program will output the total seating capacity for ' +
              'that campus.')
        horizontal_rule()
        greeting_menu()
    elif user_choice in ['c', 'C']:
        calculate_campus_capacity()
    elif user_choice in ['q', 'Q', 'quit']:
        total_capacity = format(sum(campus_capacity_list), ',')

        horizontal_rule()
        print('The accumulated total maximum capacity for all',
              'campuses entered is:', total_capacity)
        return
    else:
        print('ERROR: Please enter d, c, or q as your option')
        horizontal_rule()
        greeting_menu()


def horizontal_rule():
    print(30 * '-')


campus_capacity_list = []
first_run_greeting = 'This program computes the enrollment capacity for ' + \
    'an ACC campus.'

print(first_run_greeting)
horizontal_rule()

greeting_menu()

# Test output below
# (env) chandler@chandler-G551JM: ~/ACC/programming_fundamentals_1/tests/first_test$ python TT18_X1_Wilson.py
# This program computes the enrollment capacity for an ACC campus.
# ------------------------------
# Hello your options are:
#   d)isplay detailed instructions
#   c)alculate campus capacity
#   q)uit program
# Which option do you chose? (d, c, q): d
# - -----------------------------
# Enter an ACC campus abbreviation then enter number of buildings, classrooms and average seats per classroom, and this program will output the total seating capacity for thatcampus.
# ------------------------------
# Hello your options are:
#   d)isplay detailed instructions
#   c)alculate campus capacity
#   q)uit program
# Which option do you chose? (d, c, q): c
# Please enter an ACC campus abbreviation(q to quit): NRG
# How many buildings on campus?: 4
# How many classrooms per building?: 14
# How many seats per classroom?: 24
# ACC's NRG campus can serve up to 1,344 students.
# Please enter an ACC campus abbreviation(q to quit): CYP
# How many buildings on campus?: 5
# How many classrooms per building?: 15
# How many seats per classroom?: 25
# ACC's CYP campus can serve up to 1,875 students.
# Please enter an ACC campus abbreviation(q to quit): ACC
# - -----------------------------
# ERROR: Please enter a valid ACC campus abbreviation(NRG, RRC, RGC, CYP, HLC)
# - -----------------------------
# Please enter an ACC campus abbreviation(q to quit): RRC
# How many buildings on campus?: 6
# How many classrooms per building?: 16
# How many seats per classroom?: 26
# ACC's RRC campus can serve up to 2,496 students.
# Please enter an ACC campus abbreviation(q to quit): q
# - -----------------------------
# Hello your options are:
#   d)isplay detailed instructions
#   c)alculate campus capacity
#   q)uit program
# Which option do you chose? (d, c, q): q
# The accumulated total maximum capacity for all campuses entered is: 5,715
