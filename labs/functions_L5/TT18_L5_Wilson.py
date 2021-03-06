# Name: Chandler Wilson
# Date: 07/02/2018
# COSC1336, Lab 5, 6 parts:
#   part 0: Write 10 functions in different 'design patterns'
#   part 1: Tidy up rocket launch code
#   part 2: Tip/Tax Table
#   part 3: Scope
#   part 4: Sort
#   part 5: Write ACC with functions and turtle graphics
import math
from random import randint
import turtle


def intro():
    #  1) define 1 function f1 with: no parameters, no return
    def f1_print_pi():
        print(math.pi)

    #  2) define 1 function f2 with: 1 parameter, no return.
    def f2_check_if_even(is_it_even):
        if is_it_even % 2:
            print('This number is odd')
        else:
            print('This number is even')

    #  3) define 1 function f3 with: 2 parameters, no return.
    def f3_print_added(first_int, second_int):
        added = first_int + second_int
        print(first_int, '+', second_int, '=', added)

    #  4) define 1 function f4 with: 2 parameters, 1 return.
    def f4_return_added(first_int, second_int):
        return first_int + second_int

    #  5) define 1 function f5 with: 2 parameters, 2 returns.
    def f5_return_add_and_square(add_1, square):
        add_1 += 1
        square *= square
        return add_1, square

    #  6) define 1 function f6 with: no parameters, 1 return.
    def f6_return_pi():
        return math.pi

    #  7) define 1 function f7 with: no parameters, 2 returns.
    def f7_return_tau_and_e():
        return (math.pi * 2), math.e

    #  8) define 1 function f8 with: 3 keyword parameters, 1 return.
    def f8_return_add_three(to_add_1, to_add_2, to_add_3):
        return to_add_1 + to_add_2 + to_add_3

    #  9) define 3 functions: f9, f9a, f9b. f9 calls f9a and f9b. All
    #  0 parameters, 0 return.
    def f9a():
        print('The better radian is', end=' ')

    def f9b():
        print(math.pi * 2)

    def f9_print_better_radian():
        f9a()
        f9b()

    # 10) define 4 function f10, f10a, f10b, f10c. f10 calls f10a,
    # f10a, f10b, f10c. All 0 parameters, 0 return.
    def f10a():
        print(str(math.pi) + ', ', end='')

    def f10b():
        print(str(math.e) + ', and ', end='')

    def f10c():
        # Had to update all math.tau because it is only in 3.6+
        print(str(math.pi * 2) + '.')

    def f10_print_constants():
        print('The math module has 3 interesting constants ', end='')
        f10a()
        f10b()
        f10c()

    f1_print_pi()
    f2_check_if_even(6)
    f3_print_added(5, 6)
    f4_return_added(5, 6)
    f5_return_add_and_square(11, 25)
    f6_return_pi()
    f7_return_tau_and_e()
    f8_return_add_three(1, 2, 3)
    f9_print_better_radian()
    f10_print_constants()


def launch():
    """Launch a rocket into space."""
    def fill_booster(booster_number):
        print('Fill booster fuel tank ' + str(booster_number) + '.')
        print('  open valve')
        print('  pre-freeze tank')
        print('  attach filler hose')
        print('  pressurize fuel supply')
        print('  fill tank')
        print('  secure and seal shutoff valve')

    def start_engine(engine_number):
        print('Start engine ' + str(engine_number))
        print('  ignition sequence start')
        print('  start ignition spark generator')
        print('  open fuel valve')
        print('  verify ignition temperature')
        print('  stop ignition spark generator')
        print('  engine ' + str(engine_number) + ' is started')

    input("Press enter to begin the launch sequence...")

    print("This program launches a rocket.")
    print("start launch sequence")

    fill_booster(1)

    fill_booster(2)

    fill_booster(3)

    start_engine(1)

    start_engine(2)

    print("3, 2, 1, 0, BLASTOFF!!!")
    print("Thank you. Keep looking up!")


def tip_table():
    """Collect a bill then display a tip table for that bill"""
    # Enter the bill with tax: $16.24
    # Total due with 10% tip: $17.74
    # Total due with 15% tip: $18.49
    # Total due with 20% tip: $19.24
    # Total due with 25% tip: $19.99
    def display_total_due(bill_with_tax, tip_rate, tax_rate):
        bill_without_tax = bill_with_tax / (1 + tax_rate)
        tip = bill_without_tax * tip_rate
        total_due = format((bill_with_tax + tip), ',.2f')
        formatted_tip = format(tip_rate, '.0%')
        print('Total due with', str(formatted_tip), 'tip: $' +
              str(total_due))

    def collect_bill():
        try:
            bill_with_tax = float(input('Enter the bill with tax: $'))
        except ValueError:
            print('ERROR: Please enter an int or float for the bill')
            print('-' * 30)
            return collect_bill()
        else:
            return bill_with_tax

    bill_with_tax = collect_bill()
    tip_rate_list = [.1, .15, .20, .25]
    TAX_RATE = 0.0825

    for tip_rate in tip_rate_list:
        display_total_due(bill_with_tax, tip_rate, TAX_RATE)


def scope():  # Part 3. Get startup code from scope.py (provided)

    def less_100(number):
        modified = number - 100
        print('      in less_100. number = ', number,
              ', modified = ', modified, sep='')

    def times_ten(number):
        modified = number * 10
        print('    at top of times_ten: number = ', number,
              ', modified = ', modified, sep='')

        less_100(modified)

        print('    at bot of times_ten: number = ', number,
              ', modified = ', modified, sep='')

    def add_one(number):
        modified = number + 1
        print('  at top of add_one: number = ', number,
              ', modified = ', modified, sep='')

        times_ten(modified)

        print('  at bot of add_one: number = ', number,
              ', modified = ', modified, sep='')

    def collect_number():
        try:
            number = int(input('Please input a number: '))
        except ValueError:
            print('ERROR: Please enter an int')
            print('-' * 30)
            return collect_number()
        else:
            return number

    number = collect_number()

    print('at top of scope: number = ', number, sep='')

    add_one(number)
    times_ten(number)
    less_100(number)

    print('at bot of scope: number = ', number, sep='')


def sort():

    def more_than(a, b):
        if a > b:
            return True
        else:
            return False

    def swap(a, b):
        return b, a

    def sort3(a, b, c):
        if more_than(a, b):
            a, b = swap(a, b)
        if more_than(b, c):
            b, c = swap(b, c)
        if more_than(a, b):
            a, b = swap(a, b)

        return a, b, c

    # Predefined test cases below
    # print(sort3(1, 2, 3))
    # print(sort3(3, 2, 1))
    # print(sort3(1, 3, 2))
    # print(sort3(2, 3, 1))
    # print(sort3(2, 1, 3))
    # print(sort3(1, 1, 1))
    # print(sort3(1, 2, 2))
    # print(sort3(2, 1, 1))

    # Random test cases
    for test in range(1, 11):
        # TODO could probably not repeat this randint line
        a, b, c = randint(1, 100), randint(1, 100), randint(1, 100)
        minn, mid, maxx = sort3(a, b, c)
        print(str(test) + ') random numbers ' + str(a), b,
              str(c) + ' sort to: ' + str(minn), mid, maxx, sep=', ')


def ACC():

    def draw_a(x, y, h):
        half_height = h / 2

        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        # Could remove magic numbers
        turtle.goto((x + 50), h)
        turtle.goto((x + 100), y)
        turtle.penup()
        # This will fail if h is odd I think?
        turtle.goto((x + 25), half_height)
        turtle.pendown()
        turtle.goto((x + 75), half_height)

    def draw_c(x, y, h):
        radius = h / 2

        turtle.penup()
        turtle.goto(x, y)
        turtle.setheading(0)
        turtle.pendown()
        turtle.circle(radius, -180)

    # Runs turtle again after exitonclick()
    turtle.TurtleScreen._RUNNING = True

    turtle.pencolor('purple')
    turtle.pensize(3)

    draw_a(0, 0, 200)
    draw_c(200, 0, 200)
    draw_c(300, 0, 200)

    turtle.hideturtle()

    # Exit turtle on User click
    turtle.exitonclick()


def main():
    print('Hello. This is cosc1336 lab 5 on functions.')
    while True:
        option = input(
            'Enter choice: 0)intro 1)launch 2)tip table 3)scope 4)sort ' +
            '5)ACC 6,q)uit? ')
        option = option.lower()
        if option == '0':
            intro()
        elif option == '1':
            launch()
        elif option == '2':
            tip_table()
        elif option == '3':
            scope()
        elif option == '4':
            sort()
        elif option == '5':
            ACC()
        elif option == '6' or option == 'q':
            break
        else:
            print('  Invalid option, please try again.')
    print('\nGoodbye')


main()

# Test all options in one, last test run, and paste your output below:
# (env) chandler@chandler-G551JM:~/ACC/programming_fundamentals_1/labs/functions_L5$ python TT18_L5_Wilson.py
# Hello. This is cosc1336 lab 5 on functions.
# Enter choice: 0)intro 1)launch 2)tip table 3)scope 4)sort 5)ACC 6,q)uit? 0
# 3.141592653589793
# This number is even
# 5 + 6 = 11
# The better radian is 6.283185307179586
# The math module has 3 interesting constants 3.141592653589793, 2.718281828459045, and 6.283185307179586.
# Enter choice: 0)intro 1)launch 2)tip table 3)scope 4)sort 5)ACC 6,q)uit? 1
# Press enter to begin the launch sequence...
# This program launches a rocket.
# start launch sequence
# Fill booster fuel tank 1.
#   open valve
#   pre-freeze tank
#   attach filler hose
#   pressurize fuel supply
#   fill tank
#   secure and seal shutoff valve
# Fill booster fuel tank 2.
#   open valve
#   pre-freeze tank
#   attach filler hose
#   pressurize fuel supply
#   fill tank
#   secure and seal shutoff valve
# Fill booster fuel tank 3.
#   open valve
#   pre-freeze tank
#   attach filler hose
#   pressurize fuel supply
#   fill tank
#   secure and seal shutoff valve
# Start engine 1
#   ignition sequence start
#   start ignition spark generator
#   open fuel valve
#   verify ignition temperature
#   stop ignition spark generator
#   engine 1 is started
# Start engine 2
#   ignition sequence start
#   start ignition spark generator
#   open fuel valve
#   verify ignition temperature
#   stop ignition spark generator
#   engine 2 is started
# 3, 2, 1, 0, BLASTOFF!!!
# Thank you. Keep looking up!
# Enter choice: 0)intro 1)launch 2)tip table 3)scope 4)sort 5)ACC 6,q)uit? 2
# Enter the bill with tax: $16.24
# Total due with 10% tip: $17.74
# Total due with 15% tip: $18.49
# Total due with 20% tip: $19.24
# Total due with 25% tip: $19.99
# Enter choice: 0)intro 1)launch 2)tip table 3)scope 4)sort 5)ACC 6,q)uit? 3
# Please input a number: 10
# at top of scope: number = 10
#   at top of add_one: number = 10, modified = 11
#     at top of times_ten: number = 11, modified = 110
#       in less_100. number = 110, modified = 10
#     at bot of times_ten: number = 11, modified = 110
#   at bot of add_one: number = 10, modified = 11
#     at top of times_ten: number = 10, modified = 100
#       in less_100. number = 100, modified = 0
#     at bot of times_ten: number = 10, modified = 100
#       in less_100. number = 10, modified = -90
# at bot of scope: number = 10
# Enter choice: 0)intro 1)launch 2)tip table 3)scope 4)sort 5)ACC 6,q)uit? 3
# Please input a number: 100
# at top of scope: number = 100
#   at top of add_one: number = 100, modified = 101
#     at top of times_ten: number = 101, modified = 1010
#       in less_100. number = 1010, modified = 910
#     at bot of times_ten: number = 101, modified = 1010
#   at bot of add_one: number = 100, modified = 101
#     at top of times_ten: number = 100, modified = 1000
#       in less_100. number = 1000, modified = 900
#     at bot of times_ten: number = 100, modified = 1000
#       in less_100. number = 100, modified = 0
# at bot of scope: number = 100
# Enter choice: 0)intro 1)launch 2)tip table 3)scope 4)sort 5)ACC 6,q)uit? 3
# Please input a number: 1000
# at top of scope: number = 1000
#   at top of add_one: number = 1000, modified = 1001
#     at top of times_ten: number = 1001, modified = 10010
#       in less_100. number = 10010, modified = 9910
#     at bot of times_ten: number = 1001, modified = 10010
#   at bot of add_one: number = 1000, modified = 1001
#     at top of times_ten: number = 1000, modified = 10000
#       in less_100. number = 10000, modified = 9900
#     at bot of times_ten: number = 1000, modified = 10000
#       in less_100. number = 1000, modified = 900
# at bot of scope: number = 1000
# Enter choice: 0)intro 1)launch 2)tip table 3)scope 4)sort 5)ACC 6,q)uit? 4
# 1) random numbers 75, 79, 5 sort to: 5, 75, 79
# 2) random numbers 5, 69, 78 sort to: 5, 69, 78
# 3) random numbers 33, 39, 81 sort to: 33, 39, 81
# 4) random numbers 37, 25, 62 sort to: 25, 37, 62
# 5) random numbers 60, 68, 67 sort to: 60, 67, 68
# 6) random numbers 87, 34, 20 sort to: 20, 34, 87
# 7) random numbers 18, 54, 73 sort to: 18, 54, 73
# 8) random numbers 43, 16, 74 sort to: 16, 43, 74
# 9) random numbers 9, 60, 80 sort to: 9, 60, 80
# 10) random numbers 83, 28, 36 sort to: 28, 36, 83
# Enter choice: 0)intro 1)launch 2)tip table 3)scope 4)sort 5)ACC 6,q)uit? 6

# Goodbye