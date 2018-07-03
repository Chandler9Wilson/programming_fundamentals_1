# Name: Chandler Wilson
# Date: 07/02/2018
# COSC1336, Lab 5, 6 parts:
#   part 0: Write 10 functions in different 'design patterns'
#   part 1: Tidy up rocket launch code
#   part 2: Tip/Tax Table
#   part 3: Data passing
#   part 4: Whole is greater than the sum of its parts
#   part 5: Write ACC with functions and turtle graphics
import math


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


def tip_table():  # Part 2. Get startup code from tip_table.py (provided)
    pass


def scope():  # Part 3. Get startup code from scope.py (provided)
    pass


def sort():  # Part 4. No startup code provided. See instructions.
    pass


def ACC():  # Part 5. Extra Credit: no startup code provided. See instructions.
    pass


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
