# Name: Chandler Wilson
# Date: 07/02/2018
# COSC1336, Lab 5
import math


def intro():
    #  1) define 1 function f1 with: no parameters, no return
    def f1():
        print(math.pi)

    #  2) define 1 function f2 with: 1 parameter, no return.
    def f2(is_it_even):
        if is_it_even % 2:
            print('This number is odd')
        else:
            print('This number is even')

    #  3) define 1 function f3 with: 2 parameters, no return.
    def f3(first_int, second_int):
        added = first_int + second_int
        print(first_int, '+', second_int, '=', added)

    #  4) define 1 function f4 with: 2 parameters, 1 return.
    def f4(first_int, second_int):
        return first_int + second_int

    #  5) define 1 function f5 with: 2 parameters, 2 returns.
    def f5(add_1, square):
        add_1 += 1
        square *= square
        return add_1, square

    #  6) define 1 function f6 with: no parameters, 1 return.
    def f6():
        return math.pi

    #  7) define 1 function f7 with: no parameters, 2 returns.
    def f7():
        return (math.pi * 2), math.e

    #  8) define 1 function f8 with: 3 keyword parameters, 1 return.
    def f8(to_add_1, to_add_2, to_add_3):
        return to_add_1 + to_add_2 + to_add_3

    #  9) define 3 functions: f9, f9a, f9b. f9 calls f9a and f9b. All
    #  0 parameters, 0 return.
    def f9a():
        print('The better radian is', end=' ')

    def f9b():
        print(math.pi * 2)

    def f9():
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

    def f10():
        print('The math module has 3 interesting constants ', end='')
        f10a()
        f10b()
        f10c()

    f1()
    f2(6)
    f3(5, 6)
    f4(5, 6)
    f5(11, 25)
    f6()
    f7()
    f8(1, 2, 3)
    f9()
    f10()

# For the remaining parts,


def launch():  # Part 1. Get startup code from launch.py (provided)
    pass


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
